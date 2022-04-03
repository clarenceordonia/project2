from flask import Flask, render_template, request, flash

app = Flask(_name_)

@app.route("/hello")
def index():
	return render_template("index.html")
