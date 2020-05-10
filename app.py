from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	headline="method to import"
	return render_template("index.html", headline=headline)

@app.route("/gedy")
def gedy():
	return "Hello admin"

@app.route("/<string:name>")
def hello(name):
	name=name.capitalize()
	return f"Welcome, {name}!"

