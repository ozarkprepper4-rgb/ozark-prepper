#!/bin/bash
exec ssh -i "$HOME/.ssh/destiny_omarchy_ed25519" -o BatchMode=yes -p 2222 destiny@127.0.0.1 "$@"
