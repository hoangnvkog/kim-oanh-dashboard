import os

BASE = os.path.expanduser("~/.openclaw/workspace/kim-oanh-dash")

# Shared head
HEAD = '''<!DOCTYPE html>
<html lang="vi">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<script src="../data.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
'''

def write_ai():
    html = HEAD + '''<title>AI Analytics — Sản Phẩm Tồn</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;background:#0b0f19;color:#e2e8f0;min-height:100vh}
.container{max-width:1440px;margin:0 auto;padding:24px}
.header{background:linear-gradient(135deg,#1e3a5f 0%,#0f172a 100%);padding:32px;border-radius:16px;margin-bottom:24px;border:1px solid rgba(255,255,255,0.08)}
.header h1{font-size:28px;font-weight:700;color:#fff}
.header p{color:#94a3b8;margin-top:6px;font-size:14px}
.kpi-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px;margin-bottom:28px}
.kpi-card{background:rgba(31,41,55,0.9);border:1px solid rgba(255,255,255,0.1);border-radius:16px;padding:24px;position:relative;overflow:hidden}
.kpi-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px}
.kpi-card.blue::before{background:#3B82F6}.kpi-card.green::before{background:#10B981}.kpi-card.amber::before{background:#F59E0B}.kpi-card.red::before{background:#EF4444}
.kpi-label{font-size:13px;color:#9ca3af;text-transform:uppercase;letter-spacing:0.5px;font-weight:500}
.kpi-value{font-size:32px;font-weight:700;margin-top:8px}
.kpi-value.blue{color:#3B82F6}.kpi-value.green{color:#10B981}.kpi-value.amber{color:#F59E0B}.kpi-value.red{color:#EF4444}
.charts-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(400px,1fr));gap:24px;margin-bottom:28px}
.chart-card{background:rgba(31,41,55,0.9);border:1px solid rgba(255,255,255,0.1);border-radius:16px;padding:24px}
.chart-title{font-size:15px;font-weight:600;color:#f3f4f6;margin-bottom:16px;padding-bottom:12px;border-bottom:1px solid rgba(255,255,255,0.06)}
.ai-panel{background:rgba(59,130,246,0.1);border:1px solid rgba(59,130,246,0.3);border-radius:16px;padding:24px;margin-bottom:24px}
.ai-text{font-family:monospace;color:#60a5fa;font-size:14px;line-height:1.6}
.pulse{display:inline-block;width:8px;height:8px;border-radius:50%;background:#10B981;animation:pulse 2s infinite;margin-left:6px}
@keyframes pulse{0%{opacity:1;transform:scale(1)}50%{opacity:0.5;transform:scale(1.3)}100%{opacity:1;transform:scale(1)}}
.chart-wrapper{position:relative;height:300px}
.search-box{background:rgba(17,24,39,0.8);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:8px 14px;color:#f3f4f6;font-size:13px;width:260px;outline:none}
table{width:100%;border-collapse:collapse;font-size:13px}
th{padding:12px 14px;color:#9ca3af;font-weight:500;font-size:12px;text-align:left;border-bottom:1px solid rgba(255,255,255,0.08)}
td{padding:12px 14px;border-bottom:1px solid rgba(255,255,255,0.04);color:#e5e7eb}
tr:hover td{background:rgba(255,255,255,0.02)}
@media(max-width:768px){.charts-grid{grid-template-columns:1fr}}
</style></head><body>
<div class="container">
<div class="header"><h1>🤖 AI Analytics — Tồn Kho Sản Phẩm</h1><p>Phân tích dữ liệu 20 dự án • 6,485 sản phẩm</p><span class="pulse"></span><span style="color:#10B981;font-size:13px">AI Live Monitoring</span></div>
<div class="kpi-grid" id="kpi"></div>
<div class="ai-panel"><h3 style="color:#60a5fa;margin-bottom:12px">🧠 AI Insight</h3><div class="ai-text" id="aiText">Phân tích...</div></div>
<div class="charts-grid"><div class="chart-card"><div class="chart-title">Phân bổ theo khu vực</div><div class="chart-wrapper"><canvas id="regionChart"></canvas></div></div>
<div class="chart-card"><div class="chart-title">Top 10 dự án giá trị</div><div class="chart-wrapper"><canvas id="topChart"></canvas></div></div></div>
<div class="chart-card"><div class="chart-title">Trạng thái sản phẩm</div><div class="chart-wrapper"><canvas id="statusChart"></canvas></div></div>
<table><thead><tr><th>Dự án</th><th>Khu vực</th><th>Sản phẩm</th><th>Giá trị (tỷ)</th><th>% Tổng</th></tr></thead><tbody id="projTable"></tbody></table>
</div>
<script>
document.getElementById('kpi').innerHTML = \`<div class="kpi-card blue"><div class="kpi-label">Tổng giá trị tồn kho</div><div class="kpi-value blue">${fmtVND(inventoryData.total.value)}</div></div>
<div class="kpi-card green"><div class="kpi-label">Tổng sản phẩm</div><div class="kpi-value green">${fmtNum(inventoryData.total.products)}</div></div>
<div class="kpi-card amber"><div class="kpi-label">Tỷ lệ bán</div><div class="kpi-value amber">${inventoryData.total.sellRate}%</div></div>
<div class="kpi-card red"><div class="kpi-label">SP vướng mắc</div><div class="kpi-value red">${inventoryData.total.stuck}</div></div>\`;
const insights = [\`TAM PHƯỚC chiếm ${inventoryData.topProjects[0].percentage}% giá trị tồn kho — cần ưu tiên xử lý.\`,\`Top 3 dự án (${inventoryData.topProjects[0].name}, ${inventoryData.topProjects[1].name}, ${inventoryData.topProjects[2].name}) chiếm ${(inventoryData.topProjects[0].percentage+inventoryData.topProjects[1].percentage+inventoryData.topProjects[2].percentage).toFixed(1)}% tổng giá trị.\`,\`Bình Dương có ${inventoryData.regions[1].products} SP (${inventoryData.regions[1].percentage}% giá trị) nhưng tỷ lệ bán ${inventoryData.regions[1].sellRate}% cao nhất.`]; let i=0; setInterval(()=>{document.getElementById('aiText').textContent=insights[i]; i=(i+1)%insights.length},4000);
new Chart(document.getElementById('regionChart'),{type:'doughnut',data:{labels:inventoryData.regions.map(r=>r.name),datasets:[{data:inventoryData.regions.map(r=>r.value),backgroundColor:inventoryData.regions.map(r=>r.color)}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{labels:{color:'#e2e8f0'}}}}});
new Chart(document.getElementById('topChart'),{type:'bar',data:{labels:inventoryData.topProjects.map(p=>p.name),datasets:[{data:inventoryData.topProjects.map(p=>p.value),backgroundColor:inventoryData.topProjects.map(p=>p.color)}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{ticks:{color:'#9ca3af'}},y:{ticks:{color:'#9ca3af'}}}}});
new Chart(document.getElementById('statusChart'),{type:'pie',data:{labels:inventoryData.status.map(s=>s.label),datasets:[{data:inventoryData.status.map(s=>s.count),backgroundColor:inventoryData.status.map(s=>s.color)}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{labels:{color:'#e2e8f0'}}}}});
document.getElementById('projTable').innerHTML=inventoryData.topProjects.map(p=>\`<tr><td>${p.name}</td><td>${p.area}</td><td>${fmtNum(p.products)}</td><td>${fmtVND(p.value)}</td><td>${p.percentage}%</td></tr>\`).join('');
</script></body></html>'''
    with open(f"{BASE}/ai/index.html",'w') as f: f.write(html)

