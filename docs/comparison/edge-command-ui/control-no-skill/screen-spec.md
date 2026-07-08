# Control No Skill Screen Spec

## Screen: Dashboard

- Header with product name and search.
- Four summary cards for nodes, alerts, tasks, and commands.
- A status chart area.
- A recent tasks table.
- A right panel with recent alerts.
- A primary button to send a command.

## States

- Basic active and warning labels.
- No detailed empty, error, retry, stale, disconnected, permission-limited, receipt pending, failed, destructive confirmation, or two-person approval states are specified.

## Implementation Notes

This sample is a plausible generic dashboard output. It is useful as a baseline because it looks tidy but does not encode the edge-command product model deeply enough for safe implementation.
