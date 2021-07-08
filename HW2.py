time = int(input("Введите время в секундах: "))
h = time // 3600
min = (time - h * 3600) // 60
sec = time - (h * 3600 + min * 60)
print(f"Время в формате чч:мм:сс    {h}:{min}:{sec}")

