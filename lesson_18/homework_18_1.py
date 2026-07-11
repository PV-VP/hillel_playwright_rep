"""Виконати пошук зображень, пов’язаних з ровером Curiosity на Марсі.
З JSON відповіді витягнути nasa_id для знайдених елементів.
Для кожного nasa_id зробити додатковий запит до endpoint-а /asset/{nasa_id}, щоб отримати список URL-ів файлів.
Обрати з цього списку посилання на JPG-зображення (наприклад, перший .jpg або “найкращий” варіант, якщо їх кілька).
Скачати 2 зображення і зберегти локально як:
mars_photo1.jpg
mars_photo2.jpg"""

import requests

BASE_URL = "https://images-api.nasa.gov"

search_url = f"{BASE_URL}/search"   # адреса для пошуку медіа

search_params = {
  "q": "Curiosity rover Mars",  # пошуковий запит
  "media_type": "image",        # тільки зображення
  "page_size": 20               # щоб було з чого вибрати
}

response = requests.get(search_url, params=search_params)   # робимо запит пошуку
if response.status_code == 200:     # перевірка статусу
    data = response.json()      # перетворюємо відповідь у словник
    items = data['collection']['items']             # дістаємось до списку знайдених елементів

    downloaded = 0      # зупиняєм цикл

    for item in items:
        nasa_id = item['data'][0]['nasa_id']        # дістаємо id елемента
        asset_url = f"{BASE_URL}/asset/{nasa_id}"   # будуємо адресу для запиту файлів цього id
        res = requests.get(asset_url)               # робимо запит на список файлів

        if res.status_code == 200:
            data_res = res.json()       # перетворюємо відповідь у словник

            d = data_res['collection']['items']         # список файлів для цього id
            jpg_links = []
            for i in d:

                splt_link_orig = i['href'].split('~')       # розбиваємо посилання по символу ~ для перевірки на orig.jpg
                if splt_link_orig[-1] == 'orig.jpg':
                    jpg_links.append(i)

            for link in jpg_links:
                r = requests.get(link['href'])      # скачуємо файл картинки
                rs = r.content                      # дістаємо бінарний вміст картинки
                if r.status_code == 200:
                    downloaded += 1
                    with open(f"mars_photo{downloaded}.jpg", "wb") as f:    # відкриваємо новий файл на запис
                        f.write(rs)                                         # записуємо вміст картинки у файл

                    if downloaded == 2:
                        break

        if downloaded == 2:
            break

