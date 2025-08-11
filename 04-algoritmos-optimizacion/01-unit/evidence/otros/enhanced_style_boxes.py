"""Reusable styling utilities for Jupyter/Colab HTML info boxes.
Edit colors here to propagate across the notebook.
"""
from IPython.display import HTML, display
from textwrap import dedent
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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
    
    # Nuevas categorías para gráficos
    "chart-primary": "#1fae74",
    "chart-secondary": "#4ef5b4", 
    "chart-tertiary": "#8bffe4",
    "chart-highlight": "#ffcc29",
    "chart-grid": "#0a2c20",
    
    # Colores para múltiples series
    "series": ["#1fae74", "#4ef5b4", "#8bffe4", "#ffcc29", "#ff7e5f", "#b967ff", "#71c7ec"]
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
  
  --chart-primary: {PALETTE['chart-primary']};
  --chart-secondary: {PALETTE['chart-secondary']};
  --chart-tertiary: {PALETTE['chart-tertiary']};
  --chart-highlight: {PALETTE['chart-highlight']};
  --chart-grid: {PALETTE['chart-grid']};
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
.box-theme .box a:hover {{ text-decoration:underline; }}
.box-theme code {{ background: rgba(255,255,255,0.08); padding:2px 5px; border-radius:4px; font-size: 90%; }}
.box-theme .badge {{
  position:absolute; top:0; right:0; background: var(--box-border); color: #062116; font-weight:600; padding:2px 10px; border-bottom-left-radius:10px; font-size:11px; letter-spacing:.5px;
}}
.box-theme .tone-fade {{
  position:absolute; inset:0; background:linear-gradient(120deg,rgba(255,255,255,0.05),rgba(255,255,255,0)); pointer-events:none;
}}

/* Estilos para ecuaciones matemáticas */
.box-theme .math-container {{
  background: rgba(255,255,255,0.08);
  border-radius: 8px;
  padding: 15px;
  margin: 15px 0;
  font-size: 16px;
}}

/* Estilos para tarjetas de conceptos */
.box-theme .concept-card {{
  background: var(--box-bg-alt);
  border: 1px solid var(--box-border);
  border-radius: var(--box-radius);
  padding: 12px;
  margin: 10px 0;
}}

.box-theme .concept-card h5 {{
  color: var(--box-accent);
  margin-top: 0;
  margin-bottom: 8px;
  font-size: 16px;
}}

/* Columnas flexibles */
.box-theme .flex-container {{
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin: 15px 0;
}}

.box-theme .flex-item {{
  flex: 1 1 300px;
}}

/* Timeline para procesos */
.box-theme .timeline {{
  position: relative;
  padding-left: 30px;
}}

.box-theme .timeline::before {{
  content: '';
  position: absolute;
  left: 5px;
  top: 0;
  height: 100%;
  width: 2px;
  background: var(--box-border);
}}

.box-theme .timeline-item {{
  position: relative;
  margin-bottom: 20px;
}}

.box-theme .timeline-item::before {{
  content: '';
  position: absolute;
  left: -25px;
  top: 5px;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--box-accent);
}}

/* Estilos para tablas */
.box-theme table {{
  width: 100%;
  border-collapse: collapse;
  margin: 15px 0;
  color: var(--box-text);
}}

.box-theme th {{
  background: var(--box-bg-alt);
  text-align: left;
  padding: 8px;
}}

.box-theme td {{
  padding: 8px;
  border-top: 1px solid rgba(255,255,255,0.1);
}}

.box-theme tr:nth-child(even) {{
  background: rgba(255,255,255,0.03);
}}

/* Nuevo - Resaltado para explicaciones de variables */
.box-theme .highlight-var {{
  display: inline-block;
  background: rgba(31, 174, 116, 0.2);
  border-bottom: 1px dotted var(--box-border);
  padding: 0 3px;
  margin: 0 1px;
}}

/* Bloques de secciones para resultados */
.box-theme .section-block {{
  background: var(--box-bg-alt);
  border-left: 5px solid var(--box-accent);
  border-radius: var(--box-radius);
  padding: 15px;
  margin: 20px 0;
}}

.box-theme .section-title {{
  font-size: 18px;
  color: var(--box-accent);
  margin-top: 0;
  margin-bottom: 10px;
  font-weight: 600;
}}

/* Tarjetas de parámetros */
.box-theme .param-card {{
  background: rgba(255,255,255,0.05);
  border-radius: 8px;
  padding: 10px;
  margin: 8px 0;
}}

.box-theme .param-name {{
  font-weight: bold;
  color: var(--box-accent);
}}

.box-theme .param-value {{
  font-family: monospace;
  background: rgba(0,0,0,0.2);
  padding: 2px 5px;
  border-radius: 4px;
  margin-left: 5px;
}}

/* Estilos para key insights */
.box-theme .key-insight {{
  background: var(--box-bg-accent);
  border-radius: var(--box-radius);
  padding: 12px 15px;
  margin: 15px 0;
  border-left: 5px solid #ffcc29;
}}

