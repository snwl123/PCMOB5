# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_index():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/bmi')
def bmi_page():
    return render_template('bmi.html')

@app.route('/calcbmi')
def bmi_calc():
    weight = request.args["weight"]
    height = request.args["height"]
    name = request.args["name"]
    bmi = float(weight) / (float(height) * float(height))
    rounded_bmi = round(bmi,1)
    result = "Hi, " + name + ".Your weight is " + weight + "kg.Your height is " + height + "m.Your BMI is " + str(rounded_bmi) + "."
    return result

@app.errorhandler(404)
def page_not_found(e):
     return ('Page Not Found!'), 404

