from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

NASA_API_KEY = 'DEMO_KEY'  # Replace with your NASA API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_images', methods=['POST'])
def fetch_images():
    rover = request.form.get('rover')
    date_type = request.form.get('date_type')
    date = request.form.get('date')
    page = request.form.get('page', 1)

    if date_type == 'sol':
        params = {'sol': date, 'page': page, 'api_key': NASA_API_KEY}
    else:  # earth_date
        params = {'earth_date': date, 'page': page, 'api_key': NASA_API_KEY}

    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos'
    response = requests.get(url, params=params)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)