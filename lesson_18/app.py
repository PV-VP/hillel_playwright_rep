from flask import Flask, request, jsonify, send_from_directory
import os


app = Flask(__name__)


upload_directory = './uploads'  # Вказуємо папку, в якій будуть зберігатися завантажені файли.
if not os.path.exists(upload_directory):    # Перевіряємо, чи існує папка uploads.
    os.makedirs(upload_directory)       # Якщо папки немає — створюємо її.

#Завантаження зображення
@app.route('/upload', methods=['POST']) # декоратор Flask, який реєструє маршрут
def upload_image():
    if 'image' not in request.files:        # Перевіряємо, чи є у запиті файл з назвою image.
        return jsonify({'error': 'No image provided'}), 400         # Якщо файлу немає — повертаємо помилку 400 (Bad Request).

    image = request.files['image']      # Отримуємо об'єкт файлу із запиту.
    if image.filename == '':        # Перевіряємо, чи користувач вибрав файл.
        return jsonify({'error': 'No selected file'}), 400          # Якщо ім'я порожнє — повертаємо помилку.

    filename = os.path.join(upload_directory, image.filename)       # Формуємо повний шлях до файлу.
    image.save(filename)        # Зберігаємо файл на диск.

    return jsonify({'image_url': request.host_url + 'uploads/' + image.filename}), 201     # Код 201 означає, що ресурс успішно створено.

#Отримання
@app.route('/image/<filename>', methods=['GET'])    # декоратор Flask, який реєструє маршрут.
def get_image(filename):    #Параметр filename Flask бере із URL.
    content_type = request.headers.get('Content-Type')  #Беремо значення HTTP-заголовка Content-Type.
    filepath = os.path.join(upload_directory, filename) #Створюємо повний шлях до файлу.
    if os.path.exists(filepath):    #Перевіряємо, чи існує файл
        if content_type == 'text':  #Якщо файл є текстом
            return jsonify({'image_url': request.host_url + 'uploads/' + filename}), 200    #Повертаємо JSON
        elif content_type == 'image':  # Якщо клієнт хоче отримати саме файл.
            return send_from_directory(upload_directory, filename)  #Flask відкриває файл із папки uploads і відправляє його клієнту.
        else:
            return jsonify({'error': 'Unsupported Content-Type'}), 400  # якщо не текст і не картинка то 400
    else:
        return jsonify({'error': 'Image not found'}), 404   #якщо файлк не існує - 404

#видалення
@app.route('/delete/<filename>', methods=['DELETE'])    # декоратор Flask, який реєструє маршрут.
def delete_image(filename):
    filepath = os.path.join(upload_directory, filename)
    if not os.path.exists(filepath):
        return jsonify({'error': 'Image not found'}), 404

    os.remove(filepath)
    return jsonify({'message': f'Image {filename} deleted'}), 200


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host=host, port=port, debug=True)

