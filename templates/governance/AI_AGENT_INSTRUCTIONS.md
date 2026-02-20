# AI Agent Instructions

**VERSION:** 1.0.0
**STATUS:** STABLE

## 1. Core Directive

Your primary objective is to autonomously execute the tasks defined in the active phase of the `manifest.json`. You must adhere to all defined protocols, standards, and quality controls. Your goal is to produce high-quality, verifiable work that moves the project forward.

## 2. Onboarding Protocol

Upon waking in a new repository, you **MUST** perform the following onboarding sequence:

1.  **Read `CONTEXT.md`:** This is your primary entry point. It provides a high-level summary of the repository's architecture, dependencies, and key commands.
2.  **Read `docs/planning/manifest.json`:** This file contains the master plan for the repository, including the current phase and the status of all other phases.
3.  **Read `docs/planning/AGENTS.md`:** This file contains the current objective and any session-specific context.
4.  **Read the Active Phase YAML:** Read the YAML file for the `current_phase` defined in `manifest.json` (e.g., `docs/planning/phases/phase_01_...yaml`).

## 3. Execution Loop

For each step in the active phase YAML, you must follow this strict execution loop:

1.  **Announce State:** Begin every turn with a state block: `[STATE: Phase X | STEP: Y | DEPS: Z]`.
2.  **Execute Action:** Perform the task defined in the `action` field.
3.  **Verify Completion:** Run the command specified in the `verification_method` field.
4.  **Record Proof:** Paste the full, unmodified terminal output of the verification command into the `proof_of_work` field in the phase YAML.
5.  **Update Status:** Change the step's `status` to `COMPLETED`.
6.  **Commit & Push:** Commit the updated phase YAML file with a clear commit message (e.g., `feat(planning): complete step 01.2`).

## 4. Quality & Governance

-   **Documentation Standard:** All documentation you create or modify **MUST** adhere to the [NizamIQ Unified Documentation Standard (UDS)](https://github.com/nizamiq/documentation-standard).
-   **CI/CD Pipeline:** All code changes **MUST** pass the "Golden Pipeline" CI/CD checks. Do not merge pull requests that have failing checks.
-   **Technical Debt:** Before starting a new phase, you **MUST** review `docs/planning/DEBT.md`. If any high-priority debt is relevant to the current phase, you must address it before proceeding.

## 5. Error Handling

-   **Circuit Breaker:** If you fail to complete a step after **three** attempts, you MUST stop, mark the step as `BLOCKED`, add a detailed explanation to the `observation` field, and ask for human intervention.
-   **Self-Correction:** Do not get stuck in infinite loops. If a test is failing, analyze the error, refactor the code, and try again. If it continues to fail, invoke the circuit breaker.
