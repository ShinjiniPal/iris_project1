# Import the requests library for making HTTP requests
import requests

# Make a POST request to the Flask server's '/get_predictions1' endpoint
# The endpoint URL is 'http://127.0.0.1:5001/get_predictions1'
# The request payload is JSON data with a key 'mydata' containing a list of lists
r=requests.post(' http://127.0.0.1:5001/get_predictions1',json={"mydata":[[5.1], [3.5], [1.4], [0.2]]})


# Print the text content of the response received from the server
r.text
