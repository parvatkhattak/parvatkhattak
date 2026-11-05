#!/usr/bin/env python3
"""Generate custom animated technical SVG icons, status badges, and dividers."""
import os

OUT = "assets/icons"
os.makedirs(OUT, exist_ok=True)


def write(name, content):
    path = os.path.join(OUT, name)
    with open(path, "w") as f:
        f.write(content.strip() + "\n")


# 1. Animated glowing gradient divider with moving telemetry pulse
write("divider.svg", """
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="14" viewBox="0 0 1000 14">
  <defs>
    <linearGradient id="lineGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0"/>
      <stop offset="20%" stop-color="#38bdf8" stop-opacity="0.45"/>
      <stop offset="50%" stop-color="#818cf8" stop-opacity="0.8"/>
      <stop offset="80%" stop-color="#c084fc" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#c084fc" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="beam" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0"/>
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="1"/>
      <stop offset="100%" stop-color="#c084fc" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <line x1="0" y1="7" x2="1000" y2="7" stroke="url(#lineGrad)" stroke-width="1.2"/>
  <rect y="5.5" width="140" height="3" rx="1.5" fill="url(#beam)">
    <animate attributeName="x" from="-140" to="1000" dur="4.5s" repeatCount="indefinite"/>
  </rect>
  <circle cx="500" cy="7" r="2.5" fill="#818cf8">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="2s" repeatCount="indefinite"/>
  </circle>
</svg>
""")

# 2. Section icon: Terminal prompt `>_` (About Me)
write("terminal.svg", """
<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24">
  <rect x="2" y="3" width="20" height="18" rx="3.5" fill="#111827" stroke="#38bdf8" stroke-width="1.6"/>
  <path d="M6.5 9L10.5 12L6.5 15" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="12.5" y="13.8" width="5" height="2" rx="0.8" fill="#818cf8">
    <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/>
  </rect>
</svg>
""")

# 3. Section icon: Experience (Animated timeline nodes)
write("timeline.svg", """
<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24">
  <line x1="6" y1="4" x2="6" y2="20" stroke="#818cf8" stroke-width="1.6" stroke-dasharray="2 2"/>
  <circle cx="6" cy="6" r="3" fill="#22c55e">
    <animate attributeName="r" values="2.5;4;2.5" dur="1.8s" repeatCount="indefinite"/>
  </circle>
  <rect x="11" y="4.5" width="10" height="3" rx="1.2" fill="#38bdf8" opacity="0.9"/>
  <circle cx="6" cy="12" r="2.5" fill="#818cf8"/>
  <rect x="11" y="10.5" width="8" height="3" rx="1.2" fill="#818cf8" opacity="0.75"/>
  <circle cx="6" cy="18" r="2.5" fill="#c084fc"/>
  <rect x="11" y="16.5" width="6" height="3" rx="1.2" fill="#c084fc" opacity="0.6"/>
</svg>
""")

# 4. Section icon: Featured Projects (Animated orbiting cube / core)
write("projects.svg", """
<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24">
  <g transform="translate(12,12)">
    <polygon points="0,-8 7,-4 7,4 0,8 -7,4 -7,-4" fill="#111827" stroke="#38bdf8" stroke-width="1.6"/>
    <polyline points="-7,-4 0,0 7,-4" fill="none" stroke="#818cf8" stroke-width="1.4"/>
    <line x1="0" y1="0" x2="0" y2="8" stroke="#818cf8" stroke-width="1.4"/>
    <circle cx="0" cy="0" r="2.2" fill="#c084fc">
      <animate attributeName="r" values="1.6;3;1.6" dur="2s" repeatCount="indefinite"/>
    </circle>
    <g>
      <circle cx="0" cy="-10" r="1.5" fill="#38bdf8"/>
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="5s" repeatCount="indefinite"/>
    </g>
  </g>
</svg>
""")

