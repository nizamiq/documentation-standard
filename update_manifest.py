
import yaml
import json
import os

repo_path = '/home/ubuntu/repos/documentation-standard/'
phases_dir = os.path.join(repo_path, 'docs/planning/phases/')
manifest_path = os.path.join(repo_path, 'docs/planning/manifest.json')

phase_files = [
    'phase_00_init.yaml',
    'phase_01_uds_definition.yaml',
    'phase_02_ecosystem_migration.yaml',
    'phase_03_automated_enforcement.yaml',
    'phase_04_ecosystem_wide_enforcement.yaml'
]

all_phases_data = {}
for filename in phase_files:
    file_path = os.path.join(phases_dir, filename)
    with open(file_path, 'r') as f:
        try:
            # Use safe_load_all to handle multiple YAML documents in a single file
            for doc in yaml.safe_load_all(f):
                if doc and 'phase_id' in doc:
                    phase_id = doc.get('phase_id')
                    all_phases_data[phase_id] = doc
                    break # Assuming the first document with phase_id is the relevant one
        except yaml.YAMLError as e:
            print(f"Error reading YAML file {filename}: {e}")

completed_phases = []
current_phase = None
last_validated_step = "00.0"

# Sort phases by ID to process them in order
sorted_phase_ids = sorted(all_phases_data.keys())

for phase_id in sorted_phase_ids:
    phase = all_phases_data[phase_id]
    all_steps_completed = True
    if 'steps' in phase:
        for step in phase['steps']:
            if step.get('status') != 'COMPLETED':
                all_steps_completed = False
            if step.get('status') == 'COMPLETED' and step.get('id') > last_validated_step:
                last_validated_step = step.get('id')
    else:
        # If a phase has no steps, consider its completion based on its own status
        if phase.get('status') != 'COMPLETED':
            all_steps_completed = False

    if all_steps_completed:
        completed_phases.append(phase_id)
    elif current_phase is None: # This is the first non-completed phase
        current_phase = phase_id

# If all phases are completed, current_phase should be the last phase ID
if current_phase is None and sorted_phase_ids:
    current_phase = sorted_phase_ids[-1]

# Determine overall status
overall_status = "IN_PROGRESS"
if len(completed_phases) == len(sorted_phase_ids):
    overall_status = "COMPLETED"

# Load existing manifest.json
with open(manifest_path, 'r') as f:
    manifest = json.load(f)

# Update manifest.json
manifest['completed_phases'] = completed_phases
manifest['current_phase'] = current_phase
manifest['status'] = overall_status
manifest['last_updated'] = '2026-02-22'
manifest['last_updated_by'] = 'Protocol-01 Remediation Agent'
manifest['active_context']['last_validated_step'] = last_validated_step

# Write updated manifest.json back
with open(manifest_path, 'w') as f:
    json.dump(manifest, f, indent=2)

print("Manifest updated successfully.")
