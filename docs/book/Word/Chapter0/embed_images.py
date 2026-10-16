#!/usr/bin/env python3
"""
Download images from markdown file and create Word/PDF with embedded images.

Usage:
    python embed_images.py

This script:
1. Creates a virtual environment if needed
2. Parses Chapter_0_Foundations.md for image URLs
3. Downloads images to a local 'images' folder
4. Creates a new Word document with embedded images
5. Optionally converts to PDF
"""

import os
import re
import sys
import subprocess
import urllib.request
from pathlib import Path

# Configuration
SCRIPT_DIR = Path(__file__).parent
VENV_DIR = SCRIPT_DIR / ".venv"
MARKDOWN_FILE = SCRIPT_DIR / "Chapter_0_Foundations.md"
IMAGES_DIR = SCRIPT_DIR / "images"
OUTPUT_DOCX = SCRIPT_DIR / "Chapter_0_Foundations_with_Images.docx"
OUTPUT_PDF = SCRIPT_DIR.parent.parent / "pdf" / "Chapter0" / "Chapter_0_Foundations_with_Images.pdf"

# Image width in document (inches)
IMAGE_WIDTH = 5.5


def setup_venv():
    """Create virtual environment and install dependencies."""
    if not VENV_DIR.exists():
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", str(VENV_DIR)])

    # Get path to pip in venv
    if sys.platform == "win32":
        pip_path = VENV_DIR / "Scripts" / "pip"
        python_path = VENV_DIR / "Scripts" / "python"
    else:
        pip_path = VENV_DIR / "bin" / "pip"
        python_path = VENV_DIR / "bin" / "python"

    # Install dependencies
    print("Installing dependencies...")
    subprocess.check_call([str(pip_path), "install", "-q", "python-docx", "Pillow", "requests"])

    return python_path


def check_dependencies():
    """Check if required packages are available."""
    try:
        from docx import Document
        from PIL import Image
        return True
    except ImportError:
        return False


def run_in_venv():
    """Re-run this script inside the virtual environment."""
    if sys.platform == "win32":
        python_path = VENV_DIR / "Scripts" / "python"
    else:
        python_path = VENV_DIR / "bin" / "python"

    # Re-execute this script with venv python
    os.execv(str(python_path), [str(python_path), __file__])


# Check if we need to set up venv
if not check_dependencies():
    # Check if we're already in the venv
    if not (VENV_DIR / "bin" / "python").exists() or sys.prefix != str(VENV_DIR):
        setup_venv()
        run_in_venv()
        sys.exit(0)

# Now we can import the packages
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from PIL import Image
import requests


def extract_images_from_markdown(md_file: Path) -> list:
    """Extract image URLs and alt text from markdown file."""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern: ![alt text](url)
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    matches = re.findall(pattern, content)

    images = []
    for alt_text, url in matches:
        if url.startswith('http'):
            images.append({
                'alt': alt_text,
                'url': url,
                'filename': None
            })

    return images


def download_image_curl(url: str, filepath: Path, max_retries: int = 3) -> bool:
    """Download using curl with retries."""
    import time

    for attempt in range(max_retries):
        if attempt > 0:
            wait_time = 15 * attempt  # Exponential backoff
            print(f"    Retry {attempt + 1}/{max_retries} after {wait_time}s...")
            time.sleep(wait_time)

        try:
            result = subprocess.run([
                'curl', '-s', '-L', '-f',
                '-A', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                '-H', 'Accept: image/webp,image/apng,image/*,*/*;q=0.8',
                '-o', str(filepath),
                url
            ], capture_output=True, timeout=60)

            if result.returncode == 0 and filepath.exists() and filepath.stat().st_size > 1000:
                return True
        except Exception as e:
            print(f"    curl error: {e}")

    return False