.box-theme .key-insight h5 {{
  color: #ffcc29;
  margin-top: 0;
  margin-bottom: 5px;
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
  "info": "ℹ️",
  "primary": "🔍",
  "warning": "⚠️",
  "danger": "🚫",
  "concept": "💡",
  "data": "📊",
  "code": "💻",
  "result": "✅",
  "note": "📝",
  "key": "🔑",
  "model": "🧮",
  "optimization": "⚙️",
  "analysis": "📈",
  "question": "❓",
  "time": "⏱️"
}

def info_box(content, title=None, kind="info", badge=None, icon=True):
    """Create an info box with styling."""
    inject_styles()
    
    html_title = f"<h4>{title}</h4>" if title else ""
    html_badge = f"<div class='badge'>{badge}</div>" if badge else ""
    
    # Get icon based on kind, default to empty string if not found
    icon_html = ""
    if icon and kind in ICONS:
        icon_html = f"{ICONS.get(kind, '')} "
    
    class_name = _KIND_CLASS.get(kind, "")
    return HTML(f"""
    <div class="box {class_name}">
      {html_badge}
      {html_title}
      {icon_html}{content}
      <div class="tone-fade"></div>
    </div>
    """)

def show_formula(formula):
    """Display a formula with special styling."""
    inject_styles()
    return HTML(f"""
    <div class="math-container">
      {formula}
    </div>
    """)

def concept_card(title, content):
    """Create a styled concept card."""
    inject_styles()
    return HTML(f"""
    <div class="concept-card">
      <h5>{ICONS.get('concept', '')} {title}</h5>
      {content}
    </div>
    """)

def create_timeline(*items):
    """Create a timeline with the given items."""
    inject_styles()
    items_html = ""
    for item in items:
        items_html += f"<div class='timeline-item'>{item}</div>"
    
    return HTML(f"""
    <div class="timeline">
      {items_html}
    </div>
    """)

def flex_columns(*contents):
    """Create flexible columns with the given contents."""
    inject_styles()
    items_html = ""
    for content in contents:
        items_html += f"<div class='flex-item'>{content}</div>"
    
    return HTML(f"""
    <div class="flex-container">
      {items_html}
    </div>
    """)

def section_block(title, content):
    """Create a section block with title."""
    inject_styles()
    return HTML(f"""
    <div class="section-block">
      <h3 class="section-title">{title}</h3>
      {content}
    </div>
    """)

def param_card(name, value, description=None):
    """Create a parameter card with name and value."""
    inject_styles()
    desc_html = f"<div>{description}</div>" if description else ""
    return HTML(f"""
    <div class="param-card">
      <span class="param-name">{name}</span>
      <span class="param-value">{value}</span>
      {desc_html}
    </div>
    """)

def key_insight(title, content):
    """Create a key insight box."""
    inject_styles()
    return HTML(f"""
    <div class="key-insight">
      <h5>{ICONS.get('key', '')} {title}</h5>
      {content}
    </div>
    """)

def plt_style():
    """Return a style dictionary for matplotlib that matches the box theme."""
    return {
        'figure.figsize': (10, 6),
        'figure.facecolor': PALETTE['bg-base'],
        'axes.facecolor': PALETTE['bg-base'],
        'axes.edgecolor': PALETTE['text'],
        'axes.labelcolor': PALETTE['text'],
        'axes.grid': True,
        'grid.color': PALETTE['chart-grid'],
        'xtick.color': PALETTE['text'],
        'ytick.color': PALETTE['text'],
        'text.color': PALETTE['text'],
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.prop_cycle': plt.cycler(color=PALETTE['series'])
    }

def setup_plot_style():
    """Apply the theme style to matplotlib."""
    plt.rcParams.update(plt_style())
    
def create_heatmap(data, xlabel, ylabel, title, cmap="viridis", annot=True):
    """Create a styled heatmap."""
    inject_styles()
    setup_plot_style()
    
    plt.figure(figsize=(12, 8))
    ax = sns.heatmap(data, cmap=cmap, annot=annot, fmt=".2f", 
                   linewidths=.5, cbar_kws={"shrink": .8},
                   annot_kws={"color": "white", "fontweight": "bold"})
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    return ax

def create_comparison_chart(data, x, y1, y2, labels, title, xlabel, ylabel):
    """Create a comparison bar chart."""
    inject_styles()
    setup_plot_style()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    x_pos = np.arange(len(data[x]))
    width = 0.35
    
    bars1 = ax.bar(x_pos - width/2, data[y1], width, label=labels[0], color=PALETTE['series'][0])
    bars2 = ax.bar(x_pos + width/2, data[y2], width, label=labels[1], color=PALETTE['series'][1])
    
    # Añadir valores encima de las barras
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{height:.1f}', ha='center', va='bottom', color='white')
    
    for bar in bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{height:.1f}', ha='center', va='bottom', color='white')
    
    ax.set_xticks(x_pos)
    ax.set_xticklabels(data[x], rotation=45, ha='right')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    
    plt.tight_layout()
    return fig, ax
