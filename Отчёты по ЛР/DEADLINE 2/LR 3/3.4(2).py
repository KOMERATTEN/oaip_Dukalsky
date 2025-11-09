products = {
    "Ноутбук": {"price": 50000, "sold": 15},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 8}
}

max_sold = 0
best_selling = ""
total_revenue = 0
max_revenue = 0
best_revenue_product = ""

for product, info in products.items():
    if info["sold"] > max_sold:
        max_sold = info["sold"]
        best_selling = product
    
    revenue = info["price"] * info["sold"]
    total_revenue += revenue
    
    if revenue > max_revenue:
        max_revenue = revenue
        best_revenue_product = product

print(f"Самый продаваемый товар: {best_selling}")
print(f"Общая выручка: {total_revenue}")
print(f"Товар с наибольшей выручкой: {best_revenue_product}")