def download_image(url: str, save_dir: Path, index: int) -> Path:
    """Download an image and convert SVG to PNG if needed."""
    import time

    # Determine file extension from URL
    if '.svg' in url.lower():
        ext = '.svg'
    elif '.png' in url.lower():
        ext = '.png'
    elif '.jpg' in url.lower() or '.jpeg' in url.lower():
        ext = '.jpg'
    else:
        ext = '.png'  # Default

    filename = f"figure_0_{index}{ext}"
    filepath = save_dir / filename

    print(f"  Downloading: {url[:70]}...")

    # Add significant delay to avoid rate limiting (Wikimedia enforces this)
    time.sleep(5)

    try:
        # Use curl for more reliable downloads
        if not download_image_curl(url, filepath):
            raise Exception("Download failed after retries")

        # Convert SVG to PNG if needed (Word doesn't support SVG well)
        if ext == '.svg':
            png_path = save_dir / f"figure_0_{index}.png"
            if convert_svg_to_png(filepath, png_path):
                os.remove(filepath)
                return png_path
            else:
                # Return SVG path if conversion fails (will show placeholder in Word)
                return filepath

        return filepath

    except Exception as e:
        print(f"    Error downloading: {e}")
        return None


def convert_svg_to_png(svg_path: Path, png_path: Path) -> bool:
    """Convert SVG to PNG using available tools."""
    # Try cairosvg
    try:
        import cairosvg
        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=800)
        return True
    except ImportError:
        pass
    except Exception as e:
        print(f"    cairosvg conversion failed: {e}")

    # Try inkscape
    try:
        result = subprocess.run(
            ['inkscape', str(svg_path), '--export-type=png', f'--export-filename={png_path}', '-w', '800'],
            capture_output=True, timeout=30
        )
        if result.returncode == 0 and png_path.exists():
            return True
    except:
        pass

    # Try rsvg-convert
    try:
        result = subprocess.run(
            ['rsvg-convert', '-w', '800', '-o', str(png_path), str(svg_path)],
            capture_output=True, timeout=30
        )
        if result.returncode == 0 and png_path.exists():
            return True
    except:
        pass

    # Try ImageMagick convert
    try:
        result = subprocess.run(
            ['convert', '-density', '150', str(svg_path), str(png_path)],
            capture_output=True, timeout=30
        )
        if result.returncode == 0 and png_path.exists():
            return True
    except:
        pass

    return False


def resize_image_if_needed(img_path: Path, max_width: int = 800) -> Path:
    """Resize image if it's too large."""
    try:
        with Image.open(img_path) as img:
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img_resized = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

                # Save as PNG to preserve quality
                new_path = img_path.with_suffix('.png')
                img_resized.save(new_path, 'PNG')
                if new_path != img_path:
                    os.remove(img_path)
                return new_path
    except Exception as e:
        print(f"    Could not resize: {e}")

    return img_path


