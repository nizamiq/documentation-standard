---
title: Unified Documentation Standard (UDS)
description: "The canonical documentation standard for all NizamIQ repositories."
last_audited: "2026-02-20"
tags: ["documentation", "governance", "standard"]
---

# The NizamIQ Unified Documentation Standard (UDS)

**VERSION:** 1.0.0
**STATUS:** DRAFT

## 1. Overview

This document defines the single, canonical documentation standard for all repositories within the NizamIQ ecosystem. The UDS is designed to be **machine-first**, ensuring that all documentation is structured, predictable, and reliably parsable by AI agents. This standard unifies the competing conventions of `nizamiq-methodology` and `nizamiq-strategy` into a single, cohesive system.

## 2. Core Principles

1.  **Machine Readability:** All metadata MUST be in a structured, parsable format (YAML frontmatter).
2.  **Single Source of Truth:** This repository is the sole authority for all documentation standards.
3.  **Automated Governance:** Compliance is not optional and will be enforced by automated CI checks.
4.  **Agent-Centric Entry Points:** Repositories MUST provide a `CONTEXT.md` file as a clear, concise entry point for AI agents.

## 3. Mandatory File Structure

Every NizamIQ repository **MUST** contain the following directory structure and files. Missing files or directories will result in a CI failure.

```
/
├── docs/
│   ├── architecture/     # High-level system design, data flow, component diagrams
│   ├── api/              # API contracts, interface definitions (e.g., OpenAPI specs)
│   └── governance/       # AI agent instructions, CI/CD standards, this UDS
├── CONTEXT.md            # Root-level AI agent entry point
└── README.md             # Root-level human-readable entry point
```

## 4. Metadata Standard: YAML Frontmatter

Every Markdown file (`.md`) inside the `docs/` directory **MUST** begin with a YAML frontmatter block. This block is the single source of truth for all document metadata.

### 4.1. Required Fields

The following fields are mandatory for all documents. Missing or invalid fields will fail the `doc-lint` CI check.

| Field | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `id` | `string` | A unique, kebab-case identifier for the document. | `my-cool-document-v1` |
| `title` | `string` | The human-readable title of the document. | "My Cool Document" |
| `description` | `string` | A one-sentence summary of the document's purpose. | "This document outlines the architecture for the cool service." |
| `tags` | `array` | A list of relevant keywords for search and discovery. | `[architecture, design, service]` |
| `status` | `string` | The current state of the document. Must be one of: `DRAFT`, `IN_REVIEW`, `STABLE`, `DEPRECATED`. | `DRAFT` |
| `last_audited` | `string` | The date of the last time the document was verified against its source. Format: `YYYY-MM-DD`. | `2026-02-20` |
| `authoritative_source` | `string` | The path to the code or system this document describes. Use `NA` for non-specific docs. | `src/services/cool/index.ts` |
| `version` | `string` | The semantic version of the document (MAJOR.MINOR.PATCH). | `1.0.0` |

### 4.2. Example Frontmatter

```yaml
---
id: uds-spec-v1
title: "The NizamIQ Unified Documentation Standard (UDS)"
description: "The single, canonical documentation standard for all NizamIQ repositories."
tags: [standard, governance, documentation]
status: DRAFT
last_audited: 2026-02-20
authoritative_source: NA
version: 1.0.0
---
```

## 5. Versioning and Changelogs

To ensure a clear history of changes, every document **MUST** be versioned.

1.  **Semantic Versioning:** All documents must follow the `MAJOR.MINOR.PATCH` versioning scheme.
    -   **MAJOR:** Breaking changes to the standard or a complete rewrite.
    -   **MINOR:** Substantial new sections or non-breaking additions.
    -   **PATCH:** Minor corrections, clarifications, or typo fixes.
2.  **Changelog:** Every document **MUST** have a corresponding `CHANGELOG.md` file in the same directory, or reference a single root `CHANGELOG.md`. This file will track all version changes.

## 6. The `CONTEXT.md` File

This file is the primary entry point for AI agents. It provides a high-level, token-efficient summary of the repository. It **MUST** contain the following sections:

-   **System Architecture:** A brief, one-paragraph description of the project's purpose and core components.
-   **Dependency Map:** A list of the critical frameworks and libraries used (e.g., React, Go, Docker).
-   **Execution Commands:** The exact CLI commands required to build, test, and run the project.
-   **CI/CD Pipeline:** A summary of the Golden Pipeline gates and a link to the workflow file.

## 7. Automated Enforcement

Compliance with the UDS will be enforced by a `doc-lint` CI job. This job will:

1.  Verify the presence of all mandatory files and directories.
2.  Validate the YAML frontmatter of all `.md` files in `docs/` against the official [JSON Schema](./../schema/frontmatter.schema.json).
3.  Fail any pull request that introduces a violation.
