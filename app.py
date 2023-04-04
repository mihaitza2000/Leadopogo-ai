from flask import Flask
import requests
import json

app = Flask(__name__)

url = 'https://api.pawan.krd/v1/chat/completions'
API_KEY = "pk-nqnkfaVtEKcwMTIMxjSgpWfVnVGqKKEqlLQwhgGuJGhSJrke"
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

@app.route('/')
def hello_world():
    question = "how to increase my protein in my diate"
    payload = {
        "model": "gpt-3.5-turbo",
        "max_tokens": 100,
        "messages": [
            {
                "role": "assistant",
                "content": question
            },
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.text

if __name__ == '__main__':
    app.run()
