import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    query = data['query']
    response = get_weather(query)
    return jsonify({'message': response})

def get_weather(city):
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    try:
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."
        else:
            return "Sorry, I couldn't retrieve the River information."
    except Exception as e:
        print("Error:", e)
        return "Sorry, I encountered an error while fetching the River information."

if __name__ == '__main__':
    app.run(debug=True)
