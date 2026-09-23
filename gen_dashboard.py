
html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Amazon India Dashboard</title>
<meta name="description" content="Amazon India Sales Analytics — 10,000 orders, Jan 2024-Aug 2026"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.2/dist/chart.umd.min.js"></script>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0a0a0a;
  --surface:#111111;
  --surface2:#1a1a1a;
  --border:#222222;
  --border2:#2a2a2a;
  --tx:#e8e8e8;
  --tx2:#888888;
  --tx3:#555555;
  --accent:#FF9900;
  --accent-dim:rgba(255,153,0,.1);
  --accent-border:rgba(255,153,0,.2);
  --green:#22c55e;
  --red:#ef4444;
  --blue:#3b82f6;
  --r:8px
}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--tx);min-height:100vh;overflow-x:hidden;font-size:14px;line-height:1.5}
.sidebar{position:fixed;left:0;top:0;bottom:0;width:220px;background:var(--surface);border-right:1px solid var(--border);display:flex;flex-direction:column;z-index:100}
.sb-header{padding:20px 16px 16px;border-bottom:1px solid var(--border)}
.sb-brand{display:flex;align-items:center;gap:10px}
.sb-dot{width:8px;height:8px;border-radius:50%;background:var(--accent);flex-shrink:0}
.sb-name{font-size:13px;font-weight:600;color:var(--tx);letter-spacing:-.01em}
.sb-meta{font-size:11px;color:var(--tx3);margin-top:2px;font-family:'JetBrains Mono',monospace}
.sb-nav{padding:12px 8px;flex:1;overflow-y:auto}
.nav-group-label{font-size:10px;font-weight:600;letter-spacing:.08em;color:var(--tx3);text-transform:uppercase;padding:8px 8px 4px}
.nav-item{display:flex;align-items:center;gap:9px;padding:8px 10px;border-radius:6px;cursor:pointer;font-size:13px;font-weight:500;color:var(--tx2);margin-bottom:1px;border:none;background:none;width:100%;text-align:left;transition:background .15s,color .15s}
.nav-item:hover{background:var(--surface2);color:var(--tx)}
.nav-item.active{background:var(--accent-dim);color:var(--accent)}
.nav-item.active .nav-icon{color:var(--accent)}
.nav-icon{width:16px;height:16px;flex-shrink:0;opacity:.7}
.nav-item.active .nav-icon{opacity:1}
.nav-item svg{width:14px;height:14px;flex-shrink:0}
.sb-footer{padding:12px 16px;border-top:1px solid var(--border)}
.sb-stats{display:grid;grid-template-columns:1fr 1fr;gap:6px}
.sb-stat{background:var(--surface2);border-radius:6px;padding:8px;text-align:center}
.sb-stat-val{font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:500;color:var(--tx)}
.sb-stat-lbl{font-size:10px;color:var(--tx3);margin-top:1px}
.main{margin-left:220px;min-height:100vh;display:flex;flex-direction:column}
.topbar{position:sticky;top:0;z-index:50;background:rgba(10,10,10,.85);backdrop-filter:blur(16px);border-bottom:1px solid var(--border);padding:0 24px;height:52px;display:flex;align-items:center;gap:0}
.tb-breadcrumb{display:flex;align-items:center;gap:6px;font-size:12px}
.tb-bc-root{color:var(--tx3)}
.tb-bc-sep{color:var(--tx3)}
.tb-bc-current{color:var(--tx);font-weight:500}
.tb-right{margin-left:auto;display:flex;align-items:center;gap:10px}
.filter-wrap{display:flex;align-items:center;gap:6px}
.filter-label{font-size:11px;color:var(--tx3);font-family:'JetBrains Mono',monospace}
.filter-sel{background:var(--surface);border:1px solid var(--border2);color:var(--tx2);font-size:12px;font-family:'Inter',sans-serif;padding:5px 10px;border-radius:6px;cursor:pointer;outline:none;transition:border-color .15s}
.filter-sel:hover,.filter-sel:focus{border-color:var(--accent);color:var(--tx)}
.status-dot{width:6px;height:6px;border-radius:50%;background:var(--green);display:inline-block;margin-right:6px;animation:blink 2.5s ease infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.3}}
.status-label{font-size:11px;color:var(--tx3);font-family:'JetBrains Mono',monospace}
.content{padding:20px 24px;flex:1}
.sec{display:none}
.sec.active{display:block;animation:fadein .2s ease}
@keyframes fadein{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
.sec-header{margin-bottom:20px;padding-bottom:16px;border-bottom:1px solid var(--border)}
.sec-title{font-size:16px;font-weight:600;color:var(--tx);letter-spacing:-.02em}
.sec-desc{font-size:12px;color:var(--tx3);margin-top:3px;font-family:'JetBrains Mono',monospace}
.kpi-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px}
.kpi{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:16px;transition:border-color .15s}
.kpi:hover{border-color:var(--border2)}
.kpi-label{font-size:11px;font-weight:500;color:var(--tx3);text-transform:uppercase;letter-spacing:.06em;margin-bottom:10px}
.kpi-val{font-family:'JetBrains Mono',monospace;font-size:24px;font-weight:500;color:var(--tx);letter-spacing:-.02em;line-height:1}
.kpi-sub{font-size:11px;color:var(--tx3);margin-top:6px}
.kpi-tag{display:inline-block;font-size:10px;font-weight:500;padding:2px 7px;border-radius:4px;margin-top:8px;font-family:'JetBrains Mono',monospace}
.tag-up{background:rgba(34,197,94,.1);color:var(--green);border:1px solid rgba(34,197,94,.2)}
.tag-dn{background:rgba(239,68,68,.1);color:var(--red);border:1px solid rgba(239,68,68,.2)}
.tag-accent{background:var(--accent-dim);color:var(--accent);border:1px solid var(--accent-border)}
.grid{display:grid;gap:12px;margin-bottom:20px}
.g2{grid-template-columns:1fr 1fr}
.g3{grid-template-columns:repeat(3,1fr)}
.span2{grid-column:span 2}
.card{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:18px;transition:border-color .15s}
.card:hover{border-color:var(--border2)}
.card-header{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:14px}
.card-title{font-size:13px;font-weight:600;color:var(--tx);letter-spacing:-.01em}
.card-sub{font-size:11px;color:var(--tx3);margin-top:2px;font-family:'JetBrains Mono',monospace}
.card-tag{font-size:10px;color:var(--tx3);font-family:'JetBrains Mono',monospace;background:var(--surface2);border:1px solid var(--border);padding:2px 8px;border-radius:4px}
.chart-wrap{position:relative}
.divider{height:1px;background:var(--border);margin:20px 0}
table{width:100%;border-collapse:collapse;font-size:12px}
thead tr{border-bottom:1px solid var(--border)}
thead th{padding:8px 12px;text-align:left;font-size:10px;font-weight:600;color:var(--tx3);text-transform:uppercase;letter-spacing:.07em;white-space:nowrap;font-family:'JetBrains Mono',monospace}
tbody tr{border-bottom:1px solid rgba(34,34,34,.6);transition:background .1s}
tbody tr:hover{background:rgba(255,255,255,.02)}
td{padding:10px 12px;color:var(--tx)}
td.dim{color:var(--tx2)}
td.mono{font-family:'JetBrains Mono',monospace;font-size:11px}
.rank{display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;border-radius:4px;font-size:10px;font-weight:600;background:var(--surface2);color:var(--tx3);font-family:'JetBrains Mono',monospace}
.rank.r1{background:rgba(255,153,0,.12);color:var(--accent)}
.rank.r2{background:rgba(255,255,255,.06);color:var(--tx2)}
.rank.r3{background:rgba(255,255,255,.04);color:var(--tx3)}
.bar-wrap{display:flex;align-items:center;gap:8px}
.bar-track{flex:1;height:4px;border-radius:2px;background:var(--surface2);overflow:hidden}
.bar-fill{height:100%;border-radius:2px;background:var(--accent);transition:width .5s ease}
.bar-fill.blue{background:var(--blue)}
.bar-fill.green{background:var(--green)}
.bar-pct{font-size:10px;color:var(--tx3);min-width:32px;font-family:'JetBrains Mono',monospace}
.pill{display:inline-block;padding:2px 8px;border-radius:4px;font-size:10px;font-weight:500;font-family:'JetBrains Mono',monospace}
.pill-green{background:rgba(34,197,94,.1);color:var(--green);border:1px solid rgba(34,197,94,.15)}
.pill-blue{background:rgba(59,130,246,.1);color:var(--blue);border:1px solid rgba(59,130,246,.15)}
.pill-orange{background:var(--accent-dim);color:var(--accent);border:1px solid var(--accent-border)}
.pill-red{background:rgba(239,68,68,.1);color:var(--red);border:1px solid rgba(239,68,68,.15)}
.pill-gray{background:var(--surface2);color:var(--tx3);border:1px solid var(--border)}
.metric-row{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:20px}
.metric{background:var(--surface2);border:1px solid var(--border);border-radius:var(--r);padding:14px;text-align:center}
.metric-val{font-family:'JetBrains Mono',monospace;font-size:20px;font-weight:500;line-height:1}
.metric-lbl{font-size:10px;color:var(--tx3);margin-top:5px;text-transform:uppercase;letter-spacing:.06em}
.state-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-bottom:20px}
.state-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:12px;transition:border-color .15s;cursor:default}
.state-card:hover{border-color:var(--accent)}
.state-abbr{font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:600;color:var(--tx3);margin-bottom:6px;text-transform:uppercase;letter-spacing:.05em}
.state-rev{font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:500;color:var(--tx)}
.state-orders{font-size:10px;color:var(--tx3);margin-top:2px}
::-webkit-scrollbar{width:4px;height:4px}
::-webkit-scrollbar-thumb{background:var(--border2);border-radius:2px}
::-webkit-scrollbar-thumb:hover{background:var(--tx3)}
@media(max-width:1100px){.kpi-grid{grid-template-columns:repeat(2,1fr)}.g2{grid-template-columns:1fr}.span2{grid-column:span 1}.state-grid{grid-template-columns:repeat(3,1fr)}}
</style>
</head>
<body>
<aside class="sidebar">
  <div class="sb-header">
    <div class="sb-brand">
      <div class="sb-dot"></div>
      <div>
        <div class="sb-name">Amazon India</div>
        <div class="sb-meta">analytics / dashboard</div>
      </div>
    </div>
  </div>
  <nav class="sb-nav">
    <div class="nav-group-label">Overview</div>
    <button class="nav-item active" onclick="nav('overview',this)">
      <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="1" y="1" width="6" height="6" rx="1"/><rect x="9" y="1" width="6" height="6" rx="1"/><rect x="1" y="9" width="6" height="6" rx="1"/><rect x="9" y="9" width="6" height="6" rx="1"/></svg>
      Overview
    </button>
    <button class="nav-item" onclick="nav('sales',this)">
      <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><polyline points="1,12 5,7 9,9 15,3"/><polyline points="11,3 15,3 15,7"/></svg>
      Sales &amp; Profit
    </button>
    <button class="nav-item" onclick="nav('products',this)">
      <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="2" width="12" height="12" rx="1.5"/><line x1="5" y1="6" x2="11" y2="6"/><line x1="5" y1="9" x2="9" y2="9"/></svg>
      Products
    </button>
    <button class="nav-item" onclick="nav('orders',this)">
      <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><polyline points="6,8 8,10 11,6"/></svg>
      Orders &amp; Status
    </button>
    <div class="nav-group-label">Operations</div>
    <button class="nav-item" onclick="nav('payments',this)">
      <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="1" y="3" width="14" height="10" rx="1.5"/><line x1="1" y1="7" x2="15" y2="7"/><line x1="4" y1="10.5" x2="7" y2="10.5"/></svg>
      Payments
    </button>
    <button class="nav-item" onclick="nav('fulfillment',this)">
      <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="1" y="5" width="10" height="8" rx="1"/><polyline points="11,7 15,7 15,13 11,13"/><circle cx="4" cy="13" r="1.5"/><circle cx="12" cy="13" r="1.5"/></svg>
      Fulfillment
    </button>
    <button class="nav-item" onclick="nav('geography',this)">
      <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="8" cy="8" r="6"/><path d="M2,8 Q5,5 8,8 Q11,11 14,8"/><line x1="8" y1="2" x2="8" y2="14"/></svg>
      Geography
    </button>
  </nav>
  <div class="sb-footer">
    <div class="sb-stats">
      <div class="sb-stat"><div class="sb-stat-val">10K</div><div class="sb-stat-lbl">orders</div></div>
      <div class="sb-stat"><div class="sb-stat-val">32mo</div><div class="sb-stat-lbl">range</div></div>
      <div class="sb-stat"><div class="sb-stat-val">5</div><div class="sb-stat-lbl">categories</div></div>
      <div class="sb-stat"><div class="sb-stat-val">10</div><div class="sb-stat-lbl">states</div></div>
    </div>
  </div>
