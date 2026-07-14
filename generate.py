import random
import urllib.request
import json

W = 900
H = 430

username = "sumsh123"

try:
    url = f"https://api.github.com/users/{username}/repos?per_page=100"
    data = urllib.request.urlopen(url).read()
    repos = json.loads(data)
    PROJECT_COUNT = len(repos)

except:
    PROJECT_COUNT = 12


nodes = [
    (170,150),
    (170,240),
    (280,110),
    (280,190),
    (280,270),
    (620,110),
    (620,190),
    (620,270),
    (730,150),
    (730,240)
]


svg = f"""<svg width="{W}" height="{H}"
xmlns="http://www.w3.org/2000/svg">

<defs>

<radialGradient id="background">
<stop stop-color="#260033"/>
<stop offset="1" stop-color="#050006"/>
</radialGradient>

<radialGradient id="reactor">
<stop stop-color="white"/>
<stop offset=".25" stop-color="#ffd6f5"/>
<stop offset=".6" stop-color="#ff4fd8"/>
<stop offset="1" stop-color="#7b00ff"/>
</radialGradient>

<filter id="glow">
<feGaussianBlur stdDeviation="9"/>
</filter>

</defs>


<rect width="100%"
height="100%"
fill="url(#background)"/>

"""


# particles

for i in range(90):

    x = random.randint(0,W)
    y = random.randint(0,H)

    svg += f"""
<circle cx="{x}"
cy="{y}"
r="{random.choice([1,2])}"
fill="#ffb6ed">

<animate
attributeName="opacity"
values="0.15;1;0.15"
dur="{random.randint(2,6)}s"
repeatCount="indefinite"/>

</circle>
"""


# title

svg += """

<text x="45"
y="55"
font-family="Consolas, monospace"
font-size="28"
font-weight="600"
letter-spacing="2"
fill="white">

Summaiya's AI Lab

</text>


<text x="48"
y="82"
font-family="Consolas, monospace"
font-size="12"
letter-spacing="3"
fill="#ff8ee8">

AI • MACHINE LEARNING • CREATIVE SYSTEMS

</text>



<!-- Neural Network -->

<g stroke="#ff4fd8"
stroke-width="1.5"
opacity="0.45">

"""


for a in nodes:
    for b in nodes:

        if random.random() < 0.18:

            svg += f"""
<line x1="{a[0]}"
y1="{a[1]}"
x2="{b[0]}"
y2="{b[1]}">

<animate
attributeName="opacity"
values="0.2;0.8;0.2"
dur="3s"
repeatCount="indefinite"/>

</line>
"""


svg += "</g>"


for x,y in nodes:

    svg += f"""

<circle cx="{x}"
cy="{y}"
r="7"
fill="#ffb6ed">

<animate
attributeName="r"
values="6;10;6"
dur="2s"
repeatCount="indefinite"/>

</circle>

"""


# core

svg += """

<a href="https://github.com/sumsh123">


<circle cx="450"
cy="205"
r="120"
fill="#ff4fd8"
opacity=".15"
filter="url(#glow)">

<animate
attributeName="r"
values="100;140;100"
dur="3s"
repeatCount="indefinite"/>

</circle>


<circle cx="450"
cy="205"
r="90"
fill="none"
stroke="#ff4fd8"
stroke-width="2">

<animateTransform
attributeName="transform"
type="rotate"
from="0 450 205"
to="360 450 205"
dur="10s"
repeatCount="indefinite"/>

</circle>


<circle cx="450"
cy="205"
r="65"
fill="none"
stroke="white"
opacity=".5">


<animateTransform
attributeName="transform"
type="rotate"
from="360 450 205"
to="0 450 205"
dur="7s"
repeatCount="indefinite"/>


</circle>



<circle cx="450"
cy="205"
r="48"
fill="url(#reactor)">


<animate
attributeName="r"
values="42;58;42"
dur="2s"
repeatCount="indefinite"/>


</circle>



<circle cx="450"
cy="205"
r="13"
fill="white"/>


</a>



<text x="45"
y="345"
font-family="Consolas, monospace"
font-size="15"
fill="white">

&gt; PROJECTS LOADED: """


svg += str(PROJECT_COUNT)


svg += """

</text>



<text x="45"
y="380"
font-family="Consolas, monospace"
font-size="15"
fill="#ff4fd8">

&gt; STATUS: EVOLVING

</text>



<text x="650"
y="380"
font-family="Consolas, monospace"
font-size="12"
fill="#ffb6ed">

CLICK THE CORE

</text>


</svg>
"""


with open(
    "output/neural-core.svg",
    "w",
    encoding="utf-8"
) as file:

    file.write(svg)


print("Summaiya's AI Lab generated!")