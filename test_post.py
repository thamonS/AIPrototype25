import requests
import json

url = 'http://localhost:5001/request'
myobj = {
        'name' : 'Thamon',
        'age' : 23
        }

x = requests.post(url, data = json.dumps(myobj))
output = json.loads(x.text)
print(output['y'])