</aside>

<main class="main">
  <header class="topbar">
    <div class="tb-breadcrumb">
      <span class="tb-bc-root">amazon-india</span>
      <span class="tb-bc-sep">/</span>
      <span class="tb-bc-current" id="bc-current">overview</span>
    </div>
    <div class="tb-right">
      <div class="filter-wrap">
        <span class="filter-label">year=</span>
        <select class="filter-sel" id="yf" onchange="applyF()">
          <option value="all">all</option>
          <option value="2024">2024</option>
          <option value="2025">2025</option>
          <option value="2026">2026</option>
        </select>
      </div>
      <div class="filter-wrap">
        <span class="filter-label">cat=</span>
        <select class="filter-sel" id="cf" onchange="applyF()">
          <option value="all">all</option>
          <option value="Electronics">electronics</option>
          <option value="Apparel">apparel</option>
          <option value="Home">home</option>
          <option value="Beauty">beauty</option>
          <option value="Groceries">groceries</option>
        </select>
      </div>
      <span class="status-dot"></span>
      <span class="status-label">10,000 records loaded</span>
    </div>
  </header>

  <div class="content">

<section id="sec-overview" class="sec active">
  <div class="sec-header">
    <div class="sec-title">Overview</div>
    <div class="sec-desc">kpi summary &middot; jan 2024 &ndash; aug 2026 &middot; all categories</div>
  </div>
  <div class="kpi-grid">
    <div class="kpi"><div class="kpi-label">Total Revenue</div><div class="kpi-val" id="kv-rev">&#8377;15.58 Cr</div><div class="kpi-sub">gross sales, all categories</div><span class="kpi-tag tag-accent">+growing YoY</span></div>
    <div class="kpi"><div class="kpi-label">Net Profit</div><div class="kpi-val" id="kv-prf">&#8377;3.32 Cr</div><div class="kpi-sub">21.3% margin</div><span class="kpi-tag tag-up">+21.3%</span></div>
    <div class="kpi"><div class="kpi-label">Total Orders</div><div class="kpi-val" id="kv-ord">10,000</div><div class="kpi-sub">32 months data</div><span class="kpi-tag tag-up">81.5% delivered</span></div>
    <div class="kpi"><div class="kpi-label">Avg Order Value</div><div class="kpi-val" id="kv-aov">&#8377;15,579</div><div class="kpi-sub">per order</div><span class="kpi-tag tag-accent">high value</span></div>
    <div class="kpi"><div class="kpi-label">Return Rate</div><div class="kpi-val">4.85%</div><div class="kpi-sub">485 returned orders</div><span class="kpi-tag tag-dn">watch</span></div>
    <div class="kpi"><div class="kpi-label">Cancel Rate</div><div class="kpi-val">5.00%</div><div class="kpi-sub">500 cancelled</div><span class="kpi-tag tag-dn">monitor</span></div>
    <div class="kpi"><div class="kpi-label">FBA Share</div><div class="kpi-val">70.5%</div><div class="kpi-sub">7,054 via Amazon FBA</div><span class="kpi-tag tag-up">dominant</span></div>
    <div class="kpi"><div class="kpi-label">UPI Adoption</div><div class="kpi-val">49.7%</div><div class="kpi-sub">4,972 UPI payments</div><span class="kpi-tag tag-up">#1 method</span></div>
  </div>
  <div class="grid" style="grid-template-columns:1fr;margin-bottom:12px">
    <div class="card"><div class="card-header"><div><div class="card-title">Revenue &amp; Profit &mdash; Monthly Trend</div><div class="card-sub">jan 2024 &ndash; aug 2026 &middot; 32 months</div></div><span class="card-tag">line chart</span></div><div class="chart-wrap" style="height:240px"><canvas id="c-ov-trend"></canvas></div></div>
  </div>
  <div class="grid g2">
    <div class="card"><div class="card-header"><div><div class="card-title">Revenue by Category</div><div class="card-sub">share of &#8377;15.58 Cr total</div></div><span class="card-tag">donut</span></div><div class="chart-wrap" style="height:220px"><canvas id="c-ov-cat"></canvas></div></div>
    <div class="card"><div class="card-header"><div><div class="card-title">Order Status</div><div class="card-sub">10,000 orders breakdown</div></div><span class="card-tag">pie</span></div><div class="chart-wrap" style="height:220px"><canvas id="c-ov-status"></canvas></div></div>
  </div>
