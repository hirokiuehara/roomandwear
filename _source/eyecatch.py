# -*- coding: utf-8 -*-
"""Original eyecatch SVG illustrations for ROOM & WEAR."""
import html

ICON_OF = {
 "basic-5-items":"hanger","winter-outer-guide":"jacket","white-tee-guide":"tshirt","first-sneakers":"sneaker",
 "clothes-care":"washer","1k-layout":"floor","desk-setup":"desk","indirect-lighting":"lamp",
 "bedding-guide":"bed","small-room-storage":"box",
}

S = 'fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"'
ICONS = {
"tshirt": f'<path {S} d="M-55,-60 L-20,-75 Q0,-58 20,-75 L55,-60 L80,-25 L55,-12 L50,-30 L50,75 L-50,75 L-50,-30 L-55,-12 L-80,-25 Z"/>',
"jacket": f'<path {S} d="M-30,-75 L0,-40 L30,-75 L60,-62 L85,40 L60,45 L55,0 L55,80 L-55,80 L-55,0 L-60,45 L-85,40 L-60,-62 Z"/><path {S} d="M0,-40 L0,80 M-30,-75 L-15,10 M30,-75 L15,10"/><circle cx="8" cy="20" r="3" fill="#fff"/><circle cx="8" cy="45" r="3" fill="#fff"/>',
"knit": f'<path {S} d="M-55,-60 L-25,-72 Q0,-55 25,-72 L55,-60 L85,30 L62,38 L50,-15 L50,78 L-50,78 L-50,-15 L-62,38 L-85,30 Z"/><path {S} d="M-50,60 L50,60 M-20,-10 L-10,0 L0,-10 L10,0 L20,-10 M-20,15 L-10,25 L0,15 L10,25 L20,15"/>',
"hoodie": f'<path {S} d="M-55,-45 L-30,-58 Q-30,-90 0,-90 Q30,-90 30,-58 L55,-45 L82,35 L60,42 L50,-5 L50,80 L-50,80 L-50,-5 L-60,42 L-82,35 Z"/><path {S} d="M-30,-58 Q0,-30 30,-58 M-30,40 L30,40 L30,65 L-30,65 Z M-8,-40 L-8,-15 M8,-40 L8,-15"/>',
"shirt": f'<path {S} d="M-55,-60 L-22,-75 L0,-50 L22,-75 L55,-60 L80,40 L58,45 L50,0 L50,80 L-50,80 L-50,0 L-58,45 L-80,40 Z"/><path {S} d="M0,-50 L0,80 M-22,-75 L-12,-48 L0,-50 L12,-48 L22,-75"/><circle cx="7" cy="-20" r="3" fill="#fff"/><circle cx="7" cy="10" r="3" fill="#fff"/><circle cx="7" cy="40" r="3" fill="#fff"/>',
"pants": f'<path {S} d="M-45,-80 L45,-80 L55,85 L15,85 L0,-20 L-15,85 L-55,85 Z"/><path {S} d="M-45,-62 L45,-62 M-28,-62 L-35,-30 M28,-62 L35,-30"/>',
"sneaker": f'<path {S} d="M-90,30 L-85,-20 Q-60,-25 -45,-50 L-15,-50 Q0,-20 40,-10 Q85,0 90,30 Z"/><path {S} d="M-92,30 L92,30 L90,48 L-90,48 Z M-40,-35 L-20,-25 M-35,-20 L-12,-12 M-28,-5 L-5,2"/>',
"shoe": f'<path {S} d="M-90,30 Q-92,-15 -70,-25 L-40,-25 Q-20,-10 20,-5 Q80,0 90,25 L90,35 L-90,35 Z"/><path {S} d="M-90,35 L90,35 M30,-4 Q40,15 30,35 M-70,-25 L-70,35"/>',
"bag": f'<path {S} d="M-75,-30 L75,-30 L70,75 L-70,75 Z"/><path {S} d="M-35,-30 Q-35,-80 0,-80 Q35,-80 35,-30 M-75,10 L75,10 M-10,10 L-10,25 L10,25 L10,10"/>',
"watch": f'<circle {S} cx="0" cy="0" r="48"/><path {S} d="M-30,-38 L-25,-90 L25,-90 L30,-38 M-30,38 L-25,90 L25,90 L30,38 M0,0 L0,-30 M0,0 L22,12"/><circle cx="0" cy="0" r="4" fill="#fff"/>',
"cap": f'<path {S} d="M-70,15 Q-70,-65 0,-65 Q70,-65 70,15 Z"/><path {S} d="M-70,15 Q-10,10 70,15 Q100,25 105,45 Q20,35 -70,15 M0,-65 L0,15 M-35,-58 L-20,12 M35,-58 L20,12"/><circle cx="0" cy="-67" r="5" fill="#fff"/>',
"hanger": f'<path {S} d="M0,-45 Q0,-80 22,-80 Q40,-80 38,-62 Q36,-50 0,-45 L-90,30 Q-95,40 -82,40 L82,40 Q95,40 90,30 L0,-45"/>',
"sofa": f'<path {S} d="M-70,-40 L70,-40 L70,10 L-70,10 Z M-95,-15 L-70,-15 L-70,45 L-95,45 Z M70,-15 L95,-15 L95,45 L70,45 Z M-70,10 L70,10 L70,45 L-70,45 M-80,45 L-80,65 M80,45 L80,65 M0,-40 L0,10"/>',
"lamp": f'<path {S} d="M-45,-30 L-25,-85 L25,-85 L45,-30 Z M0,-30 L0,70 M-40,75 L40,75"/><path stroke="#fff" stroke-width="3" stroke-dasharray="4 8" fill="none" d="M-60,-10 L-80,20 M60,-10 L80,20 M0,-15 L0,-15"/>',
"desk": f'<path {S} d="M-95,10 L95,10 M-85,10 L-85,80 M85,10 L85,80 M-45,-70 L45,-70 L45,-10 L-45,-10 Z M0,-10 L0,10 M-20,10 L20,10"/><path {S} d="M55,10 L55,-25 Q55,-35 65,-35 L75,-35"/>',
"bed": f'<path {S} d="M-95,-40 L-95,60 M95,10 L95,60 M-95,10 L95,10 M-95,35 L95,35 M-85,-10 L-35,-10 L-35,10 L-85,10 Z M-30,-10 Q40,-25 95,10"/>',
"box": f'<path {S} d="M-70,-40 L70,-40 L70,70 L-70,70 Z M-80,-60 L80,-60 L80,-40 L-80,-40 Z M-20,0 L20,0"/>',
"floor": f'<path {S} d="M-85,-70 L85,-70 L85,70 L-85,70 Z M-85,10 L-20,10 L-20,70 M20,-70 L20,-20 L85,-20 M-60,-45 L-20,-45 L-20,-20 L-60,-20 Z"/><path stroke="#fff" stroke-width="3" fill="none" d="M-20,40 A30,30 0 0 1 10,70"/>',
"curtain": f'<path {S} d="M-95,-80 L95,-80 M-80,-80 Q-70,0 -85,80 L-25,80 Q-35,0 -20,-80 M80,-80 Q70,0 85,80 L25,80 Q35,0 20,-80"/><path stroke="#fff" stroke-width="3" fill="none" d="M-15,-70 L15,-70 L15,70 L-15,70 Z"/>',
"rug": f'<path {S} d="M-90,-50 L90,-50 L90,50 L-90,50 Z M-70,-30 L70,-30 L70,30 L-70,30 Z"/><path stroke="#fff" stroke-width="3" fill="none" d="M-90,-50 L-100,-50 M-90,-30 L-100,-30 M-90,-10 L-100,-10 M-90,10 L-100,10 M-90,30 L-100,30 M-90,50 L-100,50 M90,-50 L100,-50 M90,-30 L100,-30 M90,-10 L100,-10 M90,10 L100,10 M90,30 L100,30 M90,50 L100,50"/>',
"plant": f'<path {S} d="M-35,30 L35,30 L25,85 L-25,85 Z M0,30 L0,-30 M0,0 Q-50,-5 -55,-50 Q-10,-45 0,0 M0,-15 Q45,-20 55,-70 Q10,-65 0,-15 M0,-30 Q-15,-70 0,-90 Q15,-70 0,-30"/>',
"table": f'<path {S} d="M-95,-10 L95,-10 L95,5 L-95,5 Z M-80,5 L-80,60 M80,5 L80,60 M-80,35 L80,35"/><path {S} d="M-30,-10 L-30,-35 Q-30,-45 -20,-45 L-5,-45 M30,-30 L50,-30 L50,-10"/>',
"closet": f'<path {S} d="M-90,-70 L90,-70 M-75,-70 L-75,-60 M-75,-60 Q-75,-50 -95,-35 L-55,-35 Q-75,-50 -75,-60"/><path {S} d="M-25,-70 L-25,-60 M-25,-60 Q-25,-50 -45,-35 L-45,40 L-5,40 L-5,-35 Q-25,-50 -25,-60 M25,-70 L25,-60 M25,-60 Q25,-50 5,-35 L5,70 L45,70 L45,-35 Q25,-50 25,-60"/><path {S} d="M60,30 L95,30 L95,80 L60,80 Z M60,55 L95,55"/>',
"pot": f'<path {S} d="M-70,-20 L70,-20 L60,60 Q58,70 48,70 L-48,70 Q-58,70 -60,60 Z M-90,-20 L90,-20 M-90,-20 L-90,-5 M90,-20 L90,-5 M-30,-35 Q-30,-50 0,-50 Q30,-50 30,-35"/><path stroke="#fff" stroke-width="3" fill="none" d="M-25,-65 Q-15,-75 -25,-85 M0,-60 Q10,-72 0,-85 M25,-65 Q35,-75 25,-85"/>',
"humidifier": f'<path {S} d="M-45,-40 Q-45,-55 -30,-55 L30,-55 Q45,-55 45,-40 L50,75 L-50,75 Z M-50,40 L50,40"/><circle {S} cx="0" cy="58" r="8"/><path stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round" d="M-15,-65 Q-25,-80 -15,-95 M0,-65 Q10,-82 0,-100 M15,-65 Q25,-80 15,-95"/>',
"frame": f'<path {S} d="M-80,-60 L80,-60 L80,60 L-80,60 Z M-62,-42 L62,-42 L62,42 L-62,42 Z M0,-60 L0,-60"/><path {S} d="M-50,30 L-15,-10 L10,15 L25,0 L50,30 Z"/><circle cx="30" cy="-20" r="8" fill="#fff"/><path {S} d="M-20,-60 L0,-85 L20,-60"/>',
"washer": f'<path {S} d="M-65,-85 L65,-85 L65,85 L-65,85 Z M-65,-50 L65,-50"/><circle {S} cx="0" cy="18" r="45"/><path {S} d="M-30,25 Q-15,10 0,25 Q15,40 30,25"/><circle cx="-40" cy="-68" r="5" fill="#fff"/><circle cx="-20" cy="-68" r="5" fill="#fff"/>',
"door": f'<path {S} d="M-55,-85 L55,-85 L55,85 L-55,85 Z M-35,-65 L35,-65 L35,85"/><circle cx="20" cy="10" r="5" fill="#fff"/><path {S} d="M-95,85 L95,85 M65,60 L95,60 L95,85 M-95,70 L-75,70 L-75,85"/>',
}

