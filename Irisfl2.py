import requests
r=requests.post(' http://127.0.0.1:5001/get_predictions1',json={"mydata":[[5.1], [3.5], [1.4], [0.2]]})
r.text
