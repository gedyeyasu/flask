from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello flask"

@app.route("/gedy")
def gedy():
	return "Hello admin"