import json
import jsonpath


def test_Add_new_data():
    app_URL = 'http://127.0.0.1:8000/api/register/'
    f= open('file.json','r')
    request_json = json.loads(f.read())
    response=requests.post(app_URL,request_json)
    print(response.text)
            
test_Add_new_data()
