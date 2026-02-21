---
id: doc-std-agents-memory
title: Agent Context & State
description: Active memory file for AI agent session continuity in the documentation-standard repository
last_audited: "2026-02-20"
authoritative_source: docs/planning
status: DRAFT
version: 1.0.0
tags: ["planning", "agent", "context", "documentation-standard"]
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
> **Active in-scope repositories:** `nizamiq-strategy`, `nizamiq.com`, `nizamiq-methodology`, `anchorlink`, `meridian`, `Fireside`, `Cornerstone`, `KubeClaw`, `Recce`, `Atlas`, `Aegis`, `gateway-config`, `documentation-standard`, `zitadel-config`
>
> **Incubating repositories (governance setup only, no phase execution without operator authorization):** `autonomous-product-studio`, `Axiom`
>
> **Reference only (read-only, no modifications):** `nizamiq-website`, `meridian-prime`
>
> **Explicitly out of scope:** `sputnik-gateway` and any repository not listed above.

---



**Current Objective:** Execute Phase 1 of the Documentation Unification Plan — define and publish the Unified Documentation Standard (UDS).

**Active Phase:** Phase 01 (UDS_Definition_and_Publication)

**Lead Role:** Principal Documentation Architect

## Protocols (Strictly Enforced)

1.  **State Block First:** Every response must begin with `[STATE: Phase X | STEP: Y | DEPS: Z]`.
2.  **Verify Before Proceeding:** Do not mark steps as complete without providing terminal output or file read verification in the `proof_of_work` field.
3.  **Update Manifest:** Update `manifest.json` whenever a phase is completed.
4.  **Debt-Driven Development:** Before starting a new phase, review `./docs/planning/DEBT.md` and prioritize resolving any assigned debt items within the current phase's scope.
