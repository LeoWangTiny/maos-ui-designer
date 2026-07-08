# Generic Design Skill Screen Spec

## Screen Coverage

- Overview: summary cards, chart, and recent mission table.
- Alerts: side panel with alert detail and evidence preview.
- Commands: simple command review area with primary and secondary actions.

## Components

- App sidebar.
- Metric cards.
- Status chart.
- Mission table.
- Alert detail panel.
- Command review panel.
- Tags, buttons, and filters.

## States

- Active, warning, danger, selected, and disabled states.
- Basic mobile layout.
- Loading and empty states are mentioned but not fully designed.

## Implementation Notes

The prototype is intended as a general design-system page. It uses clean layout and reusable visual blocks, but it does not encode MAOS-level edge command safety, permission-limited workflow, command receipt timeout, failed recovery, audit replay, or stable `rowKey` / `data-testid` testing hooks as first-class requirements.
