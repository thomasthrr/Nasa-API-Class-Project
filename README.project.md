### This program is a web application built with Flask that interacts with NASA's Mars Rover Photos API to fetch and display images captured by the Curiosity, Opportunity, and Spirit rovers. We have learned a lot along the way, and would like to share how our code works in the following sections:

**Features**
The code allows users to view photos based on rover selection and specified dates in Martian sols or Earth dates while integrating with NASA's Mars Rover Photos API to fetch images. The purpose of the code is to provides a user-friendly interface for selecting rovers, date types, and viewing images.The backend has many features and is responsible for handling API requests, data retrieval, and response processing.

**Setup Instructions If You Would Like To Expand on The Project**
If you are planning to use the code or modify it in any way, please do the following:
1. Clone and fork the repository to your local machine
2. Install flask using pip install. On Mac, is is pip3 install Flask. For windows, it is ~m pip install flask.
3. Obtain a NASA API key from NASA's API portal. You can do so at this link: https://api.nasa.gov/
4. Insert your personal API key that you obtain from the website into the program
5. Run the Flask application using python app.py

**For Users**
1. Use the CD command to navigate the directory where your flask app.py file is located. For Mac, export FLASK_app=app.py. Export FLASK_env=Backend.py. For Windows, set FLASK_app=app.py. set FLASK_app=Backend.py
2. To run the app, execute flask run. This will open up your local web browser. You should see a similar link to: http://localhost:5000/
3. Select a rover (Curiosity, Opportunity, or Spirit) from the drop down menu
4. Choose to search for photos by either Martian sols or Earth dates and
5. Input the desired date
6. Click the submit button on the form to fetch and view images captured by the selected rover on the specified date

**Code Structure**
1. app.py: Contains the Flask backend code with routes for serving the HTML template and fetching images from NASA's API
2. index.html is the Frontend HTML template that provides the user interface to view live images from three different rovers
3. To access index.html you must followt the steps in Set-up and to easily go back to it, you can right click on the 'index.html' and click 'reveal in finder' to load your html page 