---
name: qwen-diagram-design
description: Create a concise technical process or architecture diagram from a topic using the diagram-design renderer. Trigger for flow diagrams, system diagrams, lifecycle maps, and technical explainers.
---
# Qwen Diagram Design
1. Copy `templates/content.json` to a new JSON file and replace values only; use 4–7 short steps, accurate labels and one takeaway of at most 65 characters.
2. On first use, run `scripts/setup.sh`; then run `scripts/make.sh <content-file> <out-dir>` from this skill directory. Do not write HTML, SVG, or layout code.
3. Read the one-line JSON result; if it reports failure, use the table below and rerun.
4. Verify the PNG visually at fit-to-page scale and inspect dimensions; ensure no label is clipped or overlapping.

| Common failure | Fix |
|---|---|
| Missing field / malformed JSON | Restore template keys and valid JSON strings. |
| Long or clipped labels | Keep labels ≤28, details ≤48, takeaway ≤65 characters. |
| Too many nodes | Keep 4–7 ordered steps. |
| Export dependency missing | Run `scripts/setup.sh`, then rerun make.sh; do not substitute a renderer. |

Content template: `templates/content.json`.