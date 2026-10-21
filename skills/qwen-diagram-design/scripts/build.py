import json, os, pathlib, re, subprocess, sys
from html import escape
import struct

here=pathlib.Path(__file__).resolve().parent.parent
skill=here.parent/'diagram-design'
python=here/'.venv/bin/python'
browser_path=here/'.cache/ms-playwright'
try:
 data=json.loads(pathlib.Path(sys.argv[1]).read_text()); out=pathlib.Path(sys.argv[2]).resolve(); out.mkdir(parents=True,exist_ok=True)
 steps=data['steps']; assert 3<=len(steps)<=7 and len(data['takeaway'])<=65 and all(len(x['label'])<=28 and len(x['detail'])<=48 for x in steps)
 w,h=960,1200; top=260; boxh=120; gap=28; nodes=[]; links=[]
 for i,s in enumerate(steps):
  y=top+i*(boxh+gap); label=escape(s['label']); detail=escape(s['detail']); nodes.append(f'<rect x="120" y="{y}" width="720" height="{boxh}" rx="8" fill="#fff" stroke="#b9c2c9" stroke-width="2"/><text x="160" y="{y+48}" font-size="34" font-weight="700" fill="#2d3142">{label}</text><text x="160" y="{y+87}" font-size="22" fill="#59636e">{detail}</text>')
  if i: links.append(f'<path d="M480 {y-gap} V{y}" stroke="#bf4520" stroke-width="4" marker-end="url(#a)"/>')
 h=max(1200,top+len(steps)*(boxh+gap)+100); svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img"><title>{escape(data["title"])}</title><desc>{escape(data["takeaway"])}</desc><defs><marker id="a" markerWidth="10" markerHeight="10" refX="5" refY="5" orient="auto"><path d="M0 0L10 5L0 10" fill="#bf4520"/></marker></defs><rect width="100%" height="100%" fill="#f5f5f5"/><text x="120" y="100" font-size="48" font-weight="700" fill="#2d3142">{escape(data["title"])}</text><text x="120" y="158" font-size="24" fill="#59636e">{escape(data["subtitle"])}</text>{"".join(links)}{"".join(nodes)}<text x="120" y="{h-35}" font-size="20" fill="#59636e">{escape(data["takeaway"])}</text></svg>'
 src=out/'diagram.html'; src.write_text('<!doctype html><html><body>'+svg+'</body></html>'); png=out/'diagram.png'; svgout=out/'diagram.svg'
 subprocess.run([str(python),str(skill/'scripts/export_svg.py'),str(src),str(svgout),'--system-fonts'],check=True,capture_output=True)
 env=os.environ.copy(); env.pop('DISPLAY',None); env.pop('WAYLAND_DISPLAY',None); env['PLAYWRIGHT_BROWSERS_PATH']=str(browser_path)
 subprocess.run([str(python),str(skill/'scripts/export_png.py'),str(src),str(png),'2.25'],check=True,capture_output=True,env=env)
 raw=png.read_bytes(); width,height=struct.unpack('>II',raw[16:24]); assert width>0 and height>0 and any(raw[33:]); assert len(re.findall(r'<text',svg))>0
 print(json.dumps({'ok':True,'png':str(png),'svg':str(svgout),'width':width,'height':height}))
except Exception as e:
 print(json.dumps({'ok':False,'error':str(e)})); sys.exit(1)
