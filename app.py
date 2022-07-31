
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__, template_folder='template')
model = pickle.load(open('random_forest_model.pickle', 'rb'))
features = ['make', 'year', 'engine_fuel_type', 'engine_hp',	'transmission_type', 'driven_wheels',  'number_of_doors', 'vehicle_size',	'vehicle_style']

@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])

def predict():
    """rendering result to html gui"""

    year = int(request.form["year"])  # take year input from user
    make = request.form["make"]
    number_of_doors = int(request.form[" number_of_doors"])
    vehicle_style = request.form["vehicle_style"]
    vehicle_size = request.form[" vehicle_size"]
    driven_wheels = request.form["driven_wheels"]
    engine_fuel_type = request.form["engine_fuel_type"]
    engine_hp = int(request.form["engine_hp"])
    transmission_type = request.form["transmission_type"]

    prediction = model.predict([[make, year, engine_fuel_type, engine_hp,	transmission_type, driven_wheels, number_of_doors, vehicle_size,	vehicle_style]])

    output=round(prediction[0],2)

    if output<0:
        return render_template('index.html',prediction_texts="Sorry I do not know this car brand")
    else:
        return render_template('index.html',prediction_text=(f"You can buy the car at {output}."))
# else:
#     return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)