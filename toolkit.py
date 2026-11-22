VERSION = "v0.2"

def division():
    """Prints a line of 30 '=' for the report."""
    print("="*30)

def section():
    """Prints a line of 30 '-' for the report."""
    print("-"*30)

def clean_sku(sku):
    """Returns the SKU in uppercase, or 'INVALID SKU' if it's empty."""
    if sku == "":
        return "INVALID SKU"
    else:
        return sku.upper()

def days_of_supply(on_hand, avg_daily_demand):
    """Returns how many days the stock will last, rounded to 1 decimal."""
    dos = round(on_hand / avg_daily_demand,1)
    return dos

def safety_stock(max_daily_demand, max_lead_time, avg_daily_demand, avg_lead_time):
    """Returns safety stock using the Max-Average method: worst case minus normal case."""
    ss = (max_daily_demand * max_lead_time) - (avg_daily_demand * avg_lead_time)
    return ss

def reorder_point(avg_daily_demand, avg_lead_time, safety_stock_qty):
    """Returns the stock level that should trigger a new order."""
    ro = avg_daily_demand * avg_lead_time + safety_stock_qty
    return ro

def needs_reorder(on_hand, reorder_point_qty):
    """Returns True if on hand is at or below the reorder point, otherwise False."""
    if on_hand <= reorder_point_qty:
        return True
    else:
        return False

def stock_status(days_of_supply_qty, avg_lead_time):
    """Returns 'At risk' if stock runs out before the lead time, otherwise 'Ok'."""
    if days_of_supply_qty < avg_lead_time:
        return "At risk"
    else:
        return "Ok"

def landed_cost_per_unit(unit_price, quantity, freight, duty_rate):
    """Returns the real cost per unit including freight and duty (not rounded)."""
    product_cost = unit_price * quantity
    duty = product_cost * duty_rate
    landed_total = product_cost + freight + duty
    landed_per_unit = landed_total / quantity
    return landed_per_unit

sample_sku = {
    "sku":"lbl-5160",
    "on_hand" : 850,
    "avg_demand" : 100,
    "max_demand" : 130,
    "avg_lead_time" : 5,
    "max_lead_time" : 7,
    "unit_price" : 2.00,
    "order_qty": 5000,
    "freight" : 3000,
    "duty_rate" : 0.10 
}

clean_SKU = clean_sku(sample_sku["sku"])
days = days_of_supply(sample_sku["on_hand"], sample_sku["avg_demand"])
s_stock = safety_stock(sample_sku["max_demand"],sample_sku["max_lead_time"],sample_sku["avg_demand"],sample_sku["avg_lead_time"])
r_point = reorder_point(sample_sku["avg_demand"],sample_sku["avg_lead_time"], s_stock)
reorder_flag = needs_reorder(sample_sku["on_hand"],r_point)
status_text = stock_status(days, sample_sku["avg_lead_time"])
landed_cost =landed_cost_per_unit(sample_sku["unit_price"], sample_sku["order_qty"], sample_sku["freight"], sample_sku["duty_rate"])

increase_vs_price_pct = round((landed_cost - sample_sku["unit_price"]) / sample_sku['unit_price'] * 100,1)
if reorder_flag is True:
    reorder_text = "Yes"
else:
    reorder_text = "No"

#Printing Report
division()
print(f"INVENTORY PLANNING TOOLKIT {VERSION}" )
division()
print(f"SKU: {clean_SKU}")
section()
print(f"On hand: {sample_sku['on_hand']} boxes\nDays of supply: {days} · {status_text}\nSafety stock: {s_stock} boxes\nReorder point: {r_point} boxes\nReorder needed: {reorder_text}")
section()
print(f"Landed cost per unit: ${round(landed_cost,2)} (quote ${sample_sku['unit_price']}, +{increase_vs_price_pct}%)")
division()