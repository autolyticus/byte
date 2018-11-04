import requests
url = 'https://api.jsonbin.io/b'
headers = {'Content-Type': 'application/json'}
data = {"Sample": "Hello World"}

req = requests.post(url, json=data, headers=headers)
# print(req.text)

# print(req.json())
id = req.json()['id']

req = requests.get(url+'/'+id)
print(req.text)