</section>

<section id="sec-sales" class="sec">
  <div class="sec-header"><div class="sec-title">Sales &amp; Profit</div><div class="sec-desc">revenue trends, margins, category performance</div></div>
  <div class="grid" style="grid-template-columns:1fr;margin-bottom:12px">
    <div class="card"><div class="card-header"><div><div class="card-title">Monthly Sales vs Profit</div><div class="card-sub">32 months &middot; &#8377; in thousands</div></div><span class="card-tag">bar + line</span></div><div class="chart-wrap" style="height:260px"><canvas id="c-sal-trend"></canvas></div></div>
  </div>
  <div class="grid g2" style="margin-bottom:12px">
    <div class="card"><div class="card-header"><div><div class="card-title">Category Comparison</div><div class="card-sub">revenue vs profit per category</div></div><span class="card-tag">grouped bar</span></div><div class="chart-wrap" style="height:220px"><canvas id="c-sal-cat"></canvas></div></div>
    <div class="card"><div class="card-header"><div><div class="card-title">Profit Margin</div><div class="card-sub">net margin % by category</div></div><span class="card-tag">h-bar</span></div><div class="chart-wrap" style="height:220px"><canvas id="c-sal-margin"></canvas></div></div>
  </div>
  <div class="card">
    <div class="card-header"><div><div class="card-title">Category Performance</div><div class="card-sub">ranked by revenue</div></div></div>
    <table><thead><tr><th>#</th><th>Category</th><th>Orders</th><th>Revenue</th><th>Profit</th><th>Margin</th><th>Share</th></tr></thead><tbody id="t-cat"></tbody></table>
  </div>
</section>

