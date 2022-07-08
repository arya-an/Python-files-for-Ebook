import requests

url = 'http://127.0.0.1:8000/api/user/20'
response = requests.get(url)
print(response.content)


