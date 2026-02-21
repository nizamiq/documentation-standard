---
id: ecosystem-readmemd
title: "NizamIQ Unified Documentation Standard (UDS)"
description: "The canonical Unified Documentation Standard (UDS) for all NizamIQ repositories. Contains the official standard, templates, validation schema, and governance documents."
tags: ["documentation", "governance", "standard"]
status: STABLE
last_audited: "2026-02-20"
authoritative_source: "README.md"
version: 1.0.0
---
# NizamIQ Unified Documentation Standard (UDS)

**STATUS:** DRAFT

## 1. Purpose

This repository is the single source of truth for all documentation standards across the NizamIQ ecosystem. It provides the canonical **Unified Documentation Standard (UDS)**, a complete set of templates, validation schemas, and governance workflows required to create consistent, machine-readable, and agent-friendly documentation.

Adherence to this standard is **mandatory** for all NizamIQ repositories and will be enforced automatically via the "Golden Pipeline" CI/CD process.

## 2. The Standard

The complete specification for the UDS can be found in the core standard document:

**[./standard/UDS.md](./standard/UDS.md)**

This document details the mandatory file structures, metadata formats (YAML frontmatter), versioning schemes, and content requirements.

## 3. Templates

This repository contains official templates for all required documentation artifacts. Agents and developers **MUST** use these templates when creating new documentation.

- **[./templates/CONTEXT.md](./templates/CONTEXT.md):** The root-level entry point for AI agents.
- **[./templates/CHANGELOG.md](./templates/CHANGELOG.md):** The mandatory changelog for tracking document versions.
- **[./templates/planning/](./templates/planning/):** Templates for the NizamIQ Planning Framework (`AGENTS.md`, `manifest.json`, `phase.yaml`).

## 4. Governance & Enforcement

Compliance with the UDS is not optional. It is enforced through an automated `doc-lint` CI job that is part of the Golden Pipeline.

- **[./.github/workflows/doc-lint.yml](./.github/workflows/doc-lint.yml):** The reusable workflow for automated documentation validation.
- **[./schema/frontmatter.schema.json](./schema/frontmatter.schema.json):** The JSON schema used to validate the YAML frontmatter of all documents.
