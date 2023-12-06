# iris_project1
** Deploying a Logistic Regression Model for Predictions using Flask **
Introduction:
In machine learning and data science, deploying models for real-time predictions is a crucial step towards making the technology accessible and user-friendly. We discuss the deployment process of a Logistic Regression model using Flask, a popular web framework in Python.
Objective:
The primary goal is to expose a predictive model through a web API, allowing users to make predictions based on input data sent to the server.
Technologies Used:
Flask: A lightweight and versatile web framework for Python.
joblib: A library for saving and loading machine learning models.
numpy: A fundamental package for scientific computing with Python.
Deployment Steps:
Model Training:
The first step involves training the Logistic Regression model using historical data. Once trained, the model is saved using the joblib library to ensure persistence.
Flask Application Setup:
A Flask web application is created to handle incoming requests and provide predictions. The application is initialized, and a route is defined to handle POST and GET requests at the "/get_predictions1" endpoint.
Request Handling:
The '/get_predictions1' endpoint is configured to accept both POST and GET requests. The input data is expected to be in JSON format, containing a key 'mydata' representing the data for which predictions are requested.
Running the Application:
The application is set to run when the script is executed directly. The debug mode is turned off for production use, and the application listens on port 5001.
Conclusion:
By following these steps, a Flask web application has been successfully created to deploy a Logistic Regression model. Users can send input data to the server, and the trained model will provide predictions in real-time.


