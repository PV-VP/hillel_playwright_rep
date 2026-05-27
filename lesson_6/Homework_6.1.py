#Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()


len_set = len({i for i in input()})
if len_set > 10:
    print('True')
else:
    print('False')


