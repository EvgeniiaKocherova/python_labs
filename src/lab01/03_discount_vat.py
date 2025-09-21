price = float(input("Цена(Р): "))
discount = float(input("Скидка(%): "))
vat = float(input("НДС(%): "))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f'{"База после скидки:":20} {base:.2f} Р')
print(f'{"НДС:":20} {vat_amount:.2f} Р')
print(f'{"Итого к оплате:":20} {total:.2f} Р')
