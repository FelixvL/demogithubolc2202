from flask import Flask
import pandas 
from bestand1 import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/twee/<getal>")
def hello_world2(getal):
    var1 = int(getal)
    var2 = var1 * var1
    return "<p>Dit is een hele "+str(var2)+" andere functie</p>"

@app.route("/vierde")
def hello_world3():
    return heleanderemethode()

@app.route("/vijfde")
def hello_world4():
    return heleanderemethode()