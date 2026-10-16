#!/bin/bash
# Download Chapter 0 images from Wikimedia Commons
# Run this script manually if the Python script can't download due to rate limiting

IMAGES_DIR="$(dirname "$0")/images"
mkdir -p "$IMAGES_DIR"

echo "Downloading Chapter 0 images..."
echo "If you get 429 errors, wait a few minutes and try again."
echo ""

# Use wget with delay between downloads
download_with_retry() {
    local url="$1"
    local output="$2"
    local max_retries=5

    for i in $(seq 1 $max_retries); do
        echo "  Downloading: $(basename "$output")..."
        if wget -q --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
                -O "$output" "$url" 2>/dev/null; then
            # Check if file is valid (not error page)
            if [ -s "$output" ] && [ $(stat -c%s "$output") -gt 5000 ]; then
                echo "    ✓ Success"
                return 0
            fi
        fi
        echo "    Retry $i/$max_retries - waiting 30 seconds..."
        sleep 30
    done
    echo "    ✗ Failed"
    return 1
}

# Figure 0.1 - Animal Cell
download_with_retry \
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Animal_cell_structure_en.svg/800px-Animal_cell_structure_en.svg.png" \
    "$IMAGES_DIR/figure_0_1.png"

sleep 10

# Figure 0.2 - Catabolism
download_with_retry \
    "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Catabolism_schematic.svg/600px-Catabolism_schematic.svg.png" \
    "$IMAGES_DIR/figure_0_2.png"

sleep 10

# Figure 0.3 - Sodium Potassium Pump
download_with_retry \
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Sodium-potassium_pump_and_diffusion.svg/800px-Sodium-potassium_pump_and_diffusion.svg.png" \
    "$IMAGES_DIR/figure_0_3.png"

sleep 10

# Figure 0.4 - Chemical Bonds
download_with_retry \
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Ionic_covalent_metallic_bonds.svg/800px-Ionic_covalent_metallic_bonds.svg.png" \
    "$IMAGES_DIR/figure_0_4.png"

sleep 10

# Figure 0.5 - Biological Macromolecules
download_with_retry \
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Biological_macromolecules.svg/800px-Biological_macromolecules.svg.png" \
    "$IMAGES_DIR/figure_0_5.png"

sleep 10

# Figure 0.6 - Hooke's Cork (JPG)
download_with_retry \
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Hooke-cork.jpg/800px-Hooke-cork.jpg" \
    "$IMAGES_DIR/figure_0_6.jpg"

sleep 10

# Figure 0.7 - Action Potential
download_with_retry \
    "https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Action_potential.svg/800px-Action_potential.svg.png" \
    "$IMAGES_DIR/figure_0_7.png"

sleep 10

# Figure 0.8 - Human Embryogenesis
download_with_retry \
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/HumanEmbryogenesis.svg/800px-HumanEmbryogenesis.svg.png" \
    "$IMAGES_DIR/figure_0_8.png"

sleep 10

# Figure 0.9 - Neural Crest
download_with_retry \
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Neural_crest.svg/800px-Neural_crest.svg.png" \
    "$IMAGES_DIR/figure_0_9.png"

echo ""
echo "Done! Check $IMAGES_DIR for downloaded images."
echo ""
echo "After downloading, run: python3 embed_images.py"
