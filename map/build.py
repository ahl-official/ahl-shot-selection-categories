# Builds the shot-category mind map pages (HTML) from the editors' folder PDFs + Mohit's WhatsApp list.
# Item markers: "+text" = new from Mohit (22 Nov), "?text" = needs an answer. Section gb=True = judged Good/Bad.
import json, html, pathlib
OUT = pathlib.Path(__file__).parent

P = {}
P["topper"] = dict(brand="Alchemane", name="Hair Topper", colour="#2a9d8f", src="Alchemane_Topper_Folder_Structure PDF", sections=[
  dict(name="Before", sub="hair-loss area", gb=True, groups=[(None, ["Crown area","Back area","Front area","Side area","360° view","Low confidence","Sad face / unhappy reaction"]),
                                                                 ("Conditions", ["+Alopecia"])]),
  dict(name="Customization", groups=[(None, ["Colour matching with swatches","Texture","?Size","Hair-loss area measurement","Topper","Topper size measurement (5×3, 5×6, 5×9)","Clips"])]),
  dict(name="Types of topper", groups=[(None, ["Silk base","Net base","Topper with hairline"])]),
  dict(name="Process", groups=[(None, ["Client self-wearing","Vinitt sir applying","Technician applying","Client showing topper","Client combing natural hair + topper","Client removing topper herself"])]),
  dict(name="After", sub="wearing topper", gb=True, star=True, groups=[(None, ["★ Natural hairline from front","Blending with natural hair","Parting","Smiling shot","Confidence shot","Family reaction"]),
                                                                  ("Hairstyle", ["+Middle parting","+Side parting","+Brush back"]),
                                                                  ("Reactions", ["+Happy","+Laughing","+Happy tears","+Family reactions"])]),
  dict(name="Age category", groups=[(None, ["18–30","30–40","40–50","50+"])]),
])
P["clipon"] = dict(brand="American Hairline", name="Clip-On Patch", colour="#2f6fd0", src="American_Hairline_Clip_On_Review_Draft PDF", sections=[
  dict(name="Before", gb=True, groups=[("Emotion (no good/bad)", ["Nervous shot","Low confidence","Mirror shot","Photo-conscious client"]),
                                     ("Hair area · good/bad", ["Front hair","Crown hair","Side hair","Back hair"]),
                                     ("New from Mohit", ["+Client entry shot","+Phone scrolling","+Client showing old hair photos"])]),
  dict(name="Customization", groups=[(None, ["Texture","Density","Volume","Colour match with swatches","3D scanning","Red light","Scalp check","Mold taking","Base customization book"])]),
  dict(name="Process", groups=[("Self-wearing", ["Wearing","Removing","Front angle","Back angle","Side angle"]),
                               ("Applying", ["Technician applying","Vinitt sir applying"]),
                               ("Hair trim", ["Hair trim shots"])]),
  dict(name="Removing process", new=True, groups=[(None, ["+Cleaning","+Washing head","+Drying"])]),
  dict(name="After", gb=True, star=True, groups=[(None, ["Front hairline","Side shots / side blending","Hair volume","Hair blending","Hair styling"]),
                                              ("Hairstyle", ["+Middle parting","+Side parting","+Brush back"]),
                                              ("Reactions", ["+Happy","+Laughing","+Happy tears","+Family reactions"])]),
  dict(name="Age category", groups=[(None, ["18–30","30–40","40–50","50+"])]),
])
P["stickon"] = dict(brand="American Hairline", name="Stick-On Patch", colour="#1d3f72", src="American_Hairline_Stick_On_Folder_Structure PDF", sections=[
  dict(name="Before", gb=True, groups=[("Emotion & mirror", ["Nervous","Demotivated","Low confidence","Mirror shots"]),
                                     ("Hair-loss area · good/bad", ["Crown area","Temple receding","Front hair","Back density","Side density"]),
                                     ("Extra", ["What is nape area"]),
                                     ("Conditions", ["+Alopecia","Patches alopecia","Half alopecia"]),
                                     ("New from Mohit", ["+Client entry shot","+Phone scrolling","+Client showing old hair photos"])]),
  dict(name="Consultation", new=True, groups=[(None, ["+Before online consultation"])]),
  dict(name="Customization", groups=[(None, ["Measurement","Red light","Customization book","Making of hairline","Colour blending with swatches","Mold taking","+Knotting hair","+Bleached knots"])]),
  dict(name="Process", groups=[(None, ["Applying scalp protector","Applying glue on scalp","Removing tape from system","Applying system to scalp","Hair cutting of system","Hair styling"])]),
  dict(name="Removing process", new=True, groups=[(None, ["+Cleaning","+Washing head","+Drying"])]),
  dict(name="After", gb=True, star=True, groups=[("Hairline, styling, blending · good/bad", ["Front hairline","Styling","Back blending","Side blending","After shot","+Whorl area"]),
                                              ("Happy faces", ["Smiling","Confident","Natural after reaction"]),
                                              ("Hairstyle", ["+Middle parting","+Side parting","+Brush back"]),
                                              ("Reactions", ["+Happy","+Laughing","+Happy tears","+Family reactions"])]),
  dict(name="Age category", groups=[("Age", ["18–30","30–40","40–50","50+"]),
                                   ("Hair colour", ["Black hair blending","Salt & pepper hairline / blending"])]),
  dict(name="Salon & CTA", groups=[(None, ["Salon shots","CTA shots"])]),
])
P["transplant"] = dict(brand="American Hairline", name="Hair Transplant", colour="#6b4fa3", later=True, src="American_Hairline_Hair_Transplant_Folder_Structure PDF", sections=[
  dict(name="Before", gb=True, groups=[("Emotion & mirror", ["Nervous","Demotivated","Low confidence","Frustrated with hair loss","Mirror shots"]),
                                     ("Hair-loss area · good/bad", ["Receding hairline","Temple hair loss","Crown baldness","Front density","Mid-scalp density","Donor area"]),
                                     ("Conditions", ["Norwood patterns","Advanced baldness","Crown thinning","Receding hairline","Diffuse thinning"]),
                                     ("Profiles", ["Front profile","Side profile","Back profile"])]),
  dict(name="After", gb=True, star=True, groups=[("Results · good/bad", ["Front hairline","Temple restoration","Crown results","Hair density","Overall transformation","360° after"]),
                                              ("Happy faces", ["Smiling","Confident","Mirror reaction","Natural after reaction","Patient satisfaction"]),
                                              ("Before & after · good/bad", ["Front","Crown","Side","360°"]),
                                              ("Hairstyle", ["+Middle parting","+Side parting","+Brush back"]),
                                              ("Reactions", ["+Happy","+Laughing","+Happy tears","+Family reactions"])]),
  dict(name="Age & hair", groups=[("Age", ["18–30","30–40","40–50","50+"]),("Colour", ["Black","Salt & pepper","Grey"]),
                                  ("Type", ["Straight","Wavy","Curly"]),("Pattern", ["Receding hairline","Crown baldness","Front baldness","Advanced baldness"]),
                                  ("Result", ["Hairline restoration","Crown restoration","Overall density"])]),
  dict(name="Consultation & planning", groups=[("Consultation", ["Patient consultation","Doctor explaining hair loss","Patient explaining history","Doctor examining scalp","Hair-loss assessment"]),
                                              ("Scalp analysis", ["Hairline exam","Donor area exam","Crown exam","Density analysis","Close-up scalp exam"]),
                                              ("Hairline design", ["Drawing new hairline","Hairline marking","Front hairline design","Temple design","Patient approval"]),
                                              ("Planning", ["Graft count discussion","Treatment planning","Before photography","Patient documentation"])]),
  dict(name="Transplant process", groups=[("Preparation", ["Patient preparation","Shaving donor area","Cleaning scalp","Marking donor area","Marking recipient area"]),
                                         ("Anaesthesia", ["Local anaesthesia","Anaesthesia application","Preparation close-ups"]),
                                         ("Graft extraction", ["FUE extraction","Punch tool close-up","Extracting grafts","Extracted grafts close-up","Donor area after"]),
                                         ("Graft preparation", ["Collection","Sorting","Counting","Preservation","Graft close-up"]),
                                         ("Graft implantation", ["?List cut off in the PDF"])]),
  dict(name="Clinic & CTA", groups=[("Clinic", ["Exterior","Reception","Consultation room","Operation theatre","Equipment","Interior"]),
                                    ("Doctor & team", ["Doctor intro","Doctor explaining procedure","Doctor performing","Team working","Team group"]),
                                    ("Patient experience", ["Arrival","Consultation","Interaction","Testimonial","Feedback"]),
                                    ("CTA", ["Book consultation","Contact details","Doctor CTA","Clinic branding"])]),
])

