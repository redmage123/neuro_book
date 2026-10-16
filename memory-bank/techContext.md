# Tech Context

## Document Formats
- **Microsoft Word (.docx)**: Primary authoring and editorial format
- **PDF**: Print-ready and review artifacts
- Markdown is the master format since 2026-10-16; Word and PDF are built from it (pandoc + LibreOffice via docs/build.py)

## Tools & Dependencies
- Word processor for authoring
- PDF generator (Word export or dedicated tool)
- Git for version control

## MCP Servers (Claude Code Integration)
| Server | Purpose |
|--------|---------|
| zotero | Citation management, bibliography |
| semantic-scholar | Academic paper search |
| pubmed | Biomedical literature access |
| arxiv | Preprint discovery |
| pandoc | Document format conversion |
| mermaid | Diagrams (neural pathways, flowcharts) |
| cite-assist | BibTeX citation generation |
| filesystem | File management |

## Repository Structure
```
neuro_book/
├── docs/
│   ├── book/       # Main textbook (Word + PDF)
│   └── companion/  # Student materials (Word + PDF)
├── memory-bank/    # Project context for AI assistance
└── README.md       # Project overview and philosophy
```

## Development Setup
- No build system required
- Documents edited directly in Word
- PDFs generated manually per chapter
- Git tracks all artifacts

## Constraints
- No crowdsourced contributions (curated authorship)
- Copyright reserved until license finalized
- Style sheet compliance required for all content