<section id="sec-products" class="sec">
  <div class="sec-header"><div class="sec-title">Products</div><div class="sec-desc">top performers, revenue leaders</div></div>
  <div class="grid" style="grid-template-columns:1fr;margin-bottom:12px">
    <div class="card"><div class="card-header"><div><div class="card-title">Top 10 Products by Revenue</div><div class="card-sub">all-time revenue ranking</div></div><span class="card-tag">h-bar</span></div><div class="chart-wrap" style="height:280px"><canvas id="c-prod-top"></canvas></div></div>
  </div>
  <div class="card">
    <div class="card-header"><div><div class="card-title">Product Rankings</div><div class="card-sub">top 15 by revenue</div></div></div>
    <table><thead><tr><th>Rank</th><th>Product</th><th>Orders</th><th>Revenue</th><th>Avg / Order</th><th>Share</th><th>Bar</th></tr></thead><tbody id="t-prod"></tbody></table>
  </div>
</section>

<section id="sec-orders" class="sec">
  <div class="sec-header"><div class="sec-title">Orders &amp; Status</div><div class="sec-desc">delivery performance, order lifecycle</div></div>
  <div class="metric-row">
    <div class="metric"><div class="metric-val" style="color:var(--green)">8,147</div><div class="metric-lbl">Delivered</div></div>
    <div class="metric"><div class="metric-val" style="color:var(--blue)">868</div><div class="metric-lbl">Shipped / In Transit</div></div>
    <div class="metric"><div class="metric-val" style="color:var(--red)">985</div><div class="metric-lbl">Returned + Cancelled</div></div>
  </div>
  <div class="grid g2" style="margin-bottom:12px">
    <div class="card"><div class="card-header"><div><div class="card-title">Order Status</div><div class="card-sub">lifecycle distribution</div></div><span class="card-tag">doughnut</span></div><div class="chart-wrap" style="height:220px"><canvas id="c-ord-status"></canvas></div>
      <div style="display:flex;gap:12px;margin-top:12px;flex-wrap:wrap">
        <span class="pill pill-green">Delivered 81.5%</span>
        <span class="pill pill-blue">Shipped 8.7%</span>
        <span class="pill pill-gray">Returned 4.9%</span>
        <span class="pill pill-red">Cancelled 5.0%</span>
      </div>
    </div>
    <div class="card"><div class="card-header"><div><div class="card-title">Monthly Volume</div><div class="card-sub">orders per month</div></div><span class="card-tag">line</span></div><div class="chart-wrap" style="height:220px"><canvas id="c-ord-monthly"></canvas></div></div>
  </div>
  <div class="card"><div class="card-header"><div><div class="card-title">Status by Category</div><div class="card-sub">delivery success per category</div></div><span class="card-tag">stacked bar</span></div><div class="chart-wrap" style="height:220px"><canvas id="c-ord-cat"></canvas></div></div>
</section>

<section id="sec-payments" class="sec">
  <div class="sec-header"><div class="sec-title">Payments</div><div class="sec-desc">payment method distribution &amp; preferences</div></div>
  <div class="kpi-grid">
    <div class="kpi"><div class="kpi-label">UPI</div><div class="kpi-val">4,972</div><div class="kpi-sub">49.7% share</div><span class="kpi-tag tag-up">#1 method</span></div>
    <div class="kpi"><div class="kpi-label">Credit / Debit Card</div><div class="kpi-val">2,074</div><div class="kpi-sub">20.7% share</div><span class="kpi-tag tag-accent">2nd rank</span></div>
    <div class="kpi"><div class="kpi-label">Cash on Delivery</div><div class="kpi-val">1,458</div><div class="kpi-sub">14.6% share</div><span class="kpi-tag tag-dn">declining</span></div>
    <div class="kpi"><div class="kpi-label">Net Banking</div><div class="kpi-val">1,024</div><div class="kpi-sub">10.2% share</div><span class="kpi-tag tag-dn">traditional</span></div>
  </div>
  <div class="grid g2" style="margin-bottom:12px">
    <div class="card"><div class="card-header"><div><div class="card-title">Payment Distribution</div><div class="card-sub">polar area</div></div><span class="card-tag">polar</span></div><div class="chart-wrap" style="height:240px"><canvas id="c-pay-polar"></canvas></div></div>
    <div class="card"><div class="card-header"><div><div class="card-title">Payment by Volume</div><div class="card-sub">order count ranked</div></div><span class="card-tag">h-bar</span></div><div class="chart-wrap" style="height:240px"><canvas id="c-pay-bar"></canvas></div></div>
  </div>
  <div class="card">
    <div class="card-header"><div><div class="card-title">Payment Summary</div><div class="card-sub">all methods</div></div></div>
    <table><thead><tr><th>#</th><th>Method</th><th>Orders</th><th>Share</th><th>Volume</th><th>Type</th></tr></thead><tbody id="t-pay"></tbody></table>
  </div>
</section>

<section id="sec-fulfillment" class="sec">
  <div class="sec-header"><div class="sec-title">Fulfillment</div><div class="sec-desc">channel performance &amp; logistics breakdown</div></div>
  <div class="metric-row">
    <div class="metric" style="border-color:rgba(255,153,0,.2)"><div class="metric-val" style="color:var(--accent)">7,054</div><div class="metric-lbl">Amazon FBA &mdash; 70.5%</div></div>
    <div class="metric" style="border-color:rgba(59,130,246,.2)"><div class="metric-val" style="color:var(--blue)">1,966</div><div class="metric-lbl">Seller Flex &mdash; 19.7%</div></div>
    <div class="metric"><div class="metric-val" style="color:var(--tx2)">980</div><div class="metric-lbl">Merchant FBM &mdash; 9.8%</div></div>
  </div>
  <div class="grid g2" style="margin-bottom:12px">
    <div class="card"><div class="card-header"><div><div class="card-title">Channel Mix</div><div class="card-sub">proportion of order types</div></div><span class="card-tag">doughnut</span></div><div class="chart-wrap" style="height:240px"><canvas id="c-ful-pie"></canvas></div></div>
    <div class="card"><div class="card-header"><div><div class="card-title">Channel vs Status</div><div class="card-sub">delivery success by channel</div></div><span class="card-tag">stacked bar</span></div><div class="chart-wrap" style="height:240px"><canvas id="c-ful-status"></canvas></div></div>
  </div>
</section>

<section id="sec-geography" class="sec">
  <div class="sec-header"><div class="sec-title">Geography</div><div class="sec-desc">state-wise performance across india</div></div>
  <div class="state-grid" id="state-grid"></div>
  <div class="grid" style="grid-template-columns:1fr;margin-bottom:12px">
    <div class="card"><div class="card-header"><div><div class="card-title">State Revenue Ranking</div><div class="card-sub">top 10 states</div></div><span class="card-tag">h-bar</span></div><div class="chart-wrap" style="height:300px"><canvas id="c-geo-bar"></canvas></div></div>
  </div>
  <div class="card">
    <div class="card-header"><div><div class="card-title">State Performance</div><div class="card-sub">sorted by revenue</div></div></div>
    <table><thead><tr><th>#</th><th>State</th><th>Orders</th><th>Revenue</th><th>Profit</th><th>Margin</th><th>Share</th></tr></thead><tbody id="t-state"></tbody></table>
  </div>
