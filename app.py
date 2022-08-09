
from flask import Flask, render_template, request
import jsonify
 flask_cors import CORS, cross_origin
import pickle
import numpy as np
import sklearn
import numpy as np
import pandas as pd

app = Flask(__name__, template_folder='template')
cors=CORS(app)
car_data = pd.read_csv('dataset/cleaned_car_data.csv')
model = pickle.load(open('random_forest_model.pickle', 'rb'))

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def home():
    year = sorted(car_data['year'].unique(), reverse=True)
    make = sorted(car_data['make'].unique())
    number_of_doors = sorted(car_data['number_of_doors'].unique())
    vehicle_style = sorted(car_data['vehicle_style'].unique())
    vehicle_size = sorted(car_data['vehicle_size'].unique())
    driven_wheels = sorted(car_data['driven_wheels'].unique())
    engine_fuel_type = sorted(car_data['engine_fuel_type'].unique())
    transmission_type = sorted(car_data['transmission_type'].unique())

    make.insert(0, 'Select brand')
    return render_template('index.html', year=year, make=make, number_of_doors=number_of_doors, vehicle_style=vehicle_style, vehicle_size=vehicle_size, driven_wheels=driven_wheels, engine_fuel_type=engine_fuel_type, transmission_type= transmission_type)

@app.route("/predict", methods=['POST'])

def predict():
    """rendering result to html gui"""

    year = int(request.form.get('year'))
    make = request.form.get('make')
    number_of_doors = int(request.form.get('number_of_doors'))
    vehicle_style = request.form.get('vehicle_style')
    vehicle_size = request.form.get('vehicle_size')
    driven_wheels = request.form.get('driven_wheels')
    engine_fuel_type = request.form.get('engine_fuel_type')
    engine_hp = int(request.form.get('engine_hp'))
    transmission_type = request.form.get('transmission_type')

    prediction = model.predict(pd.DataFrame(columns=['make', 'year', 'engine_fuel_type', 'engine_hp', 'transmission_type', 'driven_wheels', 'number_of_doors', 'vehicle_size', 'vehicle_style'], data=np.array([make, year, engine_fuel_type, engine_hp, transmission_type, driven_wheels, number_of_doors, vehicle_size, vehicle_style]).reshape(1,9)))

    return str(np.round(prediction[0],2))


if __name__ == "__main__":
    app.run(debug=True)