#!/usr/bin/env python3
"""
UDS Validator for doc-lint CI job.

Checks for:
1.  File existence (CONTEXT.md, CHANGELOG.md, etc.)
2.  Directory existence (docs/architecture, etc.)
3.  Frontmatter schema compliance for all changed .md files.
"""
import os, json, re, sys
from jsonschema import validate, ValidationError

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
            fm[k.strip()] = v.strip()
    return fm

def validate_frontmatter(fpath, schema, errors):
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

    try:
        validate(instance=fm, schema=schema)
    except ValidationError as e:
        errors.append(f"{fpath}: Frontmatter failed validation: {e.message} on property '{e.path[0] if e.path else ''}'")

# --- Main ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python uds_validator.py <path_to_changed_files.txt>")
        sys.exit(1)

    changed_files_path = sys.argv[1]
    repo_root = os.getcwd()
    errors = []

    # 1. Load Schema
    schema_path = os.path.join(repo_root, "governance/schema/frontmatter.schema.json")
    if not os.path.exists(schema_path):
        print(f"FATAL: Schema not found at {schema_path}")
        sys.exit(1)
    with open(schema_path, "r") as f:
        schema = json.load(f)

    # 2. Check for required files/dirs (run on every PR)
    check_file_exists(os.path.join(repo_root, "CONTEXT.md"), errors)
    check_dir_exists(os.path.join(repo_root, "docs/architecture"), errors)
    check_dir_exists(os.path.join(repo_root, "docs/api"), errors)
    check_dir_exists(os.path.join(repo_root, "docs/governance"), errors)
    check_file_exists(os.path.join(repo_root, "docs/governance/AI_AGENT_INSTRUCTIONS.md"), errors)

    # 3. Validate frontmatter of changed markdown files
    with open(changed_files_path, "r") as f:
        changed_files = [line.strip() for line in f if line.strip().endswith(".md")]

    for rel_path in changed_files:
        full_path = os.path.join(repo_root, rel_path)
        if os.path.exists(full_path):
            validate_frontmatter(full_path, schema, errors)

    # 4. Report results
    if errors:
        print("\nUDS Compliance Check FAILED:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)
    else:
        print("UDS Compliance Check PASSED.")
        sys.exit(0)
