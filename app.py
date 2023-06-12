from flask import Flask, render_template, jsonify, request
import poe

app = Flask(__name__)
token = "RsnjIpIFVRX-2Q352LZGgQ%3D%3D"
client = poe.Client(token)

@app.route('/', methods = ["GET", "POST"])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
