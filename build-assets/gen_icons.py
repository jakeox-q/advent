import sys,re,os
sys.path.insert(0,'/home/user/advent/handoff/design-source')
src=open('/home/user/advent/handoff/design-source/common.py').read()
m=re.search(r'def I\(.*?\n(.*?)\n\S',src,re.S)
P=dict(re.findall(r'"(\w+)":\s*\'(.*?)\'',src))
T=[("strategy","mind","#e8eef8","#aebfe3"),("family","family","#fcf3cc","#ebd582"),("party","balloon","#fdeee3","#f2c3a0"),("thematic","book","#e2f2f6","#9fd3e2"),("wargames","tank","#eef0f3","#c3cad4"),("solo-games","dice","#fdeee3","#f2c3a0"),("two-player","duel","#e2f2f6","#9fd3e2"),("kids","blocks","#e3f2e9","#aedcbf")]
out=sys.argv[1]; html=['<html><body style="margin:0">']
for h,ic,bg,fg in T:
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{fg}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">{P[ic]}</svg>'
    open(f'{out}/type-icon-{h}.svg','w').write(svg)
    html.append(f'<div id="t-{h}" style="width:800px;height:450px;background:{bg};position:relative;overflow:hidden"><svg style="position:absolute;right:-33px;top:-40px;width:496px;height:496px;transform:rotate(-12deg)" viewBox="0 0 24 24" fill="none" stroke="{fg}" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">{P[ic]}</svg></div>')
open(f'{out}/tiles.html','w').write(''.join(html)+'</body></html>')
print(len(P),'icons parsed')
