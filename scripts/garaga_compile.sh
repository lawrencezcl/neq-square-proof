#!/usr/bin/env bash
set -euo pipefail
# Run Garaga to compile the Noir ACIR into a Cairo verifier + artifacts.
# Requirements: garaga CLI installed and on PATH (see Garaga docs)
# Adjust garaga CLI args depending on your installed version.

GARAGA_CONFIG=garaga/garaga.toml
echo "Running Garaga with config ${GARAGA_CONFIG} ..."
# Example (pseudo-command; adjust for your garaga release):
garaga compile --config ${GARAGA_CONFIG}

echo "Garaga compile finished. Check directory: starknet/ for verifier.cairo"
