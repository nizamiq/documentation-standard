---
id: agents_memory
title: Agent Context & State
description: Active memory file for AI agent session continuity
last_audited: '2026-02-20'
authoritative_source: docs/planning/AGENTS.md
status: DRAFT
version: 2.0.0
tags: ["planning", "agent", "context"]
---

# Agent Context & State

---

## ⚠️ MANDATORY SCOPE CHECK — READ BEFORE ACTING

> **This repository is part of the NizamIQ ecosystem.**
>
> Before performing any work in any session, you **must** verify that the repository you are working on is listed as **in-scope** in the canonical ecosystem scope document:
>
> - **Human-readable:** [`nizamiq-strategy/SCOPE.md`](https://github.com/nizamiq/nizamiq-strategy/blob/main/SCOPE.md)
> - **Machine-readable:** [`nizamiq-strategy/ECOSYSTEM.json`](https://github.com/nizamiq/nizamiq-strategy/blob/main/ECOSYSTEM.json)
>
> **If a repository is not listed as `in_scope` or `incubating` in `ECOSYSTEM.json`, do not perform any work on it.** Treat it as out of scope by default.
>
> **Active in-scope repositories:** `nizamiq-strategy`, `nizamiq.com`, `nizamiq-methodology`, `anchorlink`, `meridian`, `Fireside`, `Cornerstone`, `KubeClaw`, `Recce`, `Atlas`, `Aegis`, `gateway-config`, `documentation-standard`
>
> **Incubating repositories (governance setup only, no phase execution without operator authorization):** `autonomous-product-studio`, `Axiom`
>
> **Reference only (read-only, no modifications):** `nizamiq-website`, `meridian-prime`
>
> **Explicitly out of scope:** `sputnik-gateway` and any repository not listed above.

---



## MANDATORY FIRST ACTION: AGIP Bootstrap

> **Before reading anything else, you must execute the Agent Governance Inheritance Protocol (AGIP) bootstrap.** This is non-negotiable.

```bash
#!/bin/bash
# AGIP Bootstrap v2.0.0
set -e
git clone "https://github.com/nizamiq/documentation-standard.git" /tmp/documentation-standard
mkdir -p /home/ubuntu/governance
cp -r /tmp/documentation-standard/standard /home/ubuntu/governance/
cp -r /tmp/documentation-standard/templates /home/ubuntu/governance/
cp -r /tmp/documentation-standard/schema /home/ubuntu/governance/
[ -f /home/ubuntu/governance/standard/UDS.md ] && echo "[AGIP] VERIFIED." || (echo "[AGIP] FAILED." && exit 1)
rm -rf /tmp/documentation-standard
```

After bootstrap, read `/home/ubuntu/governance/templates/governance/AI_AGENT_INSTRUCTIONS.md` for full operating instructions.

---

## Current Session

**Current Objective:** `[REPLACE WITH ACTIVE OBJECTIVE]`

**Active Phase:** `[REPLACE WITH ACTIVE PHASE ID AND NAME]`

**Lead Role:** `[REPLACE WITH AGENT ROLE]`

---

## Protocols (Strictly Enforced)

1.  **AGIP First:** Execute the AGIP bootstrap above before any other action.
2.  **State Block First:** Every response must begin with `[STATE: Phase X | STEP: Y | DEPS: Z]`.
3.  **Verify Before Proceeding:** Do not mark steps as complete without providing terminal output or file read verification in the `proof_of_work` field.
4.  **Update Manifest:** Update `manifest.json` whenever a phase is completed.
5.  **Debt-Driven Development:** Before starting a new phase, review `./docs/planning/DEBT.md` and prioritize resolving any assigned debt items within the current phase's scope.
6.  **UDS Compliance:** All documentation created or modified must comply with the Unified Documentation Standard. Run `doc-lint` locally before committing.
7.  **Agent Spawning:** If spawning child agents, pass the AGIP bootstrap as their first instruction. Governance inheritance is transitive.
