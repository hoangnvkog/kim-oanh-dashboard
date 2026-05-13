// Kim Oanh Dashboard — Shared Components & Utilities
// Usage: import this file in all dashboards

// ================== DATA HELPERS ==================
function cloneData() { return JSON.parse(JSON.stringify(inventoryData)); }

function enrichProjectData(projects) {
  projects.forEach(function(p) {
    p.sold = p.sold || Math.floor(p.products * p.sellThroughRate / 100);
    p.unsold = p.unsold || (p.products - (p.sold || 0));
    p.stuck = p.stuck || Math.floor(p.products * 0.02 + Math.random() * 5);
    p.stuckValue = p.stuckValue || +(p.value * (p.stuck / p.products) * (0.5 + Math.random() * 0.5)).toFixed(2);
    p.avgValue = p.avgValue || +(p.value / p.products).toFixed(2);
    p.stuckPct = +((p.stuck / p.products * 100).toFixed(1));
    p.stuckValuePct = +((p.stuckValue / p.value * 100).toFixed(1));
    
    if (p.sellThroughRate < 20) { p.alertLevel = 'danger'; p.action = 'Cần đẩy mạnh'; }
    else if (p.sellThroughRate < 35) { p.alertLevel = 'warning'; p.action = 'Theo dõi'; }
    else { p.alertLevel = 'success'; p.action = 'Tốt'; }
    
    if (p.stuckPct > 10) p.stuckLevel = 'danger';
    else if (p.stuckPct > 5) p.stuckLevel = 'warning';
    else p.stuckLevel = 'success';
  });
  return projects;
}

var enrichedData = cloneData();
enrichProjectData(enrichedData.topProjects);

// ================== SHARED RENDER HELPERS ==================
function getBadgeClass(level) {
  return level === 'danger' ? 'badge badge-danger' : level === 'warning' ? 'badge badge-warning' : 'badge badge-success';
}

function getAlertBadge(level) {
  return '<span class="' + getBadgeClass(level) + '">' + 
    (level === 'danger' ? '⚠️ Cao' : level === 'warning' ? '△ TB' : '✓ Thấp') + '</span>';
}

function stuckClass(pct) {
  return pct > 10 ? 'high' : pct > 5 ? 'medium' : 'low';
}

