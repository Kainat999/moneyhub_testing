import requests
import json

url = 'http://127.0.0.1:8000/webhook/'

data = {
    'event': 'TRANSACTION_CREATED',
    'client_id': '123',
    'amount': 30,
    'description': 'Test id client  Transaction',
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200 and response.text:
    try:
        json_content = response.json()
        print('Response JSON:', json_content)
    except json.JSONDecodeError:
        print('Error decoding JSON: Response content is not valid JSON.')
else:
    print('Error:', response.status_code, response.text)
