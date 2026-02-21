---
id: doc-std-debt-log
title: Technical Debt Log
description: Log of known technical debt, deferred decisions, and open issues for the documentation-standard repository
last_audited: '2026-02-20'
authoritative_source: docs/planning
status: DRAFT
version: 1.0.0
tags: ["technical-debt", "planning"]
---

# Technical Debt Log

This file tracks all known technical debt, deferred decisions, and open issues for the `documentation-standard` repository.

| ID | Priority | Description | Phase Introduced | Assigned To | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| DEBT-001 | MEDIUM | The `doc-lint.yml` workflow requires the `tj-actions/changed-files` action. This should be pinned to a specific SHA for security. | Phase 01 | TBD | OPEN |
| DEBT-002 | LOW | The `last_audited` field in the JSON schema uses `format: date` which requires a validator that supports JSON Schema draft-07 date format. Consider adding a regex pattern as a fallback. | Phase 01 | TBD | OPEN |
