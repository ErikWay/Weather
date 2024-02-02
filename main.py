from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Замените YOUR_API_KEY на свой ключ от OpenWeatherMap
API_KEY = '20cc64eb05b219466d0782b3e9146534'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    country = request.form['country']
    city = request.form['city']

    # Формируем URL запроса к OpenWeatherMap API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={API_KEY}'

    # Отправляем запрос и получаем ответ
    response = requests.get(url)
    data = response.json()

    # Извлекаем нужные данные о погоде
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']

    # Отправляем данные в формате JSON обратно клиенту
    return jsonify({'description': weather_description, 'temperature': temperature})

if __name__ == '__main__':
    app.run(debug=True)


