#!/bin/bash
#
# Agent Governance Inheritance Protocol (AGIP) - Bootstrap v1.0.0
#

set -e # Exit immediately if a command exits with a non-zero status.

# 1. Define Governance Source and Target
GOVERNANCE_REPO="https://github.com/nizamiq/documentation-standard.git"
GOVERNANCE_SRC="/tmp/documentation-standard"
AGENT_GOVERNANCE_TARGET="/home/ubuntu/governance"

# 2. Clone the Standard
echo "[AGIP] Cloning the canonical governance standard..."
git clone "$GOVERNANCE_REPO" "$GOVERNANCE_SRC"

# 3. Inject the Standard
echo "[AGIP] Injecting governance standards into agent workspace..."
mkdir -p "$AGENT_GOVERNANCE_TARGET"
cp -r "$GOVERNANCE_SRC/standard" "$AGENT_GOVERNANCE_TARGET/"
cp -r "$GOVERNANCE_SRC/templates" "$AGENT_GOVERNANCE_TARGET/"
cp -r "$GOVERNANCE_SRC/schema" "$AGENT_GOVERNANCE_TARGET/"

# 4. Verify the Standard
echo "[AGIP] Verifying governance injection..."
if [ -f "$AGENT_GOVERNANCE_TARGET/standard/UDS.md" ] && [ -f "$AGENT_GOVERNANCE_TARGET/templates/governance/AI_AGENT_INSTRUCTIONS.md" ]; then
    echo "[AGIP] Verification successful. Agent is now bound by NizamIQ ecosystem governance."
else
    echo "[AGIP] VERIFICATION FAILED. Governance injection incomplete. Halting agent activation."
    exit 1
fi

# 5. Cleanup
rm -rf "$GOVERNANCE_SRC"

echo "[AGIP] Bootstrap complete."
exit 0
exit 0
