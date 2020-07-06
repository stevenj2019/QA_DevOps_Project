from flask import Flask, jsonify
import random

app = Flask(__name__)

#Helper function 
def slot():
    num = random.randint(1, 4)
    if num == 1:
        return 'coin'
    elif num == 2:
        return 'clover'
    elif num == 3: 
        return '7'
    elif num == 4: 
        return 'horseshoe'

@app.route('/get/slot', methods=['GET'])
def machine():
    output = list()
    for i in range(1, 4):
        icon = slot()
        output.append(icon)
    return jsonify({'machine':output})