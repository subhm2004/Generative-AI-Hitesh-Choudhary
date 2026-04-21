def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100


orders = [100, 150, 200]
total_vat = 0
for price in orders:
    final_amount = add_vat(price, 10)
    total_vat += final_amount - price
    print(f"Original: {price}, Final with VAT: {final_amount}")

print(f"Total VAT: {total_vat}")