Delivery_Range = int(input("Введите расстояние доставки (в км) "))
Package_Weight = int(input("Введите вес посылки (в кг) "))
Delivery_Cost = 0
if Delivery_Range >= 500:
    Delivery_Cost = Delivery_Range / 100 * 500
else:
    Delivery_Cost = Delivery_Range / 100 * 300
if Package_Weight >= 10:
    Delivery_Cost *= .10
print(round(Delivery_Cost))
