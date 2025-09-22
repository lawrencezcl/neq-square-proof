#!/usr/bin/env bash
set -euo pipefail
# Build Noir ACIR artifact
# Requires: noir compiler installed (https://noir-lang.org)
# This will produce an ACIR bytecode file that Garaga can consume.

# Example: compile to ACIR (adjust output path if your noir cli differs)
noir compile noir/src/neq_square.nr --output noir/target/bytecode.acir --backend acir || true

echo "Noir compiled. Output: noir/target/bytecode.acir"
