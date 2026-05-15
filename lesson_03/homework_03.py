alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"'
                       '\n"That depends a good deal on where you want to get to," said the Cat."'
                       '\n"I don\'t much care where ——" said Alice.'
                       '\n"Then it doesn\'t matter which way you go," said the Cat.'
                       '\n"—— so long as I get somewhere," Alice added as an explanation.'
                       '\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
print(f'Total area: {black_sea_area + azov_sea_area} km2')
# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total = 375291
warehouse_1_2 = 250449
warehouse_2_3 = 222950
warehouse_3 = total - warehouse_1_2
warehouse_1 = total - warehouse_2_3
warehouse_2 = total - (warehouse_3 + warehouse_1)
print('Склад 1:', warehouse_1, '\nСклад 2:', warehouse_2, '\nСклад 3:', warehouse_3)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
price = 1179
payment_term = 18
for i in range(1, payment_term + 1):
    total = price * i
print(f'Варість комп\'ютера: {total}грн')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
d = {
    8019 : 8,
    9907 : 9,
    2789 : 5,
    7248 : 6,
    7128 : 5,
    19224 : 9
}

for key, value in d.items():
    print(f'Остача від ділення {key} % {value} = {key % value}')


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
total = 0

prices = [
    ('Піца велика', 4, 274),
    ('Піца середня', 2, 218),
    ('Сік', 4, 35),
    ('Торт', 1, 350),
    ('Вода', 2, 21)
]
for food, qnt, price in prices:
    total += qnt * price

print(f'Всього грошей потрібно: {total} грн')

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
foto = 232
foto_per_page = 8
total_pages = 0

if foto % foto_per_page ==0:
    total_pages = foto / foto_per_page
print(f'Ігорю знадобиться {int(total_pages)} сторінок')
      
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
kharkov_budapesht_km = 1600
tank = 48
litres_per_100 = 9
gas_total = (kharkov_budapesht_km / 100) * litres_per_100
numbers_of_full_tanks = gas_total / tank # якщо подорож починається з пустим баком
full_tank_start = int(numbers_of_full_tanks) - 1
print(f'Літрів бензину знадобиться для подорожі: {int(gas_total)}',
      f'\nКількість заїздів на заправку: {int(numbers_of_full_tanks)}')   # якщо подорож починається з повним баком numbers_of_full_tanks = full_tank_start