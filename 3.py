try:
    file = open("3_text.txt", "r", encoding='utf-8')
    i = 0
    money = 0
    for strok in file:
        i += 1
        arr = strok.split()
        if float(arr[1]) < 20000:
            print(arr[0])
        money = money + float(arr[1])

except IOError:
    print("Произошла ошибка при работе с файлом")
finally:
    print(f"средняя зарплата составляет : {(money / i)}")
    file.close()
