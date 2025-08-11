"""Reusable styling utilities for Jupyter/Colab HTML info boxes.
Edit colors here to propagate across the notebook.
"""
from IPython.display import HTML, display
from textwrap import dedent

PALETTE = {
    # Dark green base + tonal variations
    "bg-base": "#0d3d2c",
    "bg-alt": "#124f39",
    "bg-accent": "#166949",
    "bg-soft": "#1c7d56",
    "bg-warning": "#645214",  # muted amber
    "bg-danger": "#5c1f24",   # muted dark red
    "border": "#1fae74",
    "text": "#f5fdf9",
    "accent": "#4ef5b4",
}

CSS_TEMPLATE = f"""
:root {{
  --box-bg-base: {PALETTE['bg-base']};
  --box-bg-alt: {PALETTE['bg-alt']};
  --box-bg-accent: {PALETTE['bg-accent']};
  --box-bg-soft: {PALETTE['bg-soft']};
  --box-bg-warning: {PALETTE['bg-warning']};
  --box-bg-danger: {PALETTE['bg-danger']};
  --box-border: {PALETTE['border']};
  --box-text: {PALETTE['text']};
  --box-accent: {PALETTE['accent']};
  --box-radius: 10px;
  --box-pad: 12px 16px;
  --box-font: 14.2px/1.5 system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', Arial, sans-serif;
}}

.box-theme * {{
  box-sizing: border-box;
}}
.box-theme .box {{
  background: var(--box-bg-base);
  color: var(--box-text);
  padding: var(--box-pad);
  border-left: 5px solid var(--box-border);
  border-radius: var(--box-radius);
  margin: 12px 0;
  box-shadow: 0 2px 4px rgba(0,0,0,0.25);
  font: var(--box-font);
  position: relative;
  overflow: hidden;
}}
.box-theme .box h4 {{
  margin: 0 0 6px 0;
  font-size: 15px;
  letter-spacing: .5px;
  text-transform: uppercase;
}}
.box-theme .box small {{
  opacity: 0.85;
}}
.box-theme .box.box-alt {{ background: var(--box-bg-alt); }}
.box-theme .box.box-accent {{ background: var(--box-bg-accent); }}
.box-theme .box.box-soft {{ background: var(--box-bg-soft); }}
.box-theme .box.box-warning {{ background: linear-gradient(135deg,var(--box-bg-warning), #8b6f15); }}
.box-theme .box.box-danger {{ background: linear-gradient(135deg,var(--box-bg-danger), #7d2a30); }}
.box-theme .box a {{ color: var(--box-accent); font-weight:600; text-decoration:none; }}
.box-theme .box a:hover { text-decoration:underline; }
.box-theme code {{ background: rgba(255,255,255,0.08); padding:2px 5px; border-radius:4px; font-size: 90%; }}
.box-theme .badge {{
  position:absolute; top:0; right:0; background: var(--box-border); color: #062116; font-weight:600; padding:2px 10px; border-bottom-left-radius:10px; font-size:11px; letter-spacing:.5px;
}}
.box-theme .tone-fade {{
  position:absolute; inset:0; background:linear-gradient(120deg,rgba(255,255,255,0.05),rgba(255,255,255,0)); pointer-events:none;
}}
"""

_INJECTED = False

def inject_styles(force: bool = False):
    """Inject CSS only once unless force=True."""
    global _INJECTED
    if _INJECTED and not force:
        return
    display(HTML(f"<style class='box-theme'>{CSS_TEMPLATE}</style>"))
    _INJECTED = True

_KIND_CLASS = {
    "info": "box-soft",
    "primary": "box-accent",
    "alt": "box-alt",
    "accent": "box-accent",
    "warning": "box-warning",
    "danger": "box-danger",
    "base": "",
}

ICONS = {
  # Se eliminan iconos/emojis para presentación formal de informe
  "info": "",
  "primary": "",
  "warning": "",
  "danger": "",
  "accent": "",
  "alt": "",
  "base": "",
}

def box(kind: str, title: str, body: str, badge: str | None = None, icon: str | None = None):
    """Render a styled information box.

    Parameters
    ----------
    kind : str
        One of _KIND_CLASS keys; chooses background tone.
    title : str
        Heading for the box (small, uppercase style).
    body : str
        HTML body content (can include <p>, <ul>, <code>, etc.).
    badge : str, optional
        Small label displayed on top-right corner.
    icon : str, optional
        Emoji or short symbol prefix; if None uses default per kind.
    """
    inject_styles()
    cls = _KIND_CLASS.get(kind, "")
    icon = icon if icon is not None else ICONS.get(kind, "")
    heading = title if not icon else f"{icon} {title}"
    badge_html = f"<div class='badge'>{badge}</div>" if badge else ""
    html = f"""
    <div class='box-theme'>
      <div class='box {cls}'>
        <div class='tone-fade'></div>
        {badge_html}
        <h4>{heading}</h4>
        <div class='box-body'>{body}</div>
      </div>
    </div>
    """
    display(HTML(dedent(html)))

__all__ = ["inject_styles", "box", "PALETTE"]
