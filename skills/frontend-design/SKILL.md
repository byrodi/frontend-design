---
name: frontend-design
description: >
  Light pink-plum design system with CSS tokens, a design reference and an
  interactive HTML starter. Use when asked to build, lay out or restyle a
  site, landing page, web app, desktop UI or component in this style. Not for
  backend or infrastructure. When the project already has its own design
  system, do not apply this skill and follow that system.
---

# Frontend design

Build calm, light and clear interfaces from one visual family. Keep the recognizable tones and character, but choose the composition, imagery and scenarios for the specific product. A new explicit request from the user takes priority.

All skill files live in `${CLAUDE_SKILL_DIR}`, the folder that contains this SKILL.md. Claude Code substitutes the path. If the variable is left as is anywhere in the text, references included, read it as the folder that contains SKILL.md.

## Style basics

- An almost white background with a pink tint, white surfaces, a dusty pink accent, and a deep rose for links and active labels. A muted plum is the secondary accent.
- Plenty of air, thin borders, soft radii in several sizes. Shadows are barely visible and explain a layer or a movement.
- A calm sans-serif that covers the interface language, with a clear hierarchy. A large concise heading suits a landing page; in a working app, density and overview matter more.
- Pink marks the main action or a choice. Do not paint the whole screen with it; errors and success have their own semantic colors.
- Simple outline icons, real previews, clear diagrams. One expressive visual center beats a scatter of decorations.
- Do not turn every row into a separate card. Related objects group well into one surface with dividers.

## Interaction priorities

**Interaction beats plain input.** First look for a way to choose, toggle, drag, compare or try something with immediate feedback. For a finite set of options use visual cards or segments, for a range a slider with a visible value and exact input when it is needed, for relations a controllable diagram. Keep text fields for text, search and arbitrary exact data. Interactivity belongs where it cuts effort; a game on top of a simple task is too much.

**Pictures beat long text.** Show the result with a real screenshot, a subject illustration, a preview or a diagram, and add a short caption. A live example is better than a description of its features. An icon does not replace a meaningful picture. Keep action names, errors, values and accessible labels as text, never hidden inside an image. Use existing assets or an available generation tool when it helps; SVG and CSS suit diagrams. Do not require a specific MCP server or generator.

**Simplicity beats feature count.** Pick one main task per screen and one main next step. Offer sensible defaults and reveal rare settings on demand. Do not add pricing, analytics, filters, extra pages or settings without a need. Keep explicitly requested features and shorten the path to them.

## Workflow

1. Look at the existing stack, components, content and assets. Identify the person's main task. The context is usually enough, so make reversible decisions on your own.
2. Read `${CLAUDE_SKILL_DIR}/references/design-system.md` for the palette, sizes and layouts. Pick the scale for the task, a landing page or a working interface. For a targeted edit, keep the neighbouring patterns and do not start an unrequested full redesign.
3. Use `${CLAUDE_SKILL_DIR}/assets/tokens.css` as the base theme. Carry the tokens into CSS variables, Tailwind, MUI or the project's existing system without replacing its stack. For a new interface or a visual choice, open `${CLAUDE_SKILL_DIR}/assets/interactive-starter.html`, a self-contained working example with an SVG preview, choice cards and feedback. Copy the parts you need together with their CSS and adapt the data and composition.
4. Implement the real main scenario. In a demo, state its limits clearly. In a product, wire actions to state and the existing API; a success message must mean real success.
5. Check narrow and wide screens, the keyboard, long labels, selection states and errors. With a browser available, look at screenshots and walk through the main scenario. Without one, report that limit and do not claim visual testing.

## Definition of done

- It is clear what can be done here without reading long instructions.
- A meaningful visual example stands where it explains better than a paragraph, and controls show the result right away.
- The palette stays soft and text stays readable, so no small white letters on light pink. Check the contrast of the final combinations, selected and disabled states included.
- Controls work from the keyboard, focus is visible, targets are comfortable to tap. Drag and drop has a path through buttons or selection, and hover is never the only way to learn or do something.
- Images have meaningful alt text, decorative ones get an empty alt or aria-hidden. Status is clear without color, through text or an icon. Animation respects prefers-reduced-motion.
- On mobile there is no horizontal overflow and no hidden main action. Long names and translations do not break the grid.
- No dead buttons, no decorative charts with made-up numbers, no endless animation and no unrequested features.

The skill needs no network. The palette, examples and starter are all in this folder.