def chip(t):
    cls, txt = "chip", t
    if t.startswith("+"): cls, txt = "chip new", t[1:]
    elif t.startswith("?"): cls, txt = "chip ask", t[1:]
    elif t.startswith("★"): cls = "chip star"
    return f'<span class="{cls}">{html.escape(txt)}</span>'

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,'Helvetica Neue',Arial,sans-serif;background:#f6f7f9;color:#1c2430;width:1300px;padding:40px 44px 48px}
.top{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:26px}
.brand{font-size:15px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--c)}
h1{font-size:40px;line-height:1.1;margin-top:4px}
.later{display:inline-block;margin-left:12px;font-size:15px;vertical-align:middle;background:#eee;color:#666;padding:4px 10px;border-radius:20px;font-weight:600}
.legend{display:flex;gap:14px;font-size:14px;color:#555;align-items:center;flex-wrap:wrap;justify-content:flex-end;max-width:560px}
.legend span.k{display:inline-flex;align-items:center;gap:6px}
.map{display:grid;grid-template-columns:200px 1fr;column-gap:0}
.root{grid-row:1/span 50;display:flex;align-items:center;justify-content:center;position:relative}
.root div{background:var(--c);color:#fff;font-weight:800;font-size:22px;text-align:center;padding:22px 18px;border-radius:18px;width:170px;box-shadow:0 6px 18px rgba(0,0,0,.12)}
.root:after{content:"";position:absolute;right:0;top:0;bottom:0;border-right:3px solid var(--c);opacity:.35;top:var(--t);bottom:var(--b)}
.row{display:grid;grid-template-columns:230px 1fr;align-items:center;padding:9px 0;position:relative}
.row:before{content:"";position:absolute;left:0;width:26px;top:50%;border-top:3px solid var(--c);opacity:.35}
.sec{margin-left:26px;background:#fff;border:2.5px solid var(--c);border-radius:14px;padding:12px 14px;position:relative}
.sec b{font-size:19px;display:block}
.sec small{font-size:13px;color:#667;display:block;margin-top:2px}
.sec .tags{margin-top:7px;display:flex;gap:6px;flex-wrap:wrap}
.gb{font-size:11.5px;font-weight:700;padding:3px 8px;border-radius:20px;background:linear-gradient(90deg,#d8f3dc 50%,#ffd9d9 50%);color:#333}
.pri{font-size:11.5px;font-weight:700;padding:3px 8px;border-radius:20px;background:#fff3c4;color:#7a5b00}
.nw{font-size:11.5px;font-weight:700;padding:3px 8px;border-radius:20px;background:#ffe1c7;color:#a24d00}
.sec.newsec{border-style:dashed;border-color:#f08a24}
.leaves{position:relative;padding-left:30px}
.leaves:before{content:"";position:absolute;left:0;width:30px;top:50%;border-top:3px solid var(--c);opacity:.35}
.grp{background:#fff;border-radius:12px;padding:10px 12px;margin:4px 0;border:1px solid #e3e6ea}
.grp .gl{font-size:12.5px;font-weight:700;color:#667;text-transform:uppercase;letter-spacing:.05em;margin-bottom:6px}
.chips{display:flex;flex-wrap:wrap;gap:7px}
.chip{font-size:15px;padding:6px 11px;border-radius:9px;background:#eef1f5;border:1px solid #dde2e8}
.chip.new{background:#ffe9d6;border:1.5px solid #f08a24;color:#7a3a00;font-weight:600}
.chip.new:before{content:"NEW · ";font-size:11px;font-weight:800}
.chip.ask{background:#fff;border:1.5px dashed #d62828;color:#a01818;font-weight:600}
.chip.ask:after{content:"  ?";font-weight:800}
.chip.star{background:#fff3c4;border-color:#e9c46a;font-weight:700}
.foot{margin-top:26px;font-size:13px;color:#889;display:flex;justify-content:space-between}
"""

LEGEND = """<div class="legend">
<span class="k"><span class="gb">GOOD / BAD</span> editors judge these</span>
<span class="k"><span class="chip new" style="font-size:12px;padding:3px 8px">Mohit</span> added 22 Nov</span>
<span class="k"><span class="chip ask" style="font-size:12px;padding:3px 8px">check</span> needs an answer</span>
<span class="k"><span class="chip star" style="font-size:12px;padding:3px 8px">★</span> top priority</span></div>"""

def page(key, p):
    rows = []
    for s in p["sections"]:
        tags = []
        if s.get("gb"): tags.append('<span class="gb">GOOD / BAD</span>')
        if s.get("star"): tags.append('<span class="pri">AI PRIORITY</span>')
        if s.get("new"): tags.append('<span class="nw">NEW SECTION</span>')
        grps = "".join(
            f'<div class="grp">{f"<div class=gl>{html.escape(g)}</div>" if g else ""}<div class="chips">{"".join(chip(i) for i in items)}</div></div>'
            for g, items in s["groups"])
        rows.append(f'''<div class="row"><div class="sec{' newsec' if s.get('new') else ''}"><b>{html.escape(s['name'])}</b>{f"<small>{html.escape(s['sub'])}</small>" if s.get('sub') else ''}<div class="tags">{''.join(tags)}</div></div><div class="leaves">{grps}</div></div>''')
    later = '<span class="later">LATER · not in sheet yet</span>' if p.get("later") else ''
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body style="--c:{p['colour']}"><div class="top"><div><div class="brand">{p['brand']}</div><h1>{p['name']}{later}</h1></div>{LEGEND}</div>
<div class="map"><div class="root"><div>{p['name']}</div></div><div>{''.join(rows)}</div></div>
<div class="foot"><span>Source: {p['src']} + Mohit's WhatsApp list (22 Nov)</span><span>Shot Selection · category map · DRAFT for editors &amp; sir</span></div></body></html>'''

for k, p in P.items():
    (OUT / f"{k}.html").write_text(page(k, p))

# overview page
ov_css = CSS + """
.ov{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}
.card{background:#fff;border-radius:16px;border-top:7px solid var(--c);padding:16px 18px;box-shadow:0 2px 8px rgba(0,0,0,.05)}
.card h2{font-size:22px}.card .br{font-size:12.5px;font-weight:700;color:var(--c);text-transform:uppercase;letter-spacing:.06em}
.card ol{margin:10px 0 0 20px;font-size:16px;line-height:1.65}
.card .none{margin-top:10px;font-size:15px;color:#a01818;border:1.5px dashed #d62828;border-radius:10px;padding:10px}
.mohit{background:#fff7ef;border:2px dashed #f08a24;border-radius:16px;padding:16px 18px;margin-top:18px}
.mohit h3{font-size:19px;color:#a24d00;margin-bottom:8px}
.mohit .cols{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;font-size:15px}
.mohit .cols b{display:block;font-size:13px;text-transform:uppercase;color:#a24d00;margin-bottom:4px}
.center{display:flex;justify-content:center;margin-bottom:22px}
.center div{background:#1c2430;color:#fff;border-radius:40px;padding:14px 34px;font-size:22px;font-weight:800}
"""
def card(c, brand, name, secs, extra=""):
    li = "".join(f"<li>{html.escape(s)}</li>" for s in secs)
    return f'<div class="card" style="--c:{c}"><div class="br">{brand}</div><h2>{name}{extra}</h2>{"<ol>"+li+"</ol>" if secs else ""}</div>'
cards = [card(P[k]["colour"], P[k]["brand"], P[k]["name"],
              [s["name"] + (" · GOOD/BAD" if s.get("gb") else "") + (" · NEW" if s.get("new") else "") for s in P[k]["sections"]],
              ' <span class="later" style="font-size:12px">LATER</span>' if P[k].get("later") else "") for k in P]
cards.insert(1, '<div class="card" style="--c:#c77dba"><div class="br">Alchemane</div><h2>Hair Extension</h2><div class="none">No folder list received yet. Micro ring, keratin bond, tape, feather and V-light are judged the same (Sneha).</div></div>')
cards.append('<div class="card" style="--c:#d62828"><div class="br">Before we put this in the sheet</div><h2>Answers so far</h2><ol>'
 '<li>✅ Mohit: cleaning / washing / drying → clip-on + stick-on. Parting styles + reactions → all products</li>'
 '<li>✅ Editors: clip-on and stick-on stay two lists</li>'
 '<li>✅ Editors: one age set for all: 18–30, 30–40, 40–50, 50+</li>'
 '<li>✅ Editors: keep separate: hair-loss area measurement vs topper size measurement. “Size”: later</li>'
 '<li>✅ Mohit: “Neopia” was a mistake, it is Alopecia (male and female)</li>'
 '<li>⏳ Extension: Ayush\'s list comes later (added when it arrives)</li>'
 '<li>✅ Sir: Round 1 = Before + After good/bad only. Every other category stays in the list for later rounds</li></ol></div>')
ov = f'''<!doctype html><html><head><meta charset="utf-8"><style>{ov_css}</style></head><body style="--c:#1c2430">
<div class="top"><div><div class="brand">Shot Selection · AI training</div><h1>Shot category map</h1></div>{LEGEND}</div>
<div class="center"><div>Consultation video shots</div></div>
<div class="ov">{''.join(cards)}</div>
<div class="foot"><span>Detail for each product is on its own page</span><span>DRAFT v2 · answers added · 23 Nov</span></div></body></html>'''
(OUT / "0-overview.html").write_text(ov)
print("ok")
