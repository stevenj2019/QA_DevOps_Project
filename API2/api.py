from flask import Flask, jsonify
import random 

app = Flask(__name__)

@app.route('/get/multi', methods=['GET'])
def multi():
	num = random.randint(1, 5)
	return jsonify({'multiply':num})

app.run(port=5000, debug=True)