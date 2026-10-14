from pathlib import Path
import re
s=Path('index.html').read_text(encoding='utf-8')
checks={
 'documento HTML': '<!doctype html>' in s.lower(),
 'canvas': '<canvas id="game"' in s,
 'botao START': 'id="start"' in s,
 'controles': all(f'id="{x}"' in s for x in ['left','right','down','jump','dash','fire']),
 'sprites': 'unit_run' in s and 'sprite(' in s,
 'movimentacao': 'function updatePlayer' in s,
 'loop de renderizacao': 'requestAnimationFrame(frame)' in s,
 'fase e chefes': all(x in s for x in ['carrier','boss','vanguard']),
 'sem dependencias remotas': not re.search(r'<script[^>]+src=|<link[^>]+href=',s,re.I)
}
for label,ok in checks.items():
 print(('PASS' if ok else 'FAIL')+' '+label)
assert all(checks.values()),'Jogo falhou teste estrutural'