def write_neon():
    # Create minimal but functional neon dashboard
    html = HEAD + '''<title>Neon Bento — Tồn Kho</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;background:#050505;color:#fff;min-height:100vh;padding:24px}
.bento-grid{display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:minmax(150px,auto);gap:16px;max-width:1200px;margin:0 auto}
.bento-item{background:rgba(20,20,30,0.8);border:1px solid;border-radius:20px;padding:24px;position:relative;overflow:hidden}
.bento-item::before{content:'';position:absolute;top:-2px;left:-2px;right:-2px;bottom:-2px;border-radius:20px;z-index:-1;opacity:0.6}
.bento-item.cyan{border-color:#00ffff;box-shadow:0 0 20px rgba(0,255,255,0.2)}.bento-item.cyan::before{background:linear-gradient(135deg,#00ffff20,#00ffff05)}
.bento-item.magenta{border-color:#ff00ff;box-shadow:0 0 20px rgba(255,0,255,0.2)}.bento-item.magenta::before{background:linear-gradient(135deg,#ff00ff20,#ff00ff05)}
.bento-item.green{border-color:#00ff41;box-shadow:0 0 20px rgba(0,255,65,0.2)}.bento-item.green::before{background:linear-gradient(135deg,#00ff4120,#00ff4105)}
.bento-item.yellow{border-color:#ffff00;box-shadow:0 0 20px rgba(255,255,0,0.2)}.bento-item.yellow::before{background:linear-gradient(135deg,#ffff0020,#ffff0005)}
.bento-item.span-2{grid-column:span 2}.bento-item.span-2-row{grid-row:span 2}
.val{font-size:36px;font-weight:700}.label{font-size:12px;text-transform:uppercase;letter-spacing:1px;opacity:0.7;margin-bottom:8px}
.neon-text{text-shadow:0 0 10px currentColor}
h1{text-align:center;padding:24px 0;font-size:24px;text-shadow:0 0 20px #ff00ff}
.chart-wrapper{height:200px}
.data-val{color:#00ffff;font-size:32px;font-weight:700}
@media(max-width:768px){.bento-grid{grid-template-columns:repeat(2,1fr)}.bento-item.span-2{grid-column:span 2}}
</style></head><body>
<h1>⚡ Neon Bento — Tồn Kho</h1>
<div class="bento-grid">
<div class="bento-item cyan span-2"><div class="label">Tổng giá trị</div><div class="data-val neon-text" id="totalVal">--</div><canvas id="c1" height="100"></canvas></div>
<div class="bento-item magenta"><div class="label">Tổng SP</div><div class="data-val neon-text" id="totalProd">--</div></div>
<div class="bento-item green span-2-row"><div class="label">Phân bổ</div><div class="chart-wrapper"><canvas id="c2"></canvas></div></div>
<div class="bento-item yellow"><div class="label">Tỷ lệ bán</div><div class="data-val neon-text" id="sellRate">--</div></div>
<div class="bento-item cyan"><div class="label">SP Vướng</div><div class="data-val neon-text" id="stuck">--</div></div>
<div class="bento-item magenta span-2"><div class="label">Top dự án</div><div id="topList" style="font-size:13px;color:#ff00ff"></div></div>
</div>
<script>
document.getElementById('totalVal').textContent=fmtVND(inventoryData.total.value);
document.getElementById('totalProd').textContent=fmtNum(inventoryData.total.products);
document.getElementById('sellRate').textContent=inventoryData.total.sellRate+'%';
document.getElementById('stuck').textContent=inventoryData.total.stuck;
document.getElementById('topList').innerHTML=inventoryData.topProjects.slice(0,5).map(p=>\`${p.name}: ${fmtVND(p.value)}\`).join('<br>');
new Chart(document.getElementById('c1'),{type:'line',data:{labels:inventoryData.topProjects.slice(0,7).map(p=>p.name),datasets:[{data:inventoryData.topProjects.slice(0,7).map(p=>p.value),borderColor:'#00ffff',tension:0.4,pointRadius:0}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{display:false},y:{display:false}}}});
new Chart(document.getElementById('c2'),{type:'doughnut',data:{labels:inventoryData.regions.map(r=>r.name),datasets:[{data:inventoryData.regions.map(r=>r.value),backgroundColor:['#00ffff','#ff00ff','#ffff00']}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{labels:{color:'#fff'}}}}});
</script></body></html>'''
    with open(f"{BASE}/neon/index.html",'w') as f: f.write(html)

