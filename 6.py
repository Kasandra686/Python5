try:
    file = open("text_6.txt", "r" , encoding = 'utf-8')
    dikt=dict()
    for el in file:
        strok = el.replace("(л)","")
        strok = strok.replace("(пр)", "")
        strok =strok.replace("(лаб)", "")
        strok = strok.replace("-", "0")
        stroka = (strok.split())
        leson=str(stroka[0])
        leson=(leson[:len(leson)-1])
        hour = int(stroka[1]) + int(stroka[2])+int(stroka[3])
        dikt.update({leson: hour})
except IOError:
    print("Произошла ошибка при работе с файлом")
finally:
    print(dikt)
    file.close()