</section>

  </div>
</main>
<script>
const MD=[
  {m:'2024-01',s:4441265.57,p:1016530.29,o:316},{m:'2024-02',s:4071073.66,p:778165.74,o:265},
  {m:'2024-03',s:5761054.84,p:1243584.05,o:310},{m:'2024-04',s:4612546.48,p:1041978.73,o:326},
  {m:'2024-05',s:4660178.05,p:1020331.21,o:324},{m:'2024-06',s:4810938.17,p:937123.34,o:311},
  {m:'2024-07',s:5744760.13,p:1256434.89,o:328},{m:'2024-08',s:4760372.35,p:976600.73,o:315},
  {m:'2024-09',s:4033814.56,p:914060.89,o:303},{m:'2024-10',s:4820971.84,p:1033414.57,o:311},
  {m:'2024-11',s:4483427.16,p:867487.80,o:281},{m:'2024-12',s:4812417.32,p:1045396.92,o:315},
  {m:'2025-01',s:4606206.73,p:945448.74,o:317},{m:'2025-02',s:4311299.81,p:849842.38,o:275},
  {m:'2025-03',s:5197449.69,p:1109671.45,o:335},{m:'2025-04',s:3889801.47,p:866003.41,o:280},
  {m:'2025-05',s:5390320.66,p:1108438.96,o:333},{m:'2025-06',s:4691064.39,p:1037380.01,o:305},
  {m:'2025-07',s:5548031.92,p:1147269.68,o:341},{m:'2025-08',s:4825647.41,p:995098.14,o:296},
  {m:'2025-09',s:4645851.23,p:978708.78,o:320},{m:'2025-10',s:4786859.11,p:983414.48,o:340},
  {m:'2025-11',s:5110161.44,p:1197245.96,o:316},{m:'2025-12',s:4424179.17,p:983901.42,o:286},
  {m:'2026-01',s:4907181.04,p:1068832.87,o:304},{m:'2026-02',s:4324986.58,p:906184.52,o:268},
  {m:'2026-03',s:4854721.92,p:1074182.43,o:314},{m:'2026-04',s:5193546.45,p:1089945.17,o:329},
  {m:'2026-05',s:4795167.11,p:1057988.22,o:315},{m:'2026-06',s:5767141.03,p:1222177.09,o:331},
  {m:'2026-07',s:6443679.00,p:1329442.03,o:374},{m:'2026-08',s:5063777.60,p:1084723.59,o:316}
];
const CD=[
  {c:'Apparel & Fashion',     s:9831025.09,  p:2085354.00,  o:2580},
  {c:'Beauty & Personal Care',s:2889178.50,  p:604390.41,   o:1499},
  {c:'Electronics & Mobiles', s:123569507.07,p:26310257.24, o:3045},
  {c:'Home & Kitchen',        s:17973218.93, p:3837268.36,  o:1888},
  {c:'Pantry & Groceries',    s:1526964.30,  p:329738.48,   o:988}
];
const PD=[
  {n:'Laptop Backpack',             s:26529187.41,o:652},
  {n:'Power Bank 20000mAh',         s:25548449.07,o:634},
  {n:'5G Smartphone',               s:24330766.23,o:596},
  {n:'Wireless Earbuds',            s:23848640.89,o:603},
  {n:'Smartwatch',                  s:23312463.47,o:560},
  {n:'Stainless Steel Dinner Set',  s:3865114.25, o:390},
  {n:'Cotton Bedsheet Double',      s:3789133.82, o:401},
  {n:'Water Purifier',              s:3785924.80, o:400},
  {n:'Induction Cooktop',           s:3510999.56, o:361},
  {n:'Mixer Grinder 750W',          s:3022046.50, o:336},
  {n:'Sports Shoes',                s:2034983.60, o:538},
  {n:'Men Denim Jeans',             s:2000867.28, o:516},
  {n:'Cotton Kurta Set',            s:1971599.27, o:512},
  {n:'Saree with Unstitched Blouse',s:1944962.97, o:515},
  {n:'Printed T-Shirt',             s:1878611.97, o:499}
];
const STDATA={Delivered:8147,Shipped:868,Returned:485,Cancelled:500};
const PAY={'UPI':4972,'Credit/Debit Card':2074,'Cash on Delivery (COD)':1458,'Net Banking':1024,'Amazon Pay Later':472};
const FUL={'Amazon (FBA)':7054,'Seller Flex':1966,'Merchant (FBM)':980};
const GD=[
  {st:'Maharashtra', ab:'MH',s:29554237.21,p:6301731.56,o:1840},
  {st:'Karnataka',   ab:'KA',s:24415704.16,p:5273235.35,o:1515},
  {st:'Delhi',       ab:'DL',s:22361687.04,p:4699095.38,o:1444},
  {st:'Tamil Nadu',  ab:'TN',s:17889855.25,p:3856864.11,o:1109},
  {st:'Uttar Pradesh',ab:'UP',s:14140675.36,p:2978266.81,o:991},
  {st:'Telangana',   ab:'TG',s:13961458.53,p:2944127.16,o:906},
  {st:'West Bengal', ab:'WB',s:10864550.51,p:2344788.08,o:665},
  {st:'Gujarat',     ab:'GJ',s:9369304.18, p:2008021.80,o:591},
  {st:'Rajasthan',   ab:'RJ',s:6620697.25, p:1383028.68,o:456},
  {st:'Kerala',      ab:'KL',s:6611724.40, p:1377849.56,o:483}
];
const FULST={
  'Amazon (FBA)':{D:5890,Sh:720,R:218,Ca:226},
  'Seller Flex':{D:1622,Sh:120,R:140,Ca:84},
  'Merchant (FBM)':{D:635,Sh:28,R:127,Ca:190}
};
const CATST={
  'Apparel & Fashion':{D:2088,Sh:220,R:156,Ca:116},
  'Beauty & Personal Care':{D:1223,Sh:130,R:72,Ca:74},
  'Electronics & Mobiles':{D:2488,Sh:298,R:138,Ca:121},
  'Home & Kitchen':{D:1545,Sh:150,R:96,Ca:97},
  'Pantry & Groceries':{D:803,Sh:70,R:23,Ca:92}
};
const TOTAL=155789893.89;