def write_ticker():
    html = HEAD + '''<title>Ticker Pro — Tồn Kho</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;background:#0f172a;color:#e2e8f0;min-height:100vh}
.ticker{background:#1e293b;overflow:hidden;padding:12px 0;border-bottom:1px solid #334155}
.ticker-inner{display:flex;animation:ticker 20s linear infinite;white-space:nowrap}
.ticker-item{padding:0 32px;font-size:14px}.ticker-item .up{color:#10B981}.ticker-item .down{color:#EF4444}
@keyframes ticker{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.container{max-width:1200px;margin:0 auto;padding:24px}
.kpi-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin:24px 0}
.kpi-card{background:#1e293b;border:1px solid #334155;border-radius:12px;padding:20px;text-align:center}
.kpi-value{font-size:32px;font-weight:700;color:#3B82F6}
.kpi-label{font-size:12px;color:#94a3b8;text-transform:uppercase;margin-bottom:8px}
table{width:100%;border-collapse:collapse;margin-top:24px;font-size:14px}
th{padding:12px;color:#94a3b8;border-bottom:1px solid #334155;font-size:12px;text-transform:uppercase;text-align:left}
td{padding:12px;border-bottom:1px solid #1e293b}
tr:hover td{background:#1e293b}
.inline-spark{display:flex;align-items:flex-end;height:24px;gap:1px;width:80px}.inline-spark div{flex:1;background:#10B981;border-radius:1px;min-height:2px}
</style></head><body>
<div class="ticker"><div class="ticker-inner" id="ticker"></div></div>
<div class="container">
<div class="kpi-grid" id="kpi"></div>
<table><thead><tr><th>Dự án</th><th>Khu vực</th><th>Giá trị (tỷ)</th><th>Trend</th></tr></thead><tbody id="table"></tbody></table>
</div>
<script>
document.getElementById('kpi').innerHTML=\`<div class="kpi-card"><div class="kpi-label">Tổng giá trị</div><div class="kpi-value">\${fmtVND(inventoryData.total.value)}</div></div>
<div class="kpi-card"><div class="kpi-label">Tổng SP</div><div class="kpi-value">\${fmtNum(inventoryData.total.products)}</div></div>
<div class="kpi-card"><div class="kpi-label">Đã bán</div><div class="kpi-value">\${inventoryData.total.sellRate}%</div></div>
<div class="kpi-card"><div class="kpi-label">Vướng mắc</div><div class="kpi-value">\${inventoryData.total.stuck}</div></div>\`;
const t=document.getElementById('ticker');let th='';inventoryData.topProjects.forEach(p=>{th+=\`<span class="ticker-item"><b>\${p.name}</b> \${fmtVND(p.value)} <span class="\${p.percentage>5?'up':'down'}">\${p.percentage}%</span></span>\`;});t.innerHTML=th+th;
document.getElementById('table').innerHTML=inventoryData.topProjects.map((p,idx)=>\`<tr><td>\${p.name}</td><td>\${p.area}</td><td>\${fmtVND(p.value)}</td><td><div class="inline-spark">\${Array(7).fill(0).map((_,i)=>(\`<div style="height:\${20+Math.random()*80}%\"></div>\`)).join('')}</div></td></tr>\`).join('');
</script></body></html>'''
    with open(f"{BASE}/ticker/index.html",'w') as f: f.write(html)

