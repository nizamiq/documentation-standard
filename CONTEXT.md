---
id: ecosystem-contextmd
title: "CONTEXT.md"
description: "Provides context for the AI agent."
tags: ["documentation", "governance"]
status: STABLE
last_audited: "2026-02-20"
authoritative_source: "CONTEXT.md"
version: 1.0.0
---
# CONTEXT.md

**LAST UPDATED:** 2026-02-20

## 1. System Architecture

This repository (`documentation-standard`) is the single source of truth for all documentation standards across the NizamIQ ecosystem. It is a pure documentation and governance repository with no runtime components. It contains the canonical **Unified Documentation Standard (UDS)**, a complete set of templates, a JSON validation schema, and a reusable GitHub Actions workflow (`doc-lint`) for automated enforcement. It is the authoritative reference for all 13 NizamIQ repositories.

## 2. Dependency Map

- **Languages:** Markdown, YAML, JSON
- **Frameworks/Runtimes:** GitHub Actions
- **Key Libraries:** PyYAML, jsonschema (used by the `doc-lint` CI workflow)
- **Databases:** None
- **Cloud Services:** GitHub

## 3. Execution Commands

This is a documentation repository with no executable commands. Key entry points for navigation are:

| Action | Path |
| :--- | :--- |
| **Read the Standard** | [`./standard/UDS.md`](./standard/UDS.md) |
| **Use CONTEXT.md Template** | [`./templates/CONTEXT.md`](./templates/CONTEXT.md) |
| **Use Planning Templates** | [`./templates/planning/`](./templates/planning/) |
| **View Frontmatter Schema** | [`./schema/frontmatter.schema.json`](./schema/frontmatter.schema.json) |

## 4. CI/CD Pipeline

This repository uses the **NizamIQ Golden Pipeline** standard. The `doc-lint` workflow defined here is designed to be called as a reusable workflow from the Golden Pipeline in all other repositories.

| Gate | Name | Description |
| :--- | :--- | :--- |
| 1 | **Code Quality** | Linting and formatting checks. |
| 2 | **Verifiable Truth** | No tests applicable (documentation repo). |
| 3 | **AI Autonomous Review** | CodeRabbit and CodeX review all changes. |
| 4 | **Build & Security** | Trivy security scan. |

**Workflow File:** [`.github/workflows/doc-lint.yml`](./.github/workflows/doc-lint.yml)
