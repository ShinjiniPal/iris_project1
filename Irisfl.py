# Import necessary modules from Flask and joblib
from flask import Flask, request, Response
from joblib import load
import numpy as np

# Load the pre-trained Logistic Regression model
my_lr_model=load('Model/LogReg_model.joblib')
from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route for receiving predictions
@app.route( "/get_predictions1",methods=['POST','GET'])
def testing():
    data=request.json               # Extract data from the incoming JSON request
    user_sent_this_data=data.get('mydata')

    user_number=np.array(user_sent_this_data).reshape(1,-1)                # Convert the user's data to a numpy array and reshape it
    model_predictions=my_lr_model.predict(user_number)                     # Make predictions using the pre-trained model
    return Response(str(model_predictions))                                 # Return the model predictions as a response

# Run the Flask application if this script is executed directly
if __name__=='__main__':
    app.run(debug=False, port=5001)       # Start the application on port 5001 with debugging turned off