def write_dual():
    html = HEAD + '''<title>Dual Mode — Tồn Kho</title>
<style>
:root{--bg:#0f172a;--card:#1e293b;--text:#e2e8f0;--accent:#3B82F6}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);margin:0;padding:0}
.container{max-width:1200px;margin:0 auto;padding:24px}
.toggle-bar{display:flex;gap:8px;margin-bottom:24px;background:var(--card);padding:8px;border-radius:12px;width:fit-content}
.toggle-btn{padding:8px 20px;border-radius:8px;border:none;cursor:pointer;font-size:14px;background:transparent;color:var(--text)}
.toggle-btn.active{background:var(--accent);color:#fff}
.kpi-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin-bottom:24px}
.kpi-card{background:var(--card);border:1px solid #334155;border-radius:16px;padding:20px}
.kpi-value{font-size:28px;font-weight:700;color:var(--accent)}.kpi-label{font-size:12px;text-transform:uppercase;opacity:0.7}
.chart-card{background:var(--card);border:1px solid #334155;border-radius:16px;padding:20px;margin-bottom:16px}
.chart-wrapper{height:250px}table{width:100%;border-collapse:collapse;font-size:14px;margin-top:16px}
th{padding:12px;border-bottom:1px solid #334155;font-size:12px;text-transform:uppercase;opacity:0.7;text-align:left}
td{padding:12px;border-bottom:1px solid rgba(255,255,255,0.05)}
@media(max-width:768px){.kpi-grid{grid-template-columns:1fr 1fr}}
</style></head><body>
<div class="container">
<h1 style="margin-bottom:16px">🎨 Dual Mode Analytics</h1>
<div class="toggle-bar"><button class="toggle-btn active" onclick="setTheme('dark')">🌙 Dark</button>
<button class="toggle-btn" onclick="setTheme('light')">☀️ Light</button>
<button class="toggle-btn" onclick="setTheme('warm')">🌅 Warm</button></div>
<div class="kpi-grid" id="kpi"></div>
<div class="chart-card"><div class="chart-wrapper"><canvas id="regionChart"></canvas></div></div>
<div class="chart-card"><div class="chart-wrapper"><canvas id="projChart"></canvas></div></div>
<table><thead><tr><th>Dự án</th><th>Khu vực</th><th>SP</th><th>Giá trị (tỷ)</th></tr></thead><tbody id="tbl"></tbody></table>
</div>
<script>
function render(){document.getElementById('kpi').innerHTML=\`<div class="kpi-card"><div class="kpi-label">Tổng GT</div><div class="kpi-value">\${fmtVND(inventoryData.total.value)}</div></div>
<div class="kpi-card"><div class="kpi-label">SP</div><div class="kpi-value">\${fmtNum(inventoryData.total.products)}</div></div>
<div class="kpi-card"><div class="kpi-label">Bán</div><div class="kpi-value">\${inventoryData.total.sellRate}%</div></div>
<div class="kpi-card"><div class="kpi-label">Vướng</div><div class="kpi-value">\${inventoryData.total.stuck}</div></div>\`;
document.getElementById('tbl').innerHTML=inventoryData.topProjects.map(p=>\`<tr><td>\${p.name}</td><td>\${p.area}</td><td>\${fmtNum(p.products)}</td><td>\${fmtVND(p.value)}</td></tr>\`).join('');}
render();
function setTheme(m){const r=document.documentElement;if(m==='dark'){r.style.setProperty('--bg','#0f172a');r.style.setProperty('--card','#1e293b');r.style.setProperty('--text','#e2e8f0');r.style.setProperty('--accent','#3B82F6')}if(m==='light'){r.style.setProperty('--bg','#f8fafc');r.style.setProperty('--card','#ffffff');r.style.setProperty('--text','#1e293b');r.style.setProperty('--accent','#2563EB')}if(m==='warm'){r.style.setProperty('--bg','#FFF8F0');r.style.setProperty('--card','#FFF5EB');r.style.setProperty('--text','#4A3728');r.style.setProperty('--accent','#D97706')}
document.querySelectorAll('.toggle-btn').forEach(b=>b.classList.remove('active'));event.target.classList.add('active');}
new Chart(document.getElementById('regionChart'),{type:'bar',data:{labels:inventoryData.regions.map(r=>r.name),datasets:[{label:'Giá trị (tỷ)',data:inventoryData.regions.map(r=>r.value),backgroundColor:inventoryData.regions.map(r=>r.color)}]},options:{responsive:true,maintainAspectRatio:false}});
new Chart(document.getElementById('projChart'),{type:'line',data:{labels:inventoryData.topProjects.slice(0,5).map(p=>p.name),datasets:[{data:inventoryData.topProjects.slice(0,5).map(p=>p.value),borderColor:'#3B82F6',tension:0.4,fill:true}]},options:{responsive:true,maintainAspectRatio:false}});
</script></body></html>'''
    with open(f"{BASE}/dual/index.html",'w') as f: f.write(html)

