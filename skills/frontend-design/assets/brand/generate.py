"""Regenerates every file in this folder. Needs rsvg-convert and ffmpeg: python3 generate.py"""
import math, os, subprocess, tempfile

ROSE, CREAM, INK, TEXT = "#D78494", "#FDEFF2", "#8E3A50", "#29242A"
SW = 22  # stroke width in logo units
Q = math.pi * 25  # quarter arc, r=50
C = 2 * math.pi * 50

def circle_path(cx):
    return f"M{cx},0 A50,50 0 0 0 {cx-50},50 A50,50 0 0 0 {cx},100 A50,50 0 0 0 {cx+50},50 A50,50 0 0 0 {cx},0"

# (path, length, draw window in seconds)
STROKES = [
    ("M0,100 V50 A50,50 0 0 1 50,0 H58", 50 + Q + 8, (0.00, 0.45)),
    (circle_path(156), C, (0.25, 0.75)),
    (circle_path(304), C, (0.50, 1.00)),
    ("M354,-50 V100", 150, (0.80, 1.10)),
    ("M406,0 V100", 100, (0.95, 1.25)),
]
I_DOT, PERIOD = (406, -45, 13), (457, 97, 14)
BBOX = (-11, -61, 471, 111)  # x0 y0 x1 y1
MARK_PERIOD, MARK_BBOX = (88, 97, 14), (-11, -11, 102, 111)

def clamp(x): return max(0.0, min(1.0, x))
def ease(x): x = clamp(x); return x * x * (3 - 2 * x)
def back_out(x):
    x = clamp(x); c = 2.2
    return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2
def bounce(x):
    x = clamp(x); n, d = 7.5625, 2.75
    if x < 1 / d: return n * x * x
    if x < 2 / d: x -= 1.5 / d; return n * x * x + 0.75
    if x < 2.5 / d: x -= 2.25 / d; return n * x * x + 0.9375
    x -= 2.625 / d; return n * x * x + 0.984375
def win(u, a, b): return clamp((u - a) / (b - a))

def stroke(d, L, vis_from, vis_to, color):
    if vis_to - vis_from < 0.5: return ""
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{SW}" stroke-linecap="round" '
            f'stroke-linejoin="round" stroke-dasharray="{vis_to-vis_from:.2f} {L*3:.2f}" stroke-dashoffset="{-vis_from:.2f}"/>')

def dot(x, y, r, color, scale=1.0, dy=0.0):
    if scale <= 0.01: return ""
    return f'<circle cx="{x}" cy="{y+dy:.2f}" r="{r*scale:.2f}" fill="{color}"/>'

def logo(u, ink=CREAM, accent=INK):
    """Wordmark state at timeline time u (seconds): draw 0-1.3, dots 1.1-2.05, pulse 2.8, erase 3.9-4.7."""
    out = []
    n = len(STROKES)
    for i, (d, L, (a, b)) in enumerate(STROKES):
        drawn = ease(win(u, a, b)) * L
        k = n - 1 - i  # erase last letter first
        gone = ease(win(u, 4.0 + 0.06 * k, 4.4 + 0.06 * k)) * L
        out.append(stroke(d, L, gone, drawn, ink))
    shrink = 1 - ease(win(u, 3.9, 4.2))
    out.append(dot(*I_DOT, ink, back_out(win(u, 1.15, 1.45)) * shrink))
    fall = bounce(win(u, 1.35, 2.05))
    pulse = 1 + 0.35 * math.sin(math.pi * win(u, 2.8, 3.15)) + 0.15 * math.sin(math.pi * win(u, 3.2, 3.45))
    if u >= 1.35:
        out.append(dot(*PERIOD, accent, pulse * (1 - ease(win(u, 4.35, 4.6))), dy=-(1 - fall) * 200))
    return "".join(out)

def mark(ink=CREAM, accent=INK):
    return (f'<path d="{STROKES[0][0]}" fill="none" stroke="{ink}" stroke-width="{SW}" stroke-linecap="round" '
            f'stroke-linejoin="round"/>{dot(*MARK_PERIOD, accent)}')

def place(bbox, target_cx, target_cy, size, by_height=False):
    x0, y0, x1, y1 = bbox
    s = size / ((y1 - y0) if by_height else (x1 - x0))
    return f'translate({target_cx - (x0+x1)/2*s:.2f},{target_cy - (y0+y1)/2*s:.2f}) scale({s:.4f})'

def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>'

def banner(w, h, u, cx, cy, lw):
    return svg(w, h, f'<rect width="{w}" height="{h}" fill="{ROSE}"/><g transform="{place(BBOX, cx, cy, lw)}">{logo(u)}</g>')

def render(svg_text, png):
    subprocess.run(["rsvg-convert", "-o", png], input=svg_text.encode(), check=True)

def write(name, text):
    with open(f"{OUT}/{name}", "w") as fh: fh.write(text + "\n")

