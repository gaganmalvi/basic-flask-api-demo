import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Basic Flask API Demo</h1><p>If you have successfully opened this page, your Flask application is running correctly!</p>"

app.run()
