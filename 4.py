try:
    file = open("text_4.txt", "r", encoding='utf-8')
    file2 = open("text_4_2.txt", "w", encoding='utf-8')
    translit = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
                "seven": "семь", "eight": "восемь", "nine": "девять"}
    for strok in file:
        arr = strok.split("-")
        file2.writelines(translit.get((arr[0])) + "-" + arr[1])
except IOError:
    print("Произошла ошибка при работе с файлом")
finally:
    print("Обработка данных выполнена успешно в файле text_4_2.txt")
    file.close()
    file2.close()
