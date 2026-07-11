
import requests

"""Метод: POST"""
url = "http://127.0.0.1:8080/upload"
file_path = "C:\\Users\\pasha\\PycharmProjects\\ithillel_playwright\\lesson_18\\mars_photo1.jpg"    # шлях до файлу
with open(file_path, "rb") as image:    # відкриваємо файл у бінарному режимі для читання
    response = requests.post(url, files={"image": image})   # відправляємо POST

print(response.status_code)    # перевіряєм
print(response.json())

"""Метод: GET"""

url = 'http://127.0.0.1:8080/image/mars_photo1.jpg' # URL для отримання інформації про зображення
header = {"Content-Type": "text"}   # задаємо заголовок, щоб сервер повернув URL зображення у форматі JSON
response = requests.get(url, headers=header)    # GET

print(response.status_code)
print(response.json())

"""Метод: DELETE"""

url = 'http://127.0.0.1:8080/delete/mars_photo1.jpg'    # URL для видалення зображення з сервера
response = requests.delete(url) # відправляємо DELETE для видалення файлу

print(response.status_code)
print(response.json())