# Web version: draws once on load, no loop, still for prefers-reduced-motion.
# The period follows the same curve as bounce(): it lands on the baseline and
# hops three times, each hop lower, and never sinks below the line.
ANIMATED_CSS = """
path{stroke-dasharray:1 2;stroke-dashoffset:1;opacity:0;animation:draw .5s cubic-bezier(.45,0,.25,1) forwards}
.i{transform-box:fill-box;transform-origin:center;transform:scale(0);animation:pop .3s 1.15s cubic-bezier(.3,1.6,.5,1) forwards}
.p{transform:translateY(-200px);opacity:0;animation:drop .7s 1.35s forwards}
@keyframes draw{0%{opacity:1}to{opacity:1;stroke-dashoffset:0}}
@keyframes pop{to{transform:scale(1)}}
@keyframes drop{0%{opacity:1;transform:translateY(-200px);animation-timing-function:cubic-bezier(.33,0,.67,.33)}
36.4%{transform:none;animation-timing-function:cubic-bezier(.33,.67,.67,1)}
54.5%{transform:translateY(-50px);animation-timing-function:cubic-bezier(.33,0,.67,.33)}
72.7%{transform:none;animation-timing-function:cubic-bezier(.33,.67,.67,1)}
81.8%{transform:translateY(-12.5px);animation-timing-function:cubic-bezier(.33,0,.67,.33)}
90.9%{transform:none;animation-timing-function:cubic-bezier(.33,.67,.67,1)}
95.5%{transform:translateY(-3px);animation-timing-function:cubic-bezier(.33,0,.67,.33)}
to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){path,.i,.p{animation:none;stroke-dashoffset:0;transform:none;opacity:1}}
"""

def animated_logo():
    parts = []
    for d, _, (a, b) in STROKES:
        parts.append(f'<path d="{d}" pathLength="1" style="animation-delay:{a}s;animation-duration:{b-a:.2f}s"/>')
    x, y, r = I_DOT
    parts.append(f'<circle class="i" cx="{x}" cy="{y}" r="{r}" fill="{TEXT}" stroke="none"/>')
    x, y, r = PERIOD
    parts.append(f'<circle class="p" cx="{x}" cy="{y}" r="{r}" fill="{ROSE}" stroke="none"/>')
    x0, y0, x1, y1 = BBOX
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0} {y0} {x1-x0} {y1-y0}" role="img" aria-label="rodi.">'
            f'<style>{ANIMATED_CSS.strip()}</style>'
            f'<g fill="none" stroke="{TEXT}" stroke-width="{SW}" stroke-linecap="round" stroke-linejoin="round">'
            f'{"".join(parts)}</g></svg>')

OUT = os.path.dirname(os.path.abspath(__file__))
HOLD = 2.2  # frame 0 shows the full logo: static previews use the first frame
T, FPS = 5.0, 25
W, H = 680, 240
BANNER_ARGS = (W * 0.5, H * 0.5, 270)  # wordmark in the center

with tempfile.TemporaryDirectory() as tmp:
    for f in range(int(T * FPS)):
        render(banner(W, H, (HOLD + f / FPS) % T, *BANNER_ARGS), f"{tmp}/f{f:03d}.png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", f"{tmp}/f%03d.png",
                    "-vf", "split[a][b];[a]palettegen=max_colors=32:stats_mode=full[p];[b][p]paletteuse=dither=none",
                    "-loop", "0", f"{OUT}/banner.gif"], check=True)

render(banner(W, H, HOLD, *BANNER_ARGS), f"{OUT}/banner.png")
render(banner(1500, 500, HOLD, 750, 250, 620), f"{OUT}/header-1500x500.png")

# Wordmark: on the brand pink, and on a light page.
x0, y0, x1, y1 = BBOX
vb = f'viewBox="{x0} {y0} {x1-x0} {y1-y0}"'
write("logo-rodi-on-rose.svg", svg(500, 180, f'<rect width="500" height="180" rx="24" fill="{ROSE}"/>'
                                            f'<g transform="{place(BBOX, 250, 90, 380)}">{logo(HOLD)}</g>'))
write("logo-rodi.svg", f'<svg xmlns="http://www.w3.org/2000/svg" {vb} role="img" aria-label="rodi.">{logo(HOLD, TEXT, ROSE)}</svg>')
write("logo-rodi-animated.svg", animated_logo())

# Mark "r.": avatar and a transparent icon.
x0, y0, x1, y1 = MARK_BBOX
write("mark-r.svg", f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0} {y0} {x1-x0} {y1-y0}" role="img" aria-label="r.">{mark(TEXT, ROSE)}</svg>')
avatar = svg(1024, 1024, f'<rect width="1024" height="1024" fill="{ROSE}"/>'
                         f'<g transform="{place(MARK_BBOX, 512, 512, 400, by_height=True)}">{mark()}</g>')
write("avatar-mark.svg", avatar)
render(avatar, f"{OUT}/avatar-mark.png")
render(svg(1024, 1024, f'<rect width="1024" height="1024" fill="{ROSE}"/>'), f"{OUT}/avatar-plain.png")
