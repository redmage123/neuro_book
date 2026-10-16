# System Patterns

## Document Organization
```
docs/
├── book/           # Main textbook
│   ├── Word/       # Publisher/editorial workflow
│   │   ├── Frontispiece/
│   │   ├── Chapter1/
│   │   ├── Chapter2/
│   │   └── Chapter3/
│   └── pdf/        # Print-ready, review-ready
│       ├── frontispiece/
│       ├── Chapter1/
│       ├── Chapter2/
│       └── Chapter3/
└── companion/      # Student notes & labs
    └── Chapter1/
        ├── Word/
        └── pdf/
```

## Naming Conventions
- Main book: `How_the_Brain_Learns_Chapter_N_[descriptor].{docx,pdf}`
- Companion: `How_the_Brain_Learns_Chapter_N_Student_Notes_and_Labs.{docx,pdf}`
- Versioning: `_v1`, `_v2` suffix when multiple versions exist
- Descriptors: `FULL`, `with_Images`, `AUTHORITATIVE`, `STYLED`

## Writing Patterns
1. **Chapter structure**: Cumulative — each builds on previous
2. **Explanation levels**: Molecular → Cellular → Circuit → Cognitive (kept distinct)
3. **Constraints first**: Introduce biological limitations before describing solutions
4. **No hand-waving**: Every mechanism explained physically

## Editorial Workflow
1. Draft in Word for collaboration
2. Generate PDF for review and archival
3. Chapters reviewed independently
4. Style sheet compliance checked before finalization

## Key Technical Decisions
- Parallel Word/PDF outputs (not derived from single source)
- Chapter-per-directory structure
- No build tooling dependency — manual artifact management
- Companion volume is complementary, not simplified
