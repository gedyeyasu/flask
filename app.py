import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/isitnewyear")
def index():
	now=datetime.datetime.now()
	newyear= now.month==1 and now.day==1
	
	return render_template("index.html", headline=newyear, date=now)

@app.route("/list")
def list():
	names=["Gedeon", "Adnrew", "Musk"]
	return render_template("index.html", name=names)

@app.route("/submit", methods=["POST"])
def submit():
	name=request.form.get("name")
	message=request.form.get("message")

	return render_template("hello.html", name=name, message=message)
@app.route("/more")
def more():
	return render_template("more.html")

@app.route("/gedy")
def gedy():
	return "Hello admin"

@app.route("/<string:name>")
def hello(name):
	name=name.capitalize()
	return f"Welcome, {name}!"

@app.route("/bye")
def bye():
	headline="Good bye!"
	return render_template("index.html", headline=headline)