def create_word_document(md_file: Path, images: list, output_path: Path):
    """Create Word document from markdown with embedded images."""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    doc = Document()

    # Set default font
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(11)

    # Track which image we're on
    image_index = 0
    in_references = False

    # Process markdown line by line
    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Chapter title (# Chapter 0)
        if line.startswith('# ') and not line.startswith('## '):
            p = doc.add_heading(line[2:].strip(), level=0)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Section heading (## ...)
        elif line.startswith('## '):
            text = line[3:].strip()
            if 'References' in text:
                in_references = True
            p = doc.add_heading(text, level=1)
            if 'Foundations' in text:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # Subheading (### ...)
        elif line.startswith('### '):
            doc.add_heading(line[4:].strip(), level=2)

        # Horizontal rule
        elif line.strip() == '---':
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run('─' * 40)

        # Epigraph/quote (italic text)
        elif line.startswith('*"') or (line.startswith('*') and '—' in line):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            text = line.strip().strip('*')
            run = p.add_run(text)
            run.italic = True

        # Image
        elif line.startswith('!['):
            match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', line)
            if match and image_index < len(images):
                img_info = images[image_index]
                local_path = img_info.get('local_path')

                if local_path and Path(local_path).exists():
                    try:
                        # Check if it's an SVG (not supported by python-docx)
                        if str(local_path).lower().endswith('.svg'):
                            p = doc.add_paragraph()
                            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                            run = p.add_run(f"[Figure 0.{image_index + 1}: {img_info['alt'][:50]}...]")
                            run.italic = True
                        else:
                            p = doc.add_paragraph()
                            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                            run = p.add_run()
                            run.add_picture(str(local_path), width=Inches(IMAGE_WIDTH))
                    except Exception as e:
                        p = doc.add_paragraph()
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        run = p.add_run(f"[Image could not be embedded: {str(e)[:50]}]")
                        run.italic = True
                else:
                    p = doc.add_paragraph()
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    run = p.add_run(f"[Figure 0.{image_index + 1}: {img_info['alt'][:50]}]")
                    run.italic = True

                image_index += 1

        # Image source line
        elif line.startswith('*Source:'):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            text = line.strip().strip('*')
            run = p.add_run(text)
            run.italic = True
            run.font.size = Pt(9)

        # Figure caption (bold markers)
        elif line.startswith('**Figure') or '**Figure' in line:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            text = re.sub(r'\*\*', '', line)  # Remove bold markers
            run = p.add_run(text)
            run.italic = True
            run.font.size = Pt(10)

        # Table
        elif line.startswith('|'):
            # Collect all table lines
            table_lines = [line]
            i += 1
            while i < len(lines) and lines[i].startswith('|'):
                table_lines.append(lines[i])
                i += 1
            i -= 1  # Back up since we'll increment at end of loop

            # Parse table
            if len(table_lines) >= 2:
                # First line is header
                headers = [cell.strip() for cell in table_lines[0].split('|')[1:-1]]
                # Skip separator line (line with dashes)
                data_start = 2 if len(table_lines) > 2 and '---' in table_lines[1] else 1
                data_lines = table_lines[data_start:]

                if headers:
                    table = doc.add_table(rows=1, cols=len(headers))
                    table.style = 'Table Grid'

                    # Header row
                    header_cells = table.rows[0].cells
                    for j, header in enumerate(headers):
                        header_cells[j].text = header
                        for run in header_cells[j].paragraphs[0].runs:
                            run.bold = True

                    # Data rows
                    for data_line in data_lines:
                        if '---' in data_line:
                            continue
                        cells = [cell.strip() for cell in data_line.split('|')[1:-1]]
                        row = table.add_row()
                        for j, cell_text in enumerate(cells):
                            if j < len(row.cells):
                                # Clean up markdown formatting
                                cell_text = re.sub(r'\*\*([^*]+)\*\*', r'\1', cell_text)
                                row.cells[j].text = cell_text

                    doc.add_paragraph()  # Space after table

        # Numbered list in references
        elif in_references and re.match(r'^\d+\.', line.strip()):
            p = doc.add_paragraph(line.strip(), style='List Number')
            p.paragraph_format.left_indent = Inches(0.25)

        # Bullet points
        elif line.strip().startswith('- '):
            text = line.strip()[2:]
            # Clean markdown formatting
            text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
            text = re.sub(r'\*([^*]+)\*', r'\1', text)
            p = doc.add_paragraph(text, style='List Bullet')

        # Regular paragraph
        elif line.strip():
            text = line.strip()
            # Clean markdown formatting for display
            text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # Bold -> plain
            text = re.sub(r'\*([^*]+)\*', r'\1', text)  # Italic -> plain

            p = doc.add_paragraph(text)

        i += 1

    # Save document
    doc.save(output_path)
    print(f"\nWord document saved: {output_path}")
    return True


def convert_to_pdf(docx_path: Path, pdf_path: Path):
    """Convert Word document to PDF using available tools."""
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    # Try LibreOffice
    try:
        result = subprocess.run(
            ['libreoffice', '--headless', '--convert-to', 'pdf', '--outdir',
             str(pdf_path.parent), str(docx_path)],
            capture_output=True, timeout=120
        )
        if result.returncode == 0:
            # LibreOffice names the file based on input name
            created_pdf = pdf_path.parent / docx_path.with_suffix('.pdf').name
            if created_pdf.exists():
                if created_pdf != pdf_path:
                    created_pdf.rename(pdf_path)
                print(f"PDF saved: {pdf_path}")
                return True
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"LibreOffice conversion failed: {e}")

    # Try unoconv
    try:
        result = subprocess.run(
            ['unoconv', '-f', 'pdf', '-o', str(pdf_path), str(docx_path)],
            capture_output=True, timeout=120
        )
        if result.returncode == 0 and pdf_path.exists():
            print(f"PDF saved: {pdf_path}")
            return True
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"unoconv conversion failed: {e}")

    print("\nNote: PDF conversion requires LibreOffice or unoconv.")
    print("Please convert the Word document to PDF manually, or install LibreOffice:")
    print("  sudo apt install libreoffice")
    return False


