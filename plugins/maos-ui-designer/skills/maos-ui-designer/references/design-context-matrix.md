# Design Context Matrix

Use this reference when industry, style, palette, or surface type materially affects the design. Pick a context, state assumptions, then adapt the workflow.

## Context Template

Use this compact form in briefs:

`Context`: industry / style / palette / surface / density / risk

Example: `Context`: fintech / data-dense operational / neutral + blue-green semantic palette / responsive web / Next.js + StyleX + headless components / AI-friendly tokenized UI / compact daily-use / regulated data.

## Industry Directions

- `Enterprise SaaS`: calm, dense, predictable navigation, tables, filters, permissions, audit trails, restrained accent color.
- `Finance/fintech`: trust, precision, comparison, risk indicators, strong number formatting, conservative palette, explicit states.
- `Healthcare`: clarity, empathy, safety, high contrast, restrained color, privacy cues, error prevention, accessible forms.
- `Developer tools`: technical density, command syntax, logs, code blocks, dark/light support, keyboard flows, clear error recovery.
- `E-commerce`: product inspection, imagery, price/action hierarchy, trust signals, mobile purchase flow, clear empty/cart states.
- `Education`: progress, guidance, readable pacing, encouraging feedback, structured navigation, lower cognitive load.
- `Creative/media`: stronger imagery, editorial rhythm, expressive typography, but still clear creation/review actions.
- `Industrial/IoT/ops`: command-center hierarchy, status maps, alerts, device health, timelines, redundancy, safety states.
- `Cybersecurity`: severity, provenance, evidence, triage, containment actions, timeline, auditability, dark technical modes when useful.
- `Government/legal`: procedural clarity, forms, evidence, status, compliance, conservative palette, accessibility, audit trail.
- `Consumer productivity`: friendly but efficient, low-friction onboarding, lightweight hierarchy, clear sync/recovery states.

## Style Directions

- `Operational`: quiet, compact, durable for daily work; prioritize speed and scanning over visual drama.
- `Data-dense`: tight tables, charts, summaries, legends, annotations, sorting, filtering, comparison, and export paths.
- `Editorial`: strong reading hierarchy, content rhythm, narrative sections, high-quality imagery, careful line length.
- `Brand-forward`: expressive first viewport, custom imagery, distinctive color/type, but keep actions and product evidence obvious.
- `Command-center`: real-time status, maps/boards, alerts, timelines, redundancy, clear severity and escalation paths.
- `Playful`: warmer copy, richer motion, characterful shapes or icons; keep task completion obvious.
- `Luxury/minimal`: restraint, whitespace, refined typography, low noise; avoid hiding core actions.
- `Technical/developer`: monospace where useful, code/log surfaces, keyboard affordances, precise labels, useful defaults.
- `Terminal-native`: text hierarchy, command ergonomics, ANSI color discipline, readable wrapping, no reliance on color alone.

## Palette Directions

- `Neutral workbench`: gray/white surfaces, one restrained accent, semantic success/warning/danger.
- `Enterprise blue`: blue for trust and navigation; avoid making every surface blue.
- `Finance green/blue`: green for positive money/status, blue for trust; use red carefully for loss/risk.
- `Health teal`: teal/blue-green with strong contrast, calm surfaces, limited saturation.
- `Ops amber`: amber/red only for severity and attention; keep normal state neutral.
- `Dark technical`: dark surfaces for logs, maps, monitoring, or developer tools; verify contrast and glare.
- `High-contrast terminal`: ANSI palette with semantic mapping; ensure output works without color.
- `Brand-specific`: derive tokens from the brand, then assign semantic roles instead of scattering brand color everywhere.

## Surface Directions

- `Web app`: reusable components, layout shells, responsive breakpoints, focus states, browser QA.
- `Responsive web`: explicit mobile reflow, touch targets, collapsed filters, sticky actions only when useful.
- `Mobile app`: thumb reach, native-feeling navigation, fewer competing regions, offline/loading clarity.
- `Desktop app`: menu/toolbars, shortcuts, resizable panels, local file/system states, dense workflows.
- `Figma prototype`: editable structure, named frames, reusable components, clear sections, annotation only when useful.
- `CLI`: command names, flags, help, examples, progress, errors, exit codes, machine-readable options.
- `TUI`: keyboard navigation, focus, panels, scroll, resize behavior, color fallback, status bar, help overlay.
- `Terminal output`: columns, wrapping, log levels, timestamps, status glyph alternatives, copy-paste-safe text.
- `Docs/README`: task-first structure, commands, expected output, troubleshooting, concise examples.

## Decision Rules

- If the user names an industry, use its expectations before choosing style.
- If the user names a style, adapt it to the product job instead of copying visual tropes.
- If the user names a palette, map it to semantic roles before applying it.
- If the surface is CLI/TUI/terminal, treat typography, spacing, color, and interaction as text-system design, not web layout.
- If the framework or styling system is specified, let component choices, token structure, and interaction patterns fit that system instead of inventing unrelated UI primitives.
- If AI-friendly UI is requested, optimize for semantic structure, stable component APIs, tokenized styles, accessible names, and testability.
- If the product is internal or operational, default to clarity, density, and durability over visual spectacle.
- If the product is marketing, brand, or portfolio, allow stronger imagery and expressive typography while preserving obvious actions.
