# class-project
# Team members - Thomas Thiry, Shivant Malkani, OIM3640-02

**The Big Idea**

Main Idea: The project aims to create a web application that displays photos taken by NASA's Mars rovers. Users will be able to view the latest images sent from Mars, offering an insight into the Martian landscape and NASA's exploration efforts. Currently, space enthusiasts do not have an easy way to look for live images of the Mars Rover displayed in a variety of angles and geographical locations. Downloadable from their smartphone. So, this MVP aims to be a good to have widget space enthusiasts can rely on to get Mars rover images. 

MVP: A simple, user-friendly interface that displays live photos from the Mars rovers. The application will fetch these images directly from NASA's API. We plan to ensure that users can look at images on a 24-hour basis 

Stretch Goal: We would add features like filtering images by Martian sol (day) or by the specific rover camera. Given our understanding of python, this might be challenging, but e would want to try implementing these additional features 

**Learning Objectives**

**Shared Goals**: Learn the basics of using and leveraging APIs for a real-world utility. We will cover web development (HTML, CSS, JavaScript), and understand the process of deploying a web application for users. 

**Individual Goals:** Thomas will focus on specific areas like frontend design and helping Shivant with the Nasa API integration and backend.  

**Implementation Plan**

Initial Tools and Frameworks: 

Frontend: HTML, CSS, and JavaScript.  

API: NASA's Mars Rover Photos API. 

Deployment: GitHub Pages or a similar platform for hosting  

Investigation Plan: Research how to effectively use NASA’s APIs using python and how to deploy a static website using GitHub Pages. 

**Project Schedule** 

Week 1: Research and familiarize with NASA's API. We will start designing the UI and strategize on how to display our images 

Week 2-3: We will then go on to develop the core functionality (fetching and displaying photos). At this point in time, we will also begin frontend development. 

Week 4: By the last week (prior to December 4th), we will finalize the frontend, conduct basic testing, and deploy the application. We will also continue to debug, and if time permits, will add additional features. 

**Collaboration Plan** 

Task Division: We plan to divide tasks based on individual strengths and learning goals. For example, focusing on the API integration while the other works on the frontend design. 

Pair Programming: Regular pair programming sessions to integrate the frontend and backend. This will be conducted in-person and through online tools such as Zoom/Teams.  

Communication: Regular in person and virtual meetings and use of collaboration tools like Notion for task / roadmap tracking. 

**Risks and Limitations** 

Major Risks: Potential challenges include difficulties in understanding and integrating the NASA API, unforeseen technical issues, and time constraints. Integrating the API and debugging will probably require extra efforts and might slow us down. This is potentially the only the thing that will slow us down and prevent us from turning in a complete project 

Mitigation Strategy: We are going to allocate extra time for learning and troubleshooting. During the thanksgiving break, we plan on meeting twice an working on the project individually too. At this point in time, based on the work we have done, we might simplify the project scope if deemed necessary. 

**Additional Course Content** 

Beneficial Topics: There are many beneficial topics we can understand through this project. We plan on using additional tutorials on JavaScript, especially related to API consumption, and resources on basic web development and deployment strategies would be beneficial to the overall scope. We expect to learn a myriad of new topics/tools on the way which will help us out with our overall python understanding 

 
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
 