def wrap(t, n=15):
    lines, cur = [], ""
    for ch in t:
        cur += ch
        if (len(cur) >= n - 3 and ch in "、・）」？ ") or len(cur) >= n:
            lines.append(cur); cur = ""
    if cur:
        if lines and len(cur) <= 2: lines[-1] += cur
        else: lines.append(cur)
    return lines[:3]

def svg(a, cat_label):
    icon = a.get("icon") or ICON_OF.get(a["slug"], "box")
    if a["cat"] == "apparel":
        c1, c2, acc = "#2a2724", "#4a453d", "#b08a5e"
    else:
        c1, c2, acc = "#454a2f", "#6b6f4d", "#9a7550"
    title = a["title"].split("。")[0]
    lines = wrap(title, 14)
    ty = 215
    tl = "".join(f'<text x="560" y="{ty + i*52}" font-size="40" font-weight="700" fill="#fff" font-family="Hiragino Sans, Noto Sans JP, Meiryo, sans-serif">{html.escape(l)}</text>' for i, l in enumerate(lines))
    en = "APPAREL" if a["cat"] == "apparel" else "INTERIOR"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>
<rect width="1200" height="630" fill="url(#g)"/>
<circle cx="280" cy="315" r="200" fill="#ffffff" fill-opacity="0.08"/>
<circle cx="280" cy="315" r="150" fill="#ffffff" fill-opacity="0.06"/>
<g transform="translate(280,315) scale(1.55)">{ICONS[icon]}</g>
<rect x="560" y="110" width="{len(en)*16+40}" height="40" rx="3" fill="{acc}"/>
<text x="580" y="138" font-size="20" letter-spacing="4" fill="#fff" font-family="Georgia, serif">{en}</text>
{tl}
<line x1="560" y1="{ty + len(lines)*52 - 10}" x2="640" y2="{ty + len(lines)*52 - 10}" stroke="{acc}" stroke-width="4"/>
<text x="560" y="560" font-size="26" letter-spacing="6" fill="#fff" fill-opacity="0.85" font-family="Georgia, serif" font-weight="700">ROOM &amp; WEAR</text>
</svg>'''
