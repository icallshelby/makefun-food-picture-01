# Fine Dining Fish — food-picture-01

Fine-dining plated dish: a seared fish fillet on green pea puree with baby carrots, radish slices, edible flowers and black tuile crisps on a dark plate, candlelit restaurant table, steam rising.

This repository is a make.fun entry for competition `food-picture-01`.
The program `main.py` copies the user's fine-dining fish photo (`entry.png`, 1024x572 PNG) to the designated output path as `entry.png`.

## How to Run

```bash
python3 main.py
```

You can customize the output directory by setting the `MAKEFUN_OUTPUT_DIR`
environment variable:

```bash
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

## Gate Limits & Specifications

- **Dimensions:** 1024x572 pixels (within the 1024x1024 maximum limit).
- **File Size:** 724,040 bytes (~707 KiB, well under the 1 MiB / 1,048,576 bytes gate limit).
- **Format:** PNG image.
- **Determinism:** 100% deterministic, byte-for-byte identical output across multiple runs.
- **Network / Clock / Randomness:** None (Python 3.13 standard library only).

## Verification Results

- **Output Path:** `/output/entry.png` (or custom `MAKEFUN_OUTPUT_DIR`)
- **Byte Count:** 724,040 bytes
- **SHA256 Hash:** `667684aa142002ce420e939d0bdf0974f1eb654f96b094fcc0c296ab180a43a7`
- **Determinism:** Verified byte-identical (`cmp` match) across independent runs.

## Revision Notes

- **verify_copy Helper:** Refactored verification logic into `verify_copy` handling gate assertion (<= 1 MiB), 8-byte PNG signature validation (`\x89PNG\r\n\x1a\n`), byte-for-byte source-to-destination comparison, SHA-256 calculation, and error exit handling.
- **Measured Verification Results:**
  - Dimensions: 1024x572 pixels
  - Byte Size: 724,040 bytes (<= 1,048,576 bytes)
  - SHA256: `667684aa142002ce420e939d0bdf0974f1eb654f96b094fcc0c296ab180a43a7`
  - Determinism: Verified byte-identical across multiple distinct output directory runs.