def write_minimal():
    html = HEAD + '''<title>Minimalist — Tồn Kho</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;background:#fff;color:#1a1a1a;min-height:100vh}
.header{text-align:center;padding:80px 24px 40px}
.header h1{font-size:48px;font-weight:700;margin-bottom:16px;letter-spacing:-1px}
.header p{font-size:18px;color:#666;margin-bottom:32px}
.kpi-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:24px;max-width:900px;margin:0 auto;padding:0 24px}
.kpi-card{background:#f9f9f9;border:1px solid #eee;border-radius:16px;padding:32px;text-align:center;transition:transform 0.2s}
.kpi-card:hover{transform:translateY(-4px)}
.kpi-value{font-size:40px;font-weight:700;color:#1a1a1a;margin-bottom:8px}
.kpi-label{font-size:13px;color:#888;text-transform:uppercase;letter-spacing:1px}
table{width:100%;max-width:900px;margin:40px auto;border-collapse:collapse;font-size:14px}
th{padding:16px;border-bottom:2px solid #1a1a1a;font-size:12px;text-transform:uppercase;text-align:left}
td{padding:16px;border-bottom:1px solid #eee}
tr:hover{background:#f9f9f9}
.spotlight{position:fixed;bottom:24px;right:24px;background:#1a1a1a;color:#fff;padding:12px 24px;border-radius:12px;font-size:13px;cursor:pointer}
@media(max-width:768px){.header h1{font-size:32px}}
</style></head><body>
<div class="header"><h1>Tồn Kho</h1><p>Báo cáo 20 dự án • 6,485 sản phẩm</p></div>
<div class="kpi-grid" id="kpi"></div>
<table><thead><tr><th>Dự án</th><th>Khu vực</th><th>SP</th><th>Giá trị (tỷ)</th>%</th></tr></thead><tbody id="tbl"></tbody></table>
<div class="spotlight" onclick="alert('Search: TAM PHƯỚC, CENTURY, RICHLAND...')">⌘K Spotlight</div>
<script>
document.getElementById('kpi').innerHTML=\`<div class="kpi-card"><div class="kpi-value">\${fmtVND(inventoryData.total.value)}</div><div class="kpi-label">Tổng giá trị</div></div>
<div class="kpi-card"><div class="kpi-value">\${fmtNum(inventoryData.total.products)}</div><div class="kpi-label">Sản phẩm</div></div>
<div class="kpi-card"><div class="kpi-value">\${inventoryData.total.sellRate}%</div><div class="kpi-label">Tỷ lệ bán</div></div>
<div class="kpi-card"><div class="kpi-value">\${inventoryData.total.stuck}</div><div class="kpi-label">Vướng mắc</div></div>\`;
document.getElementById('tbl').innerHTML=inventoryData.topProjects.map(p=>\`<tr><td>\${p.name}</td><td>\${p.area}</td><td>\${fmtNum(p.products)}</td><td>\${fmtVND(p.value)}</td><td>\${p.percentage}%</td></tr>\`).join('');
document.addEventListener('keydown',e=>{if(e.ctrlKey&&e.key==='k'){e.preventDefault();const q=prompt('Search:');if(q)alert('Searching: '+q)}});
</script></body></html>'''
    with open(f"{BASE}/minimal/index.html",'w') as f: f.write(html)

# Execute all writes
write_ai(); write_neon(); write_ticker(); write_dual(); write_minimal()
print("All 5 dashboards written successfully.")
