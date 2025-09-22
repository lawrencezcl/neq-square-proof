#!/usr/bin/env bash
set -euo pipefail
# Deploy the generated Cairo verifier to Starknet testnet.
# Requirements: starknet CLI (https://www.cairo-lang.org/docs/hello_starknet/starknet_cli)
# Environment vars:
#   STARKNET_NETWORK   e.g., 'alpha-goerli' or your configured network
#   ACCOUNT_ADDRESS, PRIVATE_KEY (if using account deploy flow)
#
# Example (simple deploy using starknet CLI):
# starknet deploy --contract starknet/verifier.cairo --network $STARKNET_NETWORK
#
echo "Deploy the verifier using the Starknet CLI, e.g.:"
echo "  starknet deploy --contract starknet/verifier.cairo --network alpha-goerli"
