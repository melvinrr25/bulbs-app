import os
from wyze_sdk import Client
from flask import Flask, render_template, request

app = Flask(__name__)

app.config['UPLOAD_PATH'] = '/tmp'
client = Client(email=os.getenv("EMAIL"), password=os.getenv("PASSWORD"))

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/settings', methods = ['POST'])
def test():
    data = request.get_json()
    color = data['color']
    brightness = data['brightness']
    info = client.bulbs.info(device_mac="7C78B271E6D9")
    model = info.product.model
    #client.bulbs.turn_off(device_mac="7C78B278639E", device_model=model)
    client.bulbs.set_color(device_mac="7C78B271E6D9", device_model=model, color=color)
    client.bulbs.set_brightness(device_mac="7C78B271E6D9", device_model=model, brightness=int(brightness))
    return { 'result': 'ok' }

with_debug = True if os.getenv('FLASK_DEBUG') else False
app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=with_debug)
