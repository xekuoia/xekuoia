"""Arma la app (un solo HTML) a partir de las piezas de src/.
Uso, desde la raíz del repo:  python3 src/assemble.py   ->  escribe app/index.html
"""
import os
D=os.path.dirname(os.path.abspath(__file__))+os.sep
OUT=os.path.join(D,os.pardir,"app","index.html")
v3=open(D+'v3.html').read()
head=v3[:v3.index('<style>')+len('<style>')]
css=v3[v3.index('<style>')+len('<style>'):v3.index('</style>')]
rm=["body[data-layout=side] .panel{grid-template-rows:auto auto minmax(0,1fr)}\n","body[data-layout=bottom] .panel{grid-template-columns:minmax(0,1fr) minmax(0,1.35fr);grid-template-rows:auto minmax(0,1fr)}\n","body[data-layout=side] .browser{max-height:232px;border-bottom:1px solid var(--edge)}\n","body[data-layout=bottom] .browser{border-right:1px solid var(--edge)}\n","scrollbar-width:none;grid-column:1/-1;","  body[data-layout] .panel{grid-template-columns:minmax(0,1fr);grid-template-rows:auto auto auto}\n","  body[data-layout] .browser{max-height:none;border-right:0;border-bottom:1px solid var(--edge)}\n"]
for a in rm:
    assert css.count(a)==1,a
    css=css.replace(a,"scrollbar-width:none;" if a.startswith("scrollbar") else "")
extra=open(D+'extra.css').read().replace("touch-action:none}\n.lrow.sel","}\n.lrow.sel").replace(".cats{grid-area:cats;grid-column:auto!important;",".cats{grid-area:cats;")
extra+=open(D+'extra2.css').read()
html=head+css+extra+"</style>\n</head>\n"+open(D+'body.html').read()+"\n<script>\n"+open(D+'app.js').read()+"\n</script>\n</body>\n</html>\n"
open(OUT,'w').write(html)
print(len(html))