def check_existing_images(images: list, images_dir: Path) -> int:
    """Check for already downloaded images."""
    found = 0
    for i, img in enumerate(images):
        # Check for various possible filenames
        for ext in ['.png', '.jpg', '.jpeg', '.svg']:
            potential_path = images_dir / f"figure_0_{i + 1}{ext}"
            if potential_path.exists() and potential_path.stat().st_size > 1000:
                img['local_path'] = potential_path
                found += 1
                break
    return found


def save_url_list(images: list, output_path: Path):
    """Save a list of URLs for manual download."""
    with open(output_path, 'w') as f:
        f.write("# Chapter 0 Image URLs\n")
        f.write("# Download these manually from a web browser if automatic download fails.\n")
        f.write("# Save them to the 'images' folder with the suggested filenames.\n\n")
        for i, img in enumerate(images):
            f.write(f"# Figure 0.{i + 1}: {img['alt']}\n")
            f.write(f"# Save as: figure_0_{i + 1}.png\n")
            f.write(f"{img['url']}\n\n")
    print(f"   URL list saved to: {output_path}")


def main():
    print("=" * 60)
    print("Chapter 0 Image Embedder")
    print("=" * 60)

    # Check markdown file exists
    if not MARKDOWN_FILE.exists():
        print(f"Error: Markdown file not found: {MARKDOWN_FILE}")
        sys.exit(1)

    # Create images directory
    IMAGES_DIR.mkdir(exist_ok=True)

    # Extract image URLs
    print(f"\n1. Extracting images from {MARKDOWN_FILE.name}...")
    images = extract_images_from_markdown(MARKDOWN_FILE)
    print(f"   Found {len(images)} images")

    # Check for existing images first
    print(f"\n2. Checking for existing images in {IMAGES_DIR}/...")
    existing = check_existing_images(images, IMAGES_DIR)
    if existing > 0:
        print(f"   Found {existing} existing images")

    # Download missing images
    missing = [img for img in images if not img.get('local_path')]
    if missing:
        print(f"\n3. Downloading {len(missing)} missing images...")
        for i, img in enumerate(images):
            if img.get('local_path'):
                print(f"   ✓ Already have: figure_0_{i + 1}")
                continue

            local_path = download_image(img['url'], IMAGES_DIR, i + 1)
            if local_path:
                # Resize if too large
                local_path = resize_image_if_needed(local_path)
                img['local_path'] = local_path
                print(f"   ✓ Saved: {local_path.name}")
            else:
                img['local_path'] = None
                print(f"   ✗ Failed: {img['alt'][:40]}...")
    else:
        print(f"\n3. All images already downloaded!")

    # Count successful downloads
    successful = sum(1 for img in images if img.get('local_path'))
    print(f"\n   Have {successful}/{len(images)} images")

    # If some images failed, save URL list for manual download
    if successful < len(images):
        print(f"\n   Some images could not be downloaded (Wikimedia rate limiting).")
        save_url_list(images, IMAGES_DIR / "image_urls.txt")
        print(f"   You can download them manually from a browser and re-run this script.")

    # Create Word document
    print(f"\n4. Creating Word document...")
    if create_word_document(MARKDOWN_FILE, images, OUTPUT_DOCX):
        print(f"   ✓ Word document created")

    # Convert to PDF
    print(f"\n5. Converting to PDF...")
    convert_to_pdf(OUTPUT_DOCX, OUTPUT_PDF)

    print("\n" + "=" * 60)
    print("Output files:")
    print(f"  Word: {OUTPUT_DOCX}")
    if OUTPUT_PDF.exists():
        print(f"  PDF:  {OUTPUT_PDF}")
    print("=" * 60)


if __name__ == "__main__":
    main()