# 5. Section icon: Tech Stack (Microchip / AI processor with pulsing pins)
write("stack.svg", """
<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24">
  <g stroke="#38bdf8" stroke-width="1.6" stroke-linecap="round">
    <line x1="9" y1="2" x2="9" y2="5"/><line x1="15" y1="2" x2="15" y2="5"/>
    <line x1="9" y1="19" x2="9" y2="22"/><line x1="15" y1="19" x2="15" y2="22"/>
    <line x1="2" y1="9" x2="5" y2="9"/><line x1="2" y1="15" x2="5" y2="15"/>
    <line x1="19" y1="9" x2="22" y2="9"/><line x1="19" y1="15" x2="22" y2="15"/>
  </g>
  <rect x="5" y="5" width="14" height="14" rx="2.5" fill="#111827" stroke="#818cf8" stroke-width="1.6"/>
  <rect x="8.5" y="8.5" width="7" height="7" rx="1.2" fill="#c084fc">
    <animate attributeName="opacity" values="0.45;1;0.45" dur="1.8s" repeatCount="indefinite"/>
  </rect>
</svg>
""")

# 6. Section icon: Achievements (Pulsing star / rank beacon)
write("achievements.svg", """
<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24">
  <circle cx="12" cy="12" r="9" fill="none" stroke="#f59e0b" stroke-width="1.2" stroke-dasharray="3 3">
    <animateTransform attributeName="transform" type="rotate" from="0 12 12" to="360 12 12" dur="8s" repeatCount="indefinite"/>
  </circle>
  <polygon points="12,4.5 14.2,9.2 19.3,9.9 15.6,13.5 16.5,18.6 12,16.1 7.5,18.6 8.4,13.5 4.7,9.9 9.8,9.2" fill="#fbbf24" stroke="#f59e0b" stroke-width="1">
    <animate attributeName="opacity" values="0.75;1;0.75" dur="2s" repeatCount="indefinite"/>
  </polygon>
</svg>
""")

# 7. Section icon: GitHub Stats (Animated telemetry bars)
write("stats-icon.svg", """
<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24">
  <rect x="3" y="12" width="4" height="8" rx="1" fill="#38bdf8">
    <animate attributeName="y" values="14;7;14" dur="1.6s" repeatCount="indefinite"/>
    <animate attributeName="height" values="6;13;6" dur="1.6s" repeatCount="indefinite"/>
  </rect>
  <rect x="10" y="6" width="4" height="14" rx="1" fill="#818cf8">
    <animate attributeName="y" values="6;13;6" dur="1.6s" repeatCount="indefinite"/>
    <animate attributeName="height" values="14;7;14" dur="1.6s" repeatCount="indefinite"/>
  </rect>
  <rect x="17" y="9" width="4" height="11" rx="1" fill="#c084fc">
    <animate attributeName="y" values="11;4;11" dur="1.6s" repeatCount="indefinite"/>
    <animate attributeName="height" values="9;16;9" dur="1.6s" repeatCount="indefinite"/>
  </rect>
</svg>
""")

# 8. Section icon: Connect (Signal radar waves)
write("signal.svg", """
<svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24">
  <circle cx="12" cy="12" r="2.5" fill="#38bdf8"/>
  <circle cx="12" cy="12" r="4" fill="none" stroke="#38bdf8" stroke-width="1.6">
    <animate attributeName="r" values="3;10" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle cx="12" cy="12" r="4" fill="none" stroke="#818cf8" stroke-width="1.6">
    <animate attributeName="r" values="3;10" dur="2s" begin="1s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0" dur="2s" begin="1s" repeatCount="indefinite"/>
  </circle>
</svg>
""")

# 9. Experience table status indicators (Active pulse vs completed node)
write("pulse-live.svg", """
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="3.5" fill="#22c55e"/>
  <circle cx="8" cy="8" r="3.5" fill="none" stroke="#22c55e" stroke-width="1.5">
    <animate attributeName="r" values="3.5;7.2" dur="1.6s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.9;0" dur="1.6s" repeatCount="indefinite"/>
  </circle>
</svg>
""")

write("pulse-node.svg", """
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="3" fill="#818cf8">
    <animate attributeName="opacity" values="0.5;1;0.5" dur="2.4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="8" cy="8" r="5.5" fill="none" stroke="#818cf8" stroke-opacity="0.35" stroke-width="1"/>
</svg>
""")

# 10. Project card icons (6 featured projects)
# Medical RAG: ECG pulse line
write("proj-medical.svg", """
<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24">
  <rect x="2" y="3" width="20" height="18" rx="3" fill="#111827" stroke="#f43f5e" stroke-width="1.5"/>
  <polyline points="4,12 8,12 10,7 13,17 15,10 17,12 20,12" fill="none" stroke="#f43f5e" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="30" stroke-dashoffset="30">
    <animate attributeName="stroke-dashoffset" values="30;0;0" dur="2.2s" repeatCount="indefinite"/>
  </polyline>
</svg>
""")

