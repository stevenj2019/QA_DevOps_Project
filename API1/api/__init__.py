from flask import Flask, jsonify
import random

app = Flask(__name__)

#Helper function 
def slot():
    return random.choice(['coin', 'clover', '7', 'horseshoe'])

@app.route('/get/slot', methods=['GET'])
def machine():
    output = list()
    for i in range(1, 4):
        icon = slot()
        output.append(icon)
    return jsonify({'machine':output})