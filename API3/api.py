from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get/total', methods=['POST'])
def calc():
    if request.method == 'POST':
        DATA=request.json
        value=DATA['slot'] #returning as None for some reason 
        multiply=DATA['multiple'] # that error assumably breaks the full function
        total = value * multiply
        return jsonify({'TOTAL':total})

app.run(port=5000, debug=True)