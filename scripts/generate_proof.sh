#!/usr/bin/env bash
set -euo pipefail
# Generate a proof for the relation using your chosen proving/backend.
# The exact command depends on the proving backend (barretenberg, acir, etc.).
# This script is a template and must be edited per your prover toolchain.
# Example workflow (conceptual):
# 1) produce witness (private input w) and public inputs file (public.json)
# 2) call backend prover to produce proof.bin / proof.json

echo "Place your public inputs (x,y) into proofs/public.json and private witness w into proofs/witness.json"
echo "Then call your prover to generate proofs/example/proof.json"
echo "See README for exact commands depending on your prover."
