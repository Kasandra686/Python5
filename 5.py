print("Вводите числа через пробел. Пустая строка - окончание ввода")
i = 0
i2 = 0
try:
    file = open("text_5.txt", "w", encoding='utf-8')
    strok = " "
    while True:
        strok = input()
        if strok == "/n" or strok == "":
            break
        else:
            for el in strok.split():
                if el.isdigit():
                    file.writelines(el + " ")
                    i = i + int(el)
                    i2 += 1


except IOError:
    print("Произошла ошибка при работе с файлом")
finally:
    print(f"Все {i2} числа записанны в файл text_5.txt, их сумма состовляет: {i} ")
    file.close()
