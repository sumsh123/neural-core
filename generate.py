import random
from datetime import datetime

WIDTH = 800
HEIGHT = 300

nodes = [
    (150,120),(150,180),
    (250,100),(250,150),(250,200),
    (550,100),(550,150),(550,200),
    (650,120),(650,180)
]

svg = f"""
<svg width="{WIDTH}" height="{HEIGHT}"
xmlns="http://www.w3.org/2000/svg">


<defs>

<filter id="glow">
<feGaussianBlur stdDeviation="5" result="blur"/>
<feMerge>
<feMergeNode in="blur"/>
<feMergeNode in="SourceGraphic"/>
</feMerge>
</filter>


<radialGradient id="core">
<stop offset="0%" stop-color="#ffffff"/>
<stop offset="40%" stop-color="#ff4fd8"/>
<stop offset="100%" stop-color="#7209b7"/>
</radialGradient>


</defs>



<rect width="100%" height="100%" fill="#070011"/>



<!-- grid -->

<g stroke="#24104a" opacity="0.5">

"""

for x in range(0, WIDTH, 40):
    svg += f'<line x1="{x}" y1="0" x2="{x}" y2="{HEIGHT}"/>'

for y in range(0, HEIGHT, 40):
    svg += f'<line x1="0" y1="{y}" x2="{WIDTH}" y2="{y}"/>'

svg += """

</g>



<text x="35" y="45"
font-family="monospace"
font-size="30"
fill="#ff4fd8">

NEURAL CORE // ONLINE

</text>


<text x="35" y="75"
font-family="monospace"
font-size="15"
fill="white">

AI SYSTEM SIMULATION

</text>



<!-- connections -->

<g stroke="#00ffff" opacity="0.45">

"""


for a in nodes:
    for b in nodes:
        if random.random() < 0.18:
            svg += f"""
            <line x1="{a[0]}" y1="{a[1]}"
            x2="{b[0]}" y2="{b[1]}"/>
            """


svg += "</g>"


# nodes

for x,y in nodes:
    svg += f"""
    <circle cx="{x}" cy="{y}"
    r="10"
    fill="#ff4fd8"
    filter="url(#glow)"/>
    """


# AI CORE

svg += """

<circle cx="400" cy="150"
r="45"
fill="url(#core)"
filter="url(#glow)">

<animate attributeName="r"
values="40;48;40"
dur="2s"
repeatCount="indefinite"/>

</circle>



<text x="380" y="155"
font-family="monospace"
font-size="18"
fill="#070011">

AI

</text>



<text x="35" y="250"
font-family="monospace"
font-size="16"
fill="#00ffff">

STATUS: LEARNING

</text>



<text x="35" y="275"
font-family="monospace"
font-size="14"
fill="white">

LOSS: 0.0321 ↓   ACCURACY: 98.7%

</text>



<text x="570" y="275"
font-family="monospace"
font-size="12"
fill="#ff4fd8">

UPDATED """

svg += datetime.now().strftime("%Y-%m-%d")

svg += """

</text>


</svg>
"""


with open(
"output/neural-core.svg",
"w",
encoding="utf-8"
) as f:

    f.write(svg)


print("Neural Core v2 generated!")