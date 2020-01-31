# Так как первое и второе задание схожи, я решила их объединить, мы создаем файл, если он не создан, вводим строки и записваем, потом считаем
try:
    file = open("2_text.txt", "w")
    strok = " "
    print("Введите текст: ")
    while True:
        strok = input()
        if strok == "/n" or strok == "":
            break
        else:
            file.writelines(strok + "\n")

except IOError:
    print("Произошла ошибка при работе с файлом")
finally:
    file.close()

try:
    file = open("2_text.txt", "r")
    i = 0
    slov = 0
    bukv = 0
    bukv2 = 0
    for strok in file:
        i += 1
        slov = slov + len(strok.split())
        bukv = bukv + len(strok)
        bukv2 = bukv2 + len(strok) - strok.count(" ") - 1
except IOError:
    print("Произошла ошибка при работе с файлом")
finally:
    print(
        f"В файле записано {i} строк, в которых {slov} слов, а это {bukv} всех символов, или {bukv2} символов не считая спецсимволов и пробелов")
    file.close()