// ================== SHARED EXPORT ==================
function exportToCSV(tableId, filename) {
  var table = document.getElementById(tableId);
  if (!table) return;
  var csv = 'data:text/csv;charset=utf-8,\uFEFF';
  var rows = table.querySelectorAll('tr');
  rows.forEach(function(row) {
    var cols = row.querySelectorAll('td, th');
    var rowData = [];
    cols.forEach(function(col) { rowData.push('"' + col.textContent.replace(/"/g, '""').trim() + '"'); });
    csv += rowData.join(',') + '\n';
  });
  var link = document.createElement('a');
  link.href = encodeURI(csv);
  link.download = filename + '.csv';
  link.click();
}

function printTable(tableId) {
  var table = document.getElementById(tableId).outerHTML;
  var win = window.open('', '_blank');
  win.document.write('<html><head><title>In báo cáo</title>' +
    '<style>table{border-collapse:collapse;width:100%}th,td{border:1px solid #000;padding:8px;text-align:left}th{background:#f0f0f0}</style>' +
    '</head><body>' + table + '</body></html>');
  win.document.close();
  win.print();
}

// ================== SHARED MODAL ==================
function createModal(id, options) {
  options = options || {};
  var modal = document.createElement('div');
  modal.id = id;
  modal.className = 'dash-modal';
  modal.innerHTML = '<div class="dash-modal-overlay" onclick="closeModal(\'' + id + '\')"></div>' +
    '<div class="dash-modal-content">' +
    '<div class="dash-modal-header"><h3 id="' + id + '-title">' + (options.title || '') + '</h3>' +
    '<button class="dash-modal-close" onclick="closeModal(\'' + id + '\')">&times;</button></div>' +
    '<div class="dash-modal-body" id="' + id + '-body"></div></div>';
  document.body.appendChild(modal);
  return modal;
}

function openModal(id, title, content) {
  var modal = document.getElementById(id) || createModal(id, {title: title || 'Chi tiết'});
  document.getElementById(id + '-title').textContent = title || 'Chi tiết';
  document.getElementById(id + '-body').innerHTML = content;
  modal.classList.add('active');
}

function closeModal(id) {
  var modal = document.getElementById(id);
  if (modal) modal.classList.remove('active');
}

// ================== PROJECT DETAIL VIEW ==================
function renderProjectDetail(name, data) {
  var p = data.topProjects.find(function(x) { return x.name === name; });
  if (!p) return '<p>Không tìm thấy dự án</p>';
  
  var stuckRate = +((p.stuck / p.products * 100).toFixed(1));
  return '<div class="project-detail">' +
    '<div class="detail-item"><div class="detail-label">Khu vực</div><div class="detail-value">' + p.area + '</div></div>' +
    '<div class="detail-item"><div class="detail-label">Tổng SP</div><div class="detail-value">' + fmtNum(p.products) + '</div></div>' +
    '<div class="detail-item"><div class="detail-label">Giá trị</div><div class="detail-value">' + fmtVND(p.value) + '</div></div>' +
    '<div class="detail-item"><div class="detail-label">Đã bán</div><div class="detail-value" style="color:var(--success,#10B981)">' + fmtNum(p.sold) + '</div></div>' +
    '<div class="detail-item"><div class="detail-label">Chưa bán</div><div class="detail-value" style="color:var(--warning,#F59E0B)">' + fmtNum(p.unsold) + '</div></div>' +
    '<div class="detail-item"><div class="detail-label">Sell-through</div><div class="detail-value" style="color:' + (p.sellThroughRate < 30 ? '#EF4444' : '#10B981') + '">' + p.sellThroughRate + '%</div></div>' +
    '<div class="detail-item"><div class="detail-label">SP vướng</div><div class="detail-value" style="color:#EF4444">' + p.stuck + ' (' + stuckRate + '%)</div></div>' +
    '<div class="detail-item"><div class="detail-label">Giá trị/SP</div><div class="detail-value">' + p.avgValue + ' tỷ</div></div>' +
    '</div>' +
    '<div style="margin-top:16px"><strong>Đề xuất hành động:</strong> ' + p.action + '</div>';
}

// ================== SHARED CSS (inject) ==================
function injectSharedStyles() {
  if (document.getElementById('dash-shared-styles')) return;
  var css = document.createElement('style');
  css.id = 'dash-shared-styles';
  css.textContent = `
    .badge{display:inline-block;padding:3px 8px;border-radius:6px;font-size:12px;font-weight:600}
    .badge-danger{background:#EF4444;color:#fff}.badge-warning{background:#F59E0B;color:#000}.badge-success{background:#10B981;color:#fff}
    .alert-row td{background:rgba(239,68,68,0.1)!important}
    .stuck-high{color:#EF4444;font-weight:700}.stuck-medium{color:#F59E0B;font-weight:600}.stuck-low{color:#10B981}
    .dash-modal{display:none;position:fixed;top:0;left:0;width:100%;height:100%;align-items:center;justify-content:center;z-index:1000;padding:24px}
    .dash-modal.active{display:flex}
    .dash-modal-overlay{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.7)}
    .dash-modal-content{position:relative;z-index:1;background:var(--card,#1e293b);border:1px solid #334155;border-radius:16px;max-width:700px;width:100%;max-height:90vh;overflow-y:auto}
    .dash-modal-header{padding:20px;border-bottom:1px solid #334155;display:flex;justify-content:space-between;align-items:center}
    .dash-modal-body{padding:20px}
    .dash-modal-close{background:none;border:none;color:var(--text,#e2e8f0);font-size:24px;cursor:pointer}
    .project-detail{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px}
    .detail-item{background:rgba(255,255,255,0.03);padding:12px;border-radius:8px}
    .detail-label{font-size:11px;opacity:0.7;text-transform:uppercase;margin-bottom:4px}
    .detail-value{font-size:16px;font-weight:700}
    .export-btn,.action-btn{padding:6px 12px;border-radius:6px;border:1px solid #334155;background:#334155;color:#e2e8f0;cursor:pointer;font-size:13px;transition:.2s;margin:2px}
    .export-btn:hover,.action-btn:hover{background:#3B82F6;border-color:#3B82F6}
    .filter-btn{padding:6px 12px;border-radius:6px;border:1px solid #334155;background:#1e293b;color:#94a3b8;cursor:pointer;font-size:13px}
    .filter-btn.active{background:#3B82F6;color:#fff;border-color:#3B82F6}
    .table-section{background:#1e293b;border:1px solid #334155;border-radius:16px;padding:20px;margin:16px 0}
    .table-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;flex-wrap:wrap;gap:12px}
    .table-title{font-size:16px;font-weight:600}
    @media(max-width:768px){.project-detail{grid-template-columns:1fr 1fr}.table-header{flex-direction:column;align-items:flex-start}}
  `;
  document.head.appendChild(css);
}

// Auto-inject
document.addEventListener('DOMContentLoaded', function() { injectSharedStyles(); });