# Retail Forecasting: rising trend line + pulsing point
write("proj-forecast.svg", """
<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24">
  <rect x="2" y="3" width="20" height="18" rx="3" fill="#111827" stroke="#22c55e" stroke-width="1.5"/>
  <polyline points="5,16 10,12 14,14 19,7" fill="none" stroke="#22c55e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="19" cy="7" r="2.2" fill="#4ade80">
    <animate attributeName="r" values="1.6;3.2;1.6" dur="1.5s" repeatCount="indefinite"/>
  </circle>
</svg>
""")

# Periyar OCR / Document pipeline: scanning laser over document
write("proj-scan.svg", """
<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24">
  <rect x="4" y="2.5" width="16" height="19" rx="2.5" fill="#111827" stroke="#10b981" stroke-width="1.5"/>
  <line x1="7.5" y1="7" x2="16.5" y2="7" stroke="#475569" stroke-width="1.4" stroke-linecap="round"/>
  <line x1="7.5" y1="11" x2="16.5" y2="11" stroke="#475569" stroke-width="1.4" stroke-linecap="round"/>
  <line x1="7.5" y1="15" x2="13.5" y2="15" stroke="#475569" stroke-width="1.4" stroke-linecap="round"/>
  <line x1="5" y1="6" x2="19" y2="6" stroke="#34d399" stroke-width="1.8">
    <animate attributeName="y1" values="5;18;5" dur="2.4s" repeatCount="indefinite"/>
    <animate attributeName="y2" values="5;18;5" dur="2.4s" repeatCount="indefinite"/>
  </line>
</svg>
""")

# Faceometry: 3D mesh wireframe nodes
write("proj-vision.svg", """
<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24">
  <polygon points="12,2.5 20,7 20,17 12,21.5 4,17 4,7" fill="#111827" stroke="#38bdf8" stroke-width="1.5"/>
  <line x1="4" y1="7" x2="20" y2="17" stroke="#38bdf8" stroke-opacity="0.45" stroke-width="1"/>
  <line x1="20" y1="7" x2="4" y2="17" stroke="#38bdf8" stroke-opacity="0.45" stroke-width="1"/>
  <line x1="12" y1="2.5" x2="12" y2="21.5" stroke="#38bdf8" stroke-opacity="0.45" stroke-width="1"/>
  <circle cx="12" cy="12" r="2.4" fill="#38bdf8">
    <animate attributeName="r" values="1.6;3.2;1.6" dur="1.8s" repeatCount="indefinite"/>
  </circle>
</svg>
""")

# RL Agent (Mario DDQN): state-action loop
write("proj-rl.svg", """
<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24">
  <circle cx="12" cy="12" r="8.5" fill="#111827" stroke="#f59e0b" stroke-width="1.6" stroke-dasharray="8 4">
    <animateTransform attributeName="transform" type="rotate" from="0 12 12" to="360 12 12" dur="4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="12" cy="12" r="3" fill="#fbbf24">
    <animate attributeName="opacity" values="0.5;1;0.5" dur="1.5s" repeatCount="indefinite"/>
  </circle>
</svg>
""")

# Agentic Chatbot (LangGraph): multi-node state graph with flowing edge
write("proj-agent.svg", """
<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24">
  <line x1="6" y1="6" x2="18" y2="6" stroke="#818cf8" stroke-width="1.5"/>
  <line x1="6" y1="6" x2="12" y2="18" stroke="#818cf8" stroke-width="1.5"/>
  <line x1="18" y1="6" x2="12" y2="18" stroke="#818cf8" stroke-width="1.5"/>
  <circle cx="6" cy="6" r="3" fill="#38bdf8">
    <animate attributeName="r" values="2.5;3.6;2.5" dur="1.8s" repeatCount="indefinite"/>
  </circle>
  <circle cx="18" cy="6" r="3" fill="#818cf8">
    <animate attributeName="r" values="2.5;3.6;2.5" dur="1.8s" begin="0.6s" repeatCount="indefinite"/>
  </circle>
  <circle cx="12" cy="18" r="3" fill="#c084fc">
    <animate attributeName="r" values="2.5;3.6;2.5" dur="1.8s" begin="1.2s" repeatCount="indefinite"/>
  </circle>
</svg>
""")

print("Generated", len(os.listdir(OUT)), "animated SVG icons in", OUT)
