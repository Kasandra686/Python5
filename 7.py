import json
try:
    file = open("text_7.txt", "r" , encoding = 'utf-8')
    dikt=dict()
    i=0
    prize=0
    for el in file:
        stroka = (el.split())
        ptib= int(stroka[2]) - int(stroka[3])
        if ptib>=0:
            i+=1
            prize=prize+ptib
        dikt.update({stroka[0]: ptib})
except IOError:
    print("Произошла ошибка при работе с файлом")
finally:
    print("К сожалению, из-за нехватки времени, я не успела доделать задание, как требовалось в json виде")
    print(dikt)
    print(f"Средняя прибль неубыточных организаций составляет: {(prize/i)}")
    file.close()
