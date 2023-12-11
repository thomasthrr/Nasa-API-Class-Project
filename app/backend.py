# The first step would be to import modules from Flask and other requests libraries
from flask import Flask, render_template, request, jsonify
import requests

# We then need to initialize the flask application
app = Flask(__name__)

# NASA API KEY
NASA_API_KEY = 'ptgexIhRTW9zZOUA6I56q1g7tpOMDZHoZp92tdAB'

# At this point, we are defining the route for the root URL. "Def Index" will render the index.html file and return the HTML file as the homepage
@app.route('/')
def index():
    return render_template('index.html')

# In this next function, images from the NASA API will be fetched based on user input, and will return the images as a JSON Response
@app.route('/fetch_images', methods=['POST'])
def fetch_images():
    try:
        # Over here, the variables retrieve the form data sent from the frontend
        rover = request.form.get('rover')
        date_type = request.form.get('date_type')
        date = request.form.get('date')
        page = request.form.get('page', 1)

        # API request parameters based on selected date type (sol or earth_date)
        if date_type == 'sol':
            params = {'sol': date, 'page': page, 'api_key': NASA_API_KEY}
        else:  # earth_date
            params = {'earth_date': date, 'page': page, 'api_key': NASA_API_KEY}

        # Over here, we construct the API request URL based on user input
        url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos'

        # At this juncture, a request is sent to NASA's API to fetch data
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for HTTP status codes >= 400

        # This next snippet checks if the API request was succesful. Then, the program returns the fetched images data as a JSON response
        return jsonify(response.json())
    except requests.RequestsException as e:
        # Handle any requests-related exceptions and return an error response
        return jsonify({'error': str(e)}), 500

# Run the flask app if the code is successfully executed
if __name__ == '__main__':
    app.run(debug=True)