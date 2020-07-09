from flask import Flask, request, jsonify

app = Flask(__name__)

def win(slots):
    req = len(slots) - 1
    translated_list = list()
    options = ['coin', 'clover', '7', 'horseshoe']
    if slots.count('coin') >= req:
        value = 50 * slots.count('coin')
    elif slots.count('clover') >= req:
        value = 25 * slots.count('clover')
    elif slots.count('7') >= req:
        value = 10 * slots.count('7')
    elif slots.count('horseshoe') >= req:
        value = 5 * slots.count('horseshoe')
    else:
        value = 0 
    return value
    

@app.route('/get/total', methods=['POST'])
def calc():
    DATA=request.get_json()
    value = win(DATA['slot'])
    multiply=DATA['multiple']
    total = value * multiply
    return jsonify({'TOTAL':total})