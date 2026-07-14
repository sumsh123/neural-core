import random
from datetime import datetime

WIDTH = 700
HEIGHT = 260

neurons = []

for i in range(12):
    neurons.append({
        "x": random.randint(120,580),
        "y": random.randint(90,180)
    })


models = random.randint(5,20)
projects = random.randint(4,15)
accuracy = round(random.uniform(95,99.9),2)
loss = round(random.uniform(0.01,0.08),4)


svg = f"""
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">

<rect width="100%" height="100%" fill="#080014"/>


<text x="30" y="45"
font-size="28"
font-family="monospace"
fill="#ff4fd8">
NEURAL CORE
</text>


<text x="30" y="72"
font-size="14"
font-family="monospace"
fill="white">
AI LAB SIMULATION
</text>



<!-- connections -->
<g stroke="#6c63ff" opacity="0.5">
"""

for a in neurons:
    for b in neurons:
        if random.random() < 0.15:
            svg += f"""
            <line x1="{a['x']}" y1="{a['y']}"
            x2="{b['x']}" y2="{b['y']}"/>
            """


svg += "</g>"


# neurons
for n in neurons:
    svg += f"""
    <circle cx="{n['x']}"
    cy="{n['y']}"
    r="9"
    fill="#ff4fd8"/>
    """


svg += f"""

<circle cx="350" cy="135" r="25"
fill="#7df9ff"/>


<text x="330" y="140"
font-family="monospace"
font-size="12"
fill="#080014">
AI
</text>



<text x="30" y="225"
font-family="monospace"
font-size="15"
fill="#7df9ff">

MODELS TRAINED: {models}

</text>


<text x="250" y="225"
font-family="monospace"
font-size="15"
fill="#7df9ff">

PROJECTS: {projects}

</text>


<text x="450" y="225"
font-family="monospace"
font-size="15"
fill="white">

ACC: {accuracy}%

</text>



<text x="30" y="250"
font-family="monospace"
font-size="12"
fill="white">

LOSS: {loss} ↓ | UPDATED {datetime.now().strftime("%Y-%m-%d")}

</text>


</svg>
"""


with open("output/neural-core.svg","w", encoding="utf-8") as file:
    file.write(svg)


print("Neural Core generated!")