Chart.defaults.color='#555555';
Chart.defaults.borderColor='rgba(34,34,34,0.8)';
Chart.defaults.font.family="'Inter',sans-serif";
Chart.defaults.font.size=11;
Chart.defaults.plugins.legend.labels.usePointStyle=true;
Chart.defaults.plugins.legend.labels.pointStyleWidth=8;

const C={
  accent:'#FF9900',
  blue:'#3b82f6',
  green:'#22c55e',
  red:'#ef4444',
  tx2:'#888888',
  tx3:'#555555'
};
const STCOL={Delivered:C.green,Shipped:C.blue,Returned:'#888888',Cancelled:C.red};
const CATCOL=['#FF9900','#3b82f6','#888888','#555555','#333333'];

function fc(v){
  if(v>=1e7)return '\u20B9'+(v/1e7).toFixed(2)+' Cr';
  if(v>=1e5)return '\u20B9'+(v/1e5).toFixed(1)+'L';
  return '\u20B9'+v.toFixed(0);
}
function fn(v){return v.toLocaleString('en-IN');}
function ml(m){const[y,mo]=m.split('-');const mn=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];return mn[+mo-1]+"'"+y.slice(2);}

function nav(id,btn){
  document.querySelectorAll('.sec').forEach(s=>s.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(b=>b.classList.remove('active'));
  document.getElementById('sec-'+id).classList.add('active');
  btn.classList.add('active');
  const labels={overview:'overview',sales:'sales / profit',products:'products',orders:'orders / status',payments:'payments',fulfillment:'fulfillment',geography:'geography'};
  document.getElementById('bc-current').textContent=labels[id]||id;
}

function applyF(){
  const y=document.getElementById('yf').value;
  let fd=MD;
  if(y!=='all') fd=fd.filter(d=>d.m.startsWith(y));
  const ts=fd.reduce((a,d)=>a+d.s,0),tp=fd.reduce((a,d)=>a+d.p,0),to=fd.reduce((a,d)=>a+d.o,0);
  document.getElementById('kv-rev').textContent=fc(ts);
  document.getElementById('kv-prf').textContent=fc(tp);
  document.getElementById('kv-ord').textContent=fn(to);
  document.getElementById('kv-aov').textContent='\u20B9'+fn(to?Math.round(ts/to):0);
}

function buildCatTable(){
  const tot=CD.reduce((a,c)=>a+c.s,0);
  const sorted=[...CD].sort((a,b)=>b.s-a.s);
  document.getElementById('t-cat').innerHTML=sorted.map((c,i)=>{
    const mg=((c.p/c.s)*100).toFixed(1),sh=((c.s/tot)*100).toFixed(1);
    const rk=i===0?'r1':i===1?'r2':i===2?'r3':'';
    return `<tr><td><span class="rank ${rk}">${i+1}</span></td><td>${c.c}</td><td class="dim mono">${fn(c.o)}</td><td class="mono"><strong>${fc(c.s)}</strong></td><td class="mono">${fc(c.p)}</td><td class="mono" style="color:${+mg>25?C.green:+mg>20?C.accent:C.red}">${mg}%</td><td><div class="bar-wrap"><div class="bar-track"><div class="bar-fill" style="width:${sh}%"></div></div><span class="bar-pct">${sh}%</span></div></td></tr>`;
  }).join('');
}

function buildProdTable(){
  const mx=PD[0].s;
  document.getElementById('t-prod').innerHTML=PD.map((p,i)=>{
    const sh=((p.s/TOTAL)*100).toFixed(2),bw=((p.s/mx)*100).toFixed(1);
    const rk=i===0?'r1':i===1?'r2':i===2?'r3':'';
    return `<tr><td><span class="rank ${rk}">${i+1}</span></td><td>${p.n}</td><td class="dim mono">${fn(p.o)}</td><td class="mono">${fc(p.s)}</td><td class="dim mono">\u20B9${fn(Math.round(p.s/p.o))}</td><td class="bar-pct">${sh}%</td><td><div class="bar-wrap"><div class="bar-track"><div class="bar-fill${i>=5?' blue':''}" style="width:${bw}%"></div></div></div></td></tr>`;
  }).join('');
}

function buildPayTable(){
  const tot=Object.values(PAY).reduce((a,b)=>a+b,0),mx=Math.max(...Object.values(PAY));
  const types={'UPI':'digital','Credit/Debit Card':'card','Cash on Delivery (COD)':'cod','Net Banking':'online','Amazon Pay Later':'bnpl'};
  const sorted=Object.entries(PAY).sort((a,b)=>b[1]-a[1]);
  document.getElementById('t-pay').innerHTML=sorted.map(([pm,cnt],i)=>{
    const sh=((cnt/tot)*100).toFixed(1),w=((cnt/mx)*100).toFixed(1);
    const rk=i===0?'r1':i===1?'r2':i===2?'r3':'';
    const pillCls=i===0?'pill-green':i===1?'pill-blue':i===2?'pill-orange':'pill-gray';
    return `<tr><td><span class="rank ${rk}">${i+1}</span></td><td>${pm}</td><td class="mono">${fn(cnt)}</td><td class="mono">${sh}%</td><td><div class="bar-wrap"><div class="bar-track"><div class="bar-fill" style="width:${w}%"></div></div></div></td><td><span class="pill ${pillCls}">${types[pm]||'other'}</span></td></tr>`;
  }).join('');
}

function buildStateCards(){
  document.getElementById('state-grid').innerHTML=GD.map(g=>`
    <div class="state-card">
      <div class="state-abbr">${g.ab}</div>
      <div class="state-rev">${fc(g.s)}</div>
      <div class="state-orders">${fn(g.o)} orders</div>
    </div>
  `).join('');
}

function buildStateTable(){
  const mx=GD[0].s;
  document.getElementById('t-state').innerHTML=GD.map((g,i)=>{
    const mg=((g.p/g.s)*100).toFixed(1),sh=((g.s/TOTAL)*100).toFixed(1);
    const rk=i===0?'r1':i===1?'r2':i===2?'r3':'';
    return `<tr><td><span class="rank ${rk}">${i+1}</span></td><td><strong>${g.st}</strong> <span class="dim" style="font-size:10px">${g.ab}</span></td><td class="dim mono">${fn(g.o)}</td><td class="mono"><strong>${fc(g.s)}</strong></td><td class="mono">${fc(g.p)}</td><td class="mono">${mg}%</td><td><div class="bar-wrap"><div class="bar-track"><div class="bar-fill" style="width:${((g.s/mx)*100).toFixed(1)}%"></div></div><span class="bar-pct">${sh}%</span></div></td></tr>`;
  }).join('');
}

function mk(id,cfg){const el=document.getElementById(id);if(!el)return;return new Chart(el,cfg);}

const gridColor='rgba(34,34,34,0.8)';

function initCharts(){
  const lbs=MD.map(d=>ml(d.m));
  const sk=MD.map(d=>+(d.s/1000).toFixed(1));
  const pk=MD.map(d=>+(d.p/1000).toFixed(1));
  const ok=MD.map(d=>d.o);
  const baseOpts={responsive:true,maintainAspectRatio:false};

  mk('c-ov-trend',{type:'line',data:{labels:lbs,datasets:[
    {label:'Revenue (\\u20B9K)',data:sk,borderColor:C.accent,backgroundColor:'rgba(255,153,0,.05)',fill:true,tension:.35,pointRadius:0,borderWidth:1.5},
    {label:'Profit (\\u20B9K)', data:pk,borderColor:C.blue, backgroundColor:'rgba(59,130,246,.05)',fill:true,tension:.35,pointRadius:0,borderWidth:1.5}
  ]},options:{...baseOpts,plugins:{legend:{position:'top',labels:{color:'#555',font:{size:11}}}},scales:{y:{ticks:{callback:v=>'\u20B9'+v+'K',color:'#555'},grid:{color:gridColor}},x:{grid:{display:false},ticks:{color:'#555',maxRotation:45,maxTicksLimit:16}}}}});

  mk('c-ov-cat',{type:'doughnut',data:{labels:CD.map(c=>c.c),datasets:[{data:CD.map(c=>c.s),backgroundColor:CATCOL,borderColor:'#111',borderWidth:2,hoverOffset:4}]},
    options:{...baseOpts,cutout:'68%',plugins:{legend:{position:'bottom',labels:{color:'#555',font:{size:10},boxWidth:8}},tooltip:{callbacks:{label:c=>' '+fc(c.raw)+' ('+(c.raw/TOTAL*100).toFixed(1)+'%)'}}}}});

  mk('c-ov-status',{type:'pie',data:{labels:['Delivered','Shipped','Returned','Cancelled'],datasets:[{data:[8147,868,485,500],backgroundColor:[C.green,C.blue,'#555',C.red],borderColor:'#111',borderWidth:2}]},
    options:{...baseOpts,plugins:{legend:{position:'bottom',labels:{color:'#555',font:{size:10},boxWidth:8}},tooltip:{callbacks:{label:c=>' '+fn(c.raw)+' ('+(c.raw/100).toFixed(1)+'%)'}}}}});

  mk('c-sal-trend',{type:'bar',data:{labels:lbs,datasets:[
    {type:'bar', label:'Revenue (\\u20B9K)',data:sk,backgroundColor:'rgba(255,153,0,.25)',borderColor:C.accent,borderWidth:1,borderRadius:2,yAxisID:'y'},
    {type:'line',label:'Profit (\\u20B9K)', data:pk,borderColor:C.blue,backgroundColor:'transparent',tension:.35,pointRadius:0,borderWidth:1.5,yAxisID:'y'}
  ]},options:{...baseOpts,plugins:{legend:{position:'top',labels:{color:'#555',font:{size:11}}}},scales:{y:{ticks:{callback:v=>'\u20B9'+v+'K',color:'#555'},grid:{color:gridColor}},x:{grid:{display:false},ticks:{color:'#555',maxRotation:45,maxTicksLimit:16}}}}});

  const cshort={'Apparel & Fashion':'Apparel','Beauty & Personal Care':'Beauty','Electronics & Mobiles':'Electronics','Home & Kitchen':'Home & Kit.','Pantry & Groceries':'Groceries'};
  mk('c-sal-cat',{type:'bar',data:{labels:CD.map(c=>cshort[c.c]||c.c),datasets:[
    {label:'Revenue',data:CD.map(c=>+(c.s/1e6).toFixed(2)),backgroundColor:'rgba(255,153,0,.3)',borderColor:C.accent,borderWidth:1,borderRadius:3},
    {label:'Profit', data:CD.map(c=>+(c.p/1e6).toFixed(2)),backgroundColor:'rgba(59,130,246,.3)',borderColor:C.blue,borderWidth:1,borderRadius:3}
  ]},options:{...baseOpts,plugins:{legend:{position:'top',labels:{color:'#555',font:{size:11}}},tooltip:{callbacks:{label:c=>' \u20B9'+c.raw+'M'}}},scales:{y:{ticks:{callback:v=>'\u20B9'+v+'M',color:'#555'},grid:{color:gridColor}},x:{grid:{display:false},ticks:{color:'#555'}}}}});

  const mgs=CD.map(c=>+((c.p/c.s)*100).toFixed(1));
  mk('c-sal-margin',{type:'bar',data:{labels:CD.map(c=>cshort[c.c]||c.c),datasets:[{label:'Margin %',data:mgs,backgroundColor:mgs.map(m=>m>25?'rgba(34,197,94,.3)':m>20?'rgba(255,153,0,.3)':'rgba(239,68,68,.3)'),borderColor:mgs.map(m=>m>25?C.green:m>20?C.accent:C.red),borderWidth:1,borderRadius:3}]},
    options:{...baseOpts,indexAxis:'y',plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>' '+c.raw+'%'}}},scales:{x:{max:30,ticks:{callback:v=>v+'%',color:'#555'},grid:{color:gridColor}},y:{grid:{display:false},ticks:{color:'#555'}}}}});

  mk('c-ord-status',{type:'doughnut',data:{labels:['Delivered','Shipped','Returned','Cancelled'],datasets:[{data:[8147,868,485,500],backgroundColor:[C.green,C.blue,'#555',C.red],borderColor:'#111',borderWidth:2,hoverOffset:4}]},
    options:{...baseOpts,cutout:'66%',plugins:{legend:{display:false}}}});

  mk('c-ord-monthly',{type:'line',data:{labels:lbs,datasets:[{label:'Orders',data:ok,borderColor:C.accent,backgroundColor:'rgba(255,153,0,.05)',fill:true,tension:.35,pointRadius:0,borderWidth:1.5}]},
    options:{...baseOpts,plugins:{legend:{display:false}},scales:{y:{grid:{color:gridColor},ticks:{color:'#555'}},x:{grid:{display:false},ticks:{color:'#555',maxRotation:45,maxTicksLimit:16}}}}});

  const catKeys=Object.keys(CATST);
  mk('c-ord-cat',{type:'bar',data:{labels:catKeys.map(c=>cshort[c]||c),datasets:[
    {label:'Delivered',data:catKeys.map(k=>CATST[k].D), backgroundColor:'rgba(34,197,94,.4)', borderColor:C.green,borderWidth:1,borderRadius:2},
    {label:'Shipped',  data:catKeys.map(k=>CATST[k].Sh),backgroundColor:'rgba(59,130,246,.4)',  borderColor:C.blue, borderWidth:1,borderRadius:2},
    {label:'Returned', data:catKeys.map(k=>CATST[k].R), backgroundColor:'rgba(136,136,136,.4)', borderColor:'#555', borderWidth:1,borderRadius:2},
    {label:'Cancelled',data:catKeys.map(k=>CATST[k].Ca),backgroundColor:'rgba(239,68,68,.4)',   borderColor:C.red,  borderWidth:1,borderRadius:2}
  ]},options:{...baseOpts,plugins:{legend:{position:'top',labels:{color:'#555',font:{size:11}}}},scales:{x:{stacked:true,grid:{display:false},ticks:{color:'#555'}},y:{stacked:true,grid:{color:gridColor},ticks:{color:'#555'}}}}});

  mk('c-pay-polar',{type:'polarArea',data:{labels:Object.keys(PAY),datasets:[{data:Object.values(PAY),backgroundColor:['rgba(255,153,0,.35)','rgba(59,130,246,.35)','rgba(136,136,136,.35)','rgba(85,85,85,.35)','rgba(50,50,50,.5)'],borderColor:['rgba(255,153,0,.6)','rgba(59,130,246,.6)','rgba(136,136,136,.5)','rgba(85,85,85,.5)','rgba(70,70,70,.5)'],borderWidth:1}]},
    options:{...baseOpts,plugins:{legend:{position:'bottom',labels:{color:'#555',font:{size:10},boxWidth:8}}}}});

  mk('c-pay-bar',{type:'bar',data:{labels:Object.keys(PAY),datasets:[{label:'Orders',data:Object.values(PAY),backgroundColor:'rgba(255,153,0,.2)',borderColor:C.accent,borderWidth:1,borderRadius:4}]},
    options:{...baseOpts,indexAxis:'y',plugins:{legend:{display:false}},scales:{x:{grid:{color:gridColor},ticks:{color:'#555'}},y:{grid:{display:false},ticks:{color:'#555'}}}}});

  mk('c-ful-pie',{type:'doughnut',data:{labels:Object.keys(FUL),datasets:[{data:Object.values(FUL),backgroundColor:['rgba(255,153,0,.35)','rgba(59,130,246,.35)','rgba(136,136,136,.3)'],borderColor:['rgba(255,153,0,.7)','rgba(59,130,246,.7)','rgba(136,136,136,.5)'],borderWidth:1,hoverOffset:4}]},
    options:{...baseOpts,cutout:'60%',plugins:{legend:{position:'bottom',labels:{color:'#555',font:{size:11},boxWidth:8}},tooltip:{callbacks:{label:c=>' '+fn(c.raw)+' ('+(c.raw/100).toFixed(1)+'%)'}}}}});

  const fls=Object.keys(FULST);
  mk('c-ful-status',{type:'bar',data:{labels:fls,datasets:[
    {label:'Delivered',data:fls.map(f=>FULST[f].D), backgroundColor:'rgba(34,197,94,.4)', borderColor:C.green,borderWidth:1,borderRadius:3},
    {label:'Shipped',  data:fls.map(f=>FULST[f].Sh),backgroundColor:'rgba(59,130,246,.4)',  borderColor:C.blue, borderWidth:1,borderRadius:3},
    {label:'Returned', data:fls.map(f=>FULST[f].R), backgroundColor:'rgba(136,136,136,.4)', borderColor:'#555', borderWidth:1,borderRadius:3},
    {label:'Cancelled',data:fls.map(f=>FULST[f].Ca),backgroundColor:'rgba(239,68,68,.4)',   borderColor:C.red,  borderWidth:1,borderRadius:3}
  ]},options:{...baseOpts,plugins:{legend:{position:'top',labels:{color:'#555',font:{size:11}}}},scales:{x:{stacked:true,grid:{display:false},ticks:{color:'#555'}},y:{stacked:true,grid:{color:gridColor},ticks:{color:'#555'}}}}});

  const top10=PD.slice(0,10);
  mk('c-prod-top',{type:'bar',data:{labels:top10.map(p=>p.n),datasets:[{label:'Revenue (\\u20B9Cr)',data:top10.map(p=>+(p.s/1e7).toFixed(2)),backgroundColor:top10.map((_,i)=>i<5?'rgba(255,153,0,.3)':'rgba(59,130,246,.2)'),borderColor:top10.map((_,i)=>i<5?C.accent:C.blue),borderWidth:1,borderRadius:4}]},
    options:{...baseOpts,indexAxis:'y',plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>' \u20B9'+c.raw+' Cr'}}},scales:{x:{ticks:{callback:v=>'\u20B9'+v+' Cr',color:'#555'},grid:{color:gridColor}},y:{grid:{display:false},ticks:{color:'#888',font:{size:11}}}}}});

  mk('c-geo-bar',{type:'bar',data:{labels:GD.map(g=>g.st),datasets:[
    {label:'Revenue (\\u20B9Cr)',data:GD.map(g=>+(g.s/1e7).toFixed(2)),backgroundColor:'rgba(255,153,0,.25)',borderColor:C.accent,borderWidth:1,borderRadius:3},
    {label:'Profit (\\u20B9Cr)', data:GD.map(g=>+(g.p/1e7).toFixed(2)),backgroundColor:'rgba(59,130,246,.2)', borderColor:C.blue, borderWidth:1,borderRadius:3}
  ]},options:{...baseOpts,indexAxis:'y',plugins:{legend:{position:'top',labels:{color:'#555',font:{size:11}}}},scales:{x:{ticks:{callback:v=>'\u20B9'+v+' Cr',color:'#555'},grid:{color:gridColor}},y:{grid:{display:false},ticks:{color:'#888'}}}}});
}

document.addEventListener('DOMContentLoaded',()=>{
  buildCatTable();buildProdTable();buildPayTable();buildStateCards();buildStateTable();initCharts();
});
</script>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done:', len(html), 'bytes')
