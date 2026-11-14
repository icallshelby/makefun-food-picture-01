#!/usr/bin/env python3
"""food-picture-01 entry (Python 3.13, standard library only).

Copies entry.png to $MAKEFUN_OUTPUT_DIR/entry.png (default /output)
using a verify_copy helper that asserts size limits, verifies PNG signature,
and checks byte-for-byte identity.
Deterministic, no network, no randomness, no clock.
"""
import hashlib
import os
import shutil
import sys


def verify_copy(src_path, dest_path):
    dest_size = os.path.getsize(dest_path)

    # Gate assertion: check output is at most 1 MiB (1048576 bytes)
    if dest_size > 1048576:
        print(f"Error: output size {dest_size} exceeds 1 MiB limit (1048576 bytes)", file=sys.stderr)
        sys.exit(1)

    # Post-write verification: compare byte-for-byte and compute sha256
    with open(src_path, "rb") as f_src, open(dest_path, "rb") as f_dest:
        src_bytes = f_src.read()
        dest_bytes = f_dest.read()

    # PNG signature check (8-byte PNG header)
    png_sig = bytes([137, 80, 78, 71, 13, 10, 26, 10])
    if not dest_bytes.startswith(png_sig):
        print("Error: output file does not start with valid PNG signature", file=sys.stderr)
        sys.exit(1)

    if src_bytes != dest_bytes:
        print("Error: destination file does not match source byte-for-byte!", file=sys.stderr)
        sys.exit(1)

    sha256 = hashlib.sha256(dest_bytes).hexdigest()

    print(f"Output path: {dest_path}")
    print(f"Byte count: {dest_size}")
    print(f"SHA256: {sha256}")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(script_dir, "entry.png")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    dest_path = os.path.join(output_dir, "entry.png")

    shutil.copyfile(src_path, dest_path)
    verify_copy(src_path, dest_path)


if __name__ == "__main__":
    main()
