a = input("Точки на теста: ")
a = int(a)

if a <= 0:
    print("Слаб 2")
elif a >= 51 and a <= 60:
    print("Среден 3")
elif a >= 61 and a <= 70:
    print("Дабър 4")
elif a >= 71 and a <= 80:
    print("Много Добър 5")
elif а >= 81 and a <= 99:
    print("Отличен 6")
else:
    print("Много Отличен 7")
