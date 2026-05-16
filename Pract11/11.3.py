import csv

sum = 0

with open('prod.csv', 'r', encoding='utf-8') as f:
    print("Нужно купить:")
    for row in csv.DictReader(f):
        pro = row["Продукт"]
        kol = int(row["Количество"])
        cen = int(row["Цена"])
        print(f"{pro} - {kol} шт. за {cen} руб.")
        sum += kol * cen
print("")
print("Итоговая сумма: ",sum," руб.")