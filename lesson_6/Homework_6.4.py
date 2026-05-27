#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
#v1.0
lst = [1, 21, 34, 22, 56, 87, 6, 23, 4]
count = 0

for el in lst:
    if el % 2 == 0:
        count += el
print(count)


#v2.0
res = sum([element for element in lst if element % 2 == 0])
print(res)