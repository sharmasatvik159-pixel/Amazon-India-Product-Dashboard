# Amazon India Sales Dashboard

Interactive business intelligence dashboard built from **10,000 Amazon India orders** (Jan 2024 – Aug 2026).

## Live Preview

Open `index.html` in any browser — no server or build step required.

## Features

| Section | Metrics |
|---|---|
| Overview | 8 KPIs — Revenue, Profit, AOV, Return Rate, FBA Share, UPI Adoption |
| Sales & Profit | Monthly trend (32mo), category comparison, profit margins |
| Products | Top 15 products by revenue, ranked table |
| Orders & Status | Delivery rate, monthly volume, status by category |
| Payments | UPI / Card / COD / Net Banking breakdown |
| Fulfillment | FBA vs Seller Flex vs Merchant FBM |
| Geography | Top 10 states — revenue, profit, margins |

## Data

Source: `Amazon Sales Data India.xlsx`

| Field | Detail |
|---|---|
| Orders | 10,000 |
| Date Range | Jan 2024 – Aug 2026 |
| Categories | 5 (Electronics, Apparel, Home & Kitchen, Beauty, Groceries) |
| States | 10 |
| Total Revenue | ₹15.58 Cr |
| Net Profit | ₹3.32 Cr |
| Profit Margin | 21.3% |

## Stack

- HTML + Vanilla CSS + JavaScript
- [Chart.js 4.4.2](https://www.chartjs.org/) — all charts
- [Inter](https://fonts.google.com/specimen/Inter) + [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) — typography
- `analyse.py` — data extraction from xlsx (Python + openpyxl)
- `gen_dashboard.py` — generates `index.html` from extracted data

## Usage

```bash
# Just open in browser
start index.html

# Re-extract data from xlsx (requires Python + openpyxl)
pip install openpyxl
python analyse.py

# Regenerate the dashboard HTML
python gen_dashboard.py
```

## Key Insights

- **Electronics & Mobiles** — 79% of total revenue (₹12.36 Cr)
- **Laptop Backpack** — top product at ₹2.65 Cr revenue
- **Maharashtra** — #1 state, ₹2.96 Cr, 1,840 orders
- **UPI** — 49.7% of all payments, dominant method
- **Amazon FBA** — 70.5% fulfillment share
- **81.5%** overall delivery success rate
