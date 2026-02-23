#!/usr/bin/env python3
"""
UDS Frontmatter Pre-Commit Hook.
Validates staged .md files against the UDS schema before commit.
"""
import os, sys, json, subprocess

def get_staged_files():
    """Returns a list of staged .md files."""
    try:
        result = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"], capture_output=True, text=True, check=True)
        return [f for f in result.stdout.splitlines() if f.endswith(".md")]
    except subprocess.CalledProcessError as e:
        print(f"Error getting staged files: {e}", file=sys.stderr)
        return []

def validate_file(fpath, schema):
    """Validates a single file against the UDS schema."""
    errors = []
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return [f"{fpath}: Could not read file: {e}"]

    if not content.startswith("---"):
        return [f"{fpath}: Missing YAML frontmatter (must start with ---)"]

    end = content.find("\n---", 3)
    if end == -1:
        return [f"{fpath}: Frontmatter block not closed with ---"]

    try:
        import yaml
        from jsonschema import validate, ValidationError
        fm = yaml.safe_load(content[4:end])
        if not isinstance(fm, dict):
            return [f"{fpath}: Frontmatter is not a valid YAML mapping"]
        validate(instance=fm, schema=schema)
    except ImportError:
        print("Warning: PyYAML or jsonschema not installed. Skipping detailed validation.", file=sys.stderr)
    except yaml.YAMLError as e:
        return [f"{fpath}: Invalid YAML: {e}"]
    except ValidationError as e:
        field = e.path[0] if e.path else "root"
        return [f"{fpath}: Schema validation failed on field [1m{field}[0m: {e.message}"]
    except Exception as e:
        return [f"{fpath}: Unexpected error during validation: {e}"]

    return errors

def main():
    """Main function."""
    # Find schema file relative to script location
    script_dir = os.path.dirname(os.path.realpath(__file__))
    schema_path = os.path.abspath(os.path.join(script_dir, "../schema/frontmatter.schema.json"))
    if not os.path.exists(schema_path):
        print(f"Error: Schema file not found at {schema_path}", file=sys.stderr)
        sys.exit(1)

    with open(schema_path, "r") as f:
        schema = json.load(f)

    staged_files = get_staged_files()
    if not staged_files:
        print("No staged .md files to check.")
        sys.exit(0)

    all_errors = []
    for f in staged_files:
        errors = validate_file(f, schema)
        if errors:
            all_errors.extend(errors)

    if all_errors:
        print("\n[91mUDS Frontmatter pre-commit check FAILED:[0m")
        for error in all_errors:
            print(f"- {error}")
        print("\nPlease fix the errors above and try again.")
        sys.exit(1)
    else:
        print(f"\n[92mUDS Frontmatter pre-commit check PASSED for {len(staged_files)} file(s).[0m")
        sys.exit(0)

if __name__ == "__main__":
    main()
