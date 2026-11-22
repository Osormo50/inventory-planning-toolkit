# Inventory Planning Toolkit

A Python toolkit that helps a supply planner decide **when to order, how much stock to keep, and what an item really costs**. Built step by step while learning Python: each new version adds features using what I've just learned.

> Data in this project is made up for learning purposes.

## Features

| Status | Feature | Version |
|---|---|---|
| ✅ | SKU cleanup (uppercase, invalid check) | v0.2 |
| ✅ | Days of supply | v0.2 |
| ✅ | Safety stock (Max–Average method) | v0.2 |
| ✅ | Reorder point and reorder flag | v0.2 |
| ✅ | Stock status vs lead time | v0.2 |
| ✅ | Landed cost per unit (price + freight + duty) | v0.2 |

## Supply chain concepts and formulas

### Days of supply
How long current stock will last.
```
Days of supply = On hand ÷ Avg daily demand
```

### Safety stock (Max–Average method)
Buffer that covers a high-demand period **and** a late delivery at the same time.
```
Safety stock = (Max daily demand × Max lead time) − (Avg daily demand × Avg lead time)
```

### Reorder point
The stock level that should trigger a new purchase order.
```
Reorder point = Avg daily demand × Avg lead time + Safety stock
Reorder needed = On hand ≤ Reorder point
```

### Stock status
```
At risk  if Days of supply < Avg lead time   (runs out before a new truck can arrive)
Ok       otherwise
```

### Landed cost
The real cost per unit once freight and import duty are included.
```
Product cost    = Unit price × Quantity
Duty            = Product cost × Duty rate
Landed per unit = (Product cost + Freight + Duty) ÷ Quantity
Increase %      = (Landed per unit − Unit price) ÷ Unit price × 100
```

## Sample output

```
==============================
INVENTORY PLANNING TOOLKIT v0.2
==============================
SKU: LBL-5160
------------------------------
On hand: 850 boxes
Days of supply: 8.5 · Ok
Safety stock: 410 boxes
Reorder point: 910 boxes
Reorder needed: Yes
------------------------------
Landed cost per unit: $2.8 (quote $2.0, +40.0%)
==============================
```

**Why "Ok" and "Reorder needed: Yes" at the same time?** They answer different questions. Status asks whether stock runs out before a truck could arrive (8.5 days vs a 5-day lead time: no). Reorder asks whether it's time to order to protect the safety stock (850 ≤ 910: yes). Ordering now is what keeps the status Ok.

## Test scenarios

| Change to sample SKU | Days of supply | Status | Reorder needed | Landed cost |
|---|---|---|---|---|
| Base (on hand 850) | 8.5 | Ok | Yes | $2.8 (+40.0%) |
| On hand 950 | 9.5 | Ok | No | $2.8 |
| On hand 910 (edge) | 9.1 | Ok | Yes | $2.8 |
| On hand 400 | 4.0 | At risk | Yes | $2.8 |
| Local supplier: $2.50, freight $500, no duty | 8.5 | Ok | Yes | $2.6 (+4.0%) |
| Empty SKU | — | — | — | SKU shows INVALID SKU |

## Design

- Every calculator **returns** a value instead of printing, so later versions can run them for many SKUs without changes
- Calculators feed each other: safety stock → reorder point → reorder flag
- Every function has a docstring (`help(safety_stock)` explains it)

## How to run

```bash
python3 toolkit.py
```

Edit the `sample_sku` dictionary to test other items.

## Changelog

| Version | Changes |
|---|---|
| v0.2 | First release: SKU cleanup, days of supply, safety stock, reorder point, reorder flag, stock status, landed cost |
