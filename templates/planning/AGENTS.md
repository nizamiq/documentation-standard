---id: agents_memory
title: Agent Context & State
description: Active memory file for AI agent session continuity
last_audited: '2026-02-20'
authoritative_source: null
status: DRAFT
---
# Agent Context & State

## Current Session

**Current Objective:** "..."

**Active Phase:** ...

**Lead Role:** ...

## Protocols (Strictly Enforced)

1.  **State Block First:** Every response must begin with `[STATE: Phase X | STEP: Y | DEPS: Z]`.
2.  **Verify Before Proceeding:** Do not mark steps as complete without providing terminal output or file read verification in the `proof_of_work` field.
3.  **Update Manifest:** Update `manifest.json` whenever a phase is completed.
4.  **Debt-Driven Development:** Before starting a new phase, review `./docs/planning/DEBT.md` and prioritize resolving any assigned debt items within the current phase's scope.
