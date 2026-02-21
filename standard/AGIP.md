---
id: agent_governance_inheritance_protocol
title: Agent Governance Inheritance Protocol (AGIP)
description: The canonical protocol ensuring all spawned AI agents inherit and enforce the full NizamIQ ecosystem governance standards from birth.
tags: ["protocol", "governance", "agentic", "bootstrap"]
status: DRAFT
last_audited: "2026-02-20"
authoritative_source: standard/AGIP.md
version: 1.0.0
---

## 1. Core Directive

**An agent that does not inherit the standards of the ecosystem is a rogue agent.**

This protocol mandates that any AI agent, regardless of its origin point within the NizamIQ ecosystem, must automatically and verifiably inherit the complete set of governance standards defined in the `nizamiq/documentation-standard` repository. This is not an optional step; it is a fundamental, non-negotiable bootstrap requirement for agent activation.

## 2. The Inheritance Mechanism

The inheritance mechanism is triggered at the moment of agent creation or first activation. It consists of a single, atomic bootstrap script that performs the following actions:

1.  **Clone the Standard:** The agent must clone the `nizamiq/documentation-standard` repository into its local workspace.

    ```bash
    git clone https://github.com/nizamiq/documentation-standard.git /home/ubuntu/documentation-standard
    ```

2.  **Inject the Standard:** The agent must recursively copy the contents of the cloned repository's `/standard`, `/templates`, and `/schema` directories into its own root directory or a designated `/governance` directory.

3.  **Load the Standard:** The agent must read and load the `AI_AGENT_INSTRUCTIONS.md` and all other core governance documents into its context or system prompt, explicitly acknowledging and agreeing to be bound by their directives.

4.  **Verify the Standard:** The agent must run a self-check to confirm that the core governance files are present and accessible in its local environment. This can be a simple file existence check.

## 3. The AGIP Bootstrap Script

The following shell script is the canonical implementation of the AGIP. It must be embedded within the agent creation logic or called as the first step in any agent's lifecycle.

```bash
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
```

## 4. Enforcement

- **Agent Spawners:** Any service, agent, or process responsible for creating new agents **must** ensure this bootstrap sequence is the first operation performed by the new agent.
- **Agent Lifecycle:** The `doc-lint` CI job, which will be deployed ecosystem-wide, will serve as a secondary enforcement mechanism. It will fail any pull request that attempts to modify or remove the AGIP bootstrap call from agent creation workflows.

This protocol ensures that governance is not a feature to be added, but a fundamental property of existence for any agent operating within the NizamIQ ecosystem.
