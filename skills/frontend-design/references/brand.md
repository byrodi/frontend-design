# Brand: rodi.

The author's personal brand, built from the same family as the design system. Use it on the author's own sites, projects, profiles and covers (anything signed "by rodi."). A product with its own name keeps its own logo; the brand appears there at most as a small "by rodi." credit.

## Colors

| Role | Value | Use |
| --- | --- | --- |
| Brand pink | `#d78494` | Avatar, banners, brand surfaces |
| Brand blush | `#efccd4` | Profile background next to brand pink |
| Brand cream | `#fdeff2` | Letters on brand pink |
| Brand ink | `#8e3a50` | The period on brand pink |

Brand pink is the identity color and is slightly deeper than the UI accent `#e47f93`. Buttons and selection in an interface still use the UI accent. On a light page the wordmark is drawn in main text `#29242a` with the period in brand pink.

## Wordmark and mark

- `rodi.` is monoline lettering: one stroke width, round caps, a circle for `o` and the bowl of `d`. It is drawn from SVG paths, so no font is needed.
- The period is the signature. It always takes the accent color (brand ink on pink, brand pink on light) and never matches the letters.
- The short mark is `r.`, used for avatars and icons.
- Keep clear space of at least the height of `o` around the wordmark. Do not stretch it, outline it, add shadows or gradients, or place it on a busy photo.
- Discord status and signatures use the text form "by rodi.".

## Motion

The wordmark is written like handwriting: letters draw in one after another, the dot of `i` pops in and the period drops in with a small bounce. On the web it plays once on load and respects prefers-reduced-motion. The looping version is only for the animated banner. Its first frame shows the full logo, because static previews show the first frame.

## Files

All files live in `${CLAUDE_SKILL_DIR}/assets/brand/` and are produced by `generate.py` (needs `rsvg-convert` and `ffmpeg`). Change colors, timing or stroke width there and rerun it instead of editing the output by hand.

| File | Use |
| --- | --- |
| `logo-rodi.svg` | Wordmark for light pages, transparent background |
| `logo-rodi-animated.svg` | Same wordmark, draws in once; embed with `<img>` or inline |
| `logo-rodi-on-rose.svg` | Wordmark on a brand pink plate |
| `mark-r.svg` | `r.` icon for light backgrounds, fits a favicon |
| `avatar-mark.svg`, `avatar-mark.png` | 1024 px avatar, brand pink with a cream `r.` |
| `banner-discord.gif`, `banner-discord.png` | 680x240 profile banner, animated and static |
| `header-1500x500.png` | Header for X, Twitch and similar services |

In a Discord profile the avatar covers the lower left part of the banner, so the wordmark sits right of center. Profile theme colors: primary `#d78494`, accent `#efccd4`.
