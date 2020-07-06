from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get/total', methods=['POST'])
def calc():
    DATA=request.get_json()
    value=DATA['slot']
    multiply=DATA['multiple']
    total = value * multiply
    return jsonify({'TOTAL':total})