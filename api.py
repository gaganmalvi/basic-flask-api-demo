import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

data = [
	{'codename' : 'onclite',
	 'retail' : 'Redmi 7' },
	{'codename' : 'lime',
	 'retail' : 'Redmi 9T' },
	{'codename' : 'phoenix',
	 'retail' : 'POCO X2' } 
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Basic Flask API Demo</h1><p>If you have successfully opened this page, your Flask application is running correctly!</p>"

@app.route('/devices', methods=['GET'])
def devices():
    return jsonify(data)

app.run()
