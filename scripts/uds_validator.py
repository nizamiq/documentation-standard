#!/usr/bin/env python3
"""
UDS Validator for doc-lint CI job.

Checks for:
1.  File existence (CONTEXT.md, AI_AGENT_INSTRUCTIONS.md, etc.)
2.  Directory existence (docs/architecture, docs/api, docs/governance)
3.  Frontmatter schema compliance for all changed .md files.

The schema is embedded to avoid external file dependencies in consuming repos.
"""
import os, json, re, sys

# --- Embedded UDS Frontmatter Schema ---
# Required fields per the Unified Documentation Standard v1.0
REQUIRED_FRONTMATTER_FIELDS = ["id", "title", "last_audited", "status", "authoritative_source"]
VALID_STATUSES = {"STABLE", "DRAFT", "DEPRECATED", "ACTIVE", "ARCHIVED"}

def check_file_exists(path, errors):
    if not os.path.exists(path):
        errors.append(f"Missing required file: {path}")

def check_dir_exists(path, errors):
    if not os.path.isdir(path):
        errors.append(f"Missing required directory: {path}")

def parse_frontmatter(content):
    if not content.startswith("---"):
        return None
    end = content.find("\n---", 3)
    if end == -1:
        return None
    fm_text = content[4:end].strip()
    fm = {}
    for line in fm_text.split("\n"):
        if ":" in line and not line.startswith(" ") and not line.startswith("-"):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm

def validate_frontmatter(fpath, errors):
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        errors.append(f"{fpath}: Could not read file")
        return

    fm = parse_frontmatter(content)
    if not fm:
        errors.append(f"{fpath}: Missing or malformed YAML frontmatter block.")
        return

    # Check required fields
    for field in REQUIRED_FRONTMATTER_FIELDS:
        if field not in fm or not fm[field]:
            errors.append(f"{fpath}: Missing required frontmatter field: '{field}'")

    # Check status is valid
    if "status" in fm and fm["status"] and fm["status"] not in VALID_STATUSES:
        errors.append(f"{fpath}: Invalid status '{fm['status']}'. Must be one of: {', '.join(sorted(VALID_STATUSES))}")

# --- Main ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python uds_validator.py <path_to_changed_files.txt>")
        sys.exit(1)

    changed_files_path = sys.argv[1]
    repo_root = os.getcwd()
    errors = []

    # 1. Check for required files/dirs (run on every PR)
    check_file_exists(os.path.join(repo_root, "CONTEXT.md"), errors)
    check_dir_exists(os.path.join(repo_root, "docs/architecture"), errors)
    check_dir_exists(os.path.join(repo_root, "docs/api"), errors)
    check_dir_exists(os.path.join(repo_root, "docs/governance"), errors)
    check_file_exists(os.path.join(repo_root, "docs/governance/AI_AGENT_INSTRUCTIONS.md"), errors)

    # 2. Validate frontmatter of changed markdown files
    try:
        with open(changed_files_path, "r") as f:
            changed_files = [line.strip() for line in f if line.strip().endswith(".md")]
    except Exception as e:
        print(f"Warning: Could not read changed files list: {e}")
        changed_files = []

    for rel_path in changed_files:
        full_path = os.path.join(repo_root, rel_path)
        if os.path.exists(full_path):
            validate_frontmatter(full_path, errors)

    # 3. Report results
    if errors:
        print("\nUDS Compliance Check FAILED:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)
    else:
        print("UDS Compliance Check PASSED.")
        sys.exit(0)
