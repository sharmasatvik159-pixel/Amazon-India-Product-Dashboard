import openpyxl
import json
from collections import defaultdict, Counter

wb = openpyxl.load_workbook('Amazon Sales Data India.xlsx', read_only=True)
ws = wb['Sheet1']
rows = list(ws.iter_rows(values_only=True))
headers = rows[0]
data = [dict(zip(headers, row)) for row in rows[1:]]

def parse_ym(date_str):
    parts = date_str.split('-')
    return f'{parts[0]}-{parts[1]}'

monthly = defaultdict(lambda: {'sales': 0.0, 'profit': 0.0, 'orders': 0})
for r in data:
    d = r['Order_Date']
    key = parse_ym(d)
    monthly[key]['sales'] += r['Total_Sales_INR'] or 0
    monthly[key]['profit'] += r['Profit_INR'] or 0
    monthly[key]['orders'] += 1

monthly_sorted = sorted(monthly.items())
print('Monthly:')
for k, v in monthly_sorted:
    print(f"  {k}: sales={round(v['sales'],2)}, profit={round(v['profit'],2)}, orders={v['orders']}")

cat_data = defaultdict(lambda: {'sales': 0.0, 'profit': 0.0, 'orders': 0})
for r in data:
    cat_data[r['Category']]['sales'] += r['Total_Sales_INR'] or 0
    cat_data[r['Category']]['profit'] += r['Profit_INR'] or 0
    cat_data[r['Category']]['orders'] += 1

print('\nCategory:')
for cat, v in sorted(cat_data.items()):
    print(f"  {cat}: sales={round(v['sales'],2)}, profit={round(v['profit'],2)}, orders={v['orders']}")

prod_data = defaultdict(lambda: {'sales': 0.0, 'profit': 0.0, 'orders': 0})
for r in data:
    prod_data[r['Product']]['sales'] += r['Total_Sales_INR'] or 0
    prod_data[r['Product']]['profit'] += r['Profit_INR'] or 0
    prod_data[r['Product']]['orders'] += 1

top_prods = sorted(prod_data.items(), key=lambda x: x[1]['sales'], reverse=True)[:15]
print('\nTop 15 products:')
for p, v in top_prods:
    print(f"  {p}: sales={round(v['sales'],2)}, orders={v['orders']}")

state_data = defaultdict(lambda: {'sales': 0.0, 'profit': 0.0, 'orders': 0})
for r in data:
    state_data[r['Ship_State']]['sales'] += r['Total_Sales_INR'] or 0
    state_data[r['Ship_State']]['profit'] += r['Profit_INR'] or 0
    state_data[r['Ship_State']]['orders'] += 1

print('\nAll states (by sales):')
for st, v in sorted(state_data.items(), key=lambda x: x[1]['sales'], reverse=True):
    print(f"  {st}: sales={round(v['sales'],2)}, profit={round(v['profit'],2)}, orders={v['orders']}")

payments = Counter(r['Payment_Method'] for r in data)
print('\nPayments:', dict(payments))

fulfillments = Counter(r['Fulfillment'] for r in data)
print('Fulfillment:', dict(fulfillments))

statuses = Counter(r['Order_Status'] for r in data)
print('Status:', dict(statuses))

avg_discount = sum(r['Discount_Pct'] for r in data if r['Discount_Pct']) / len(data)
print(f'Avg discount: {avg_discount:.3f}')
print(f'Total orders: {len(data)}')
print(f'Total sales: {round(sum(r["Total_Sales_INR"] or 0 for r in data), 2)}')
print(f'Total profit: {round(sum(r["Profit_INR"] or 0 for r in data), 2)}')
