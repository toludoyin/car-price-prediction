

* [Car Price Predictor Website](https://car-prices-prediction-a.herokuapp.com/)

* To access the notebook in a presentation format and to interact with its graphs [check](https://nbviewer.org/github/toludoyin/car_price_prediction/blob/main/car_price_analysis_model.ipynb)

# **Car price prediction**
The car price prediction project predict car prices using the car features as input. The aim of the project is to help users either buyers and sellers predict the price of their preffered brand along with its qualities before placing an order.

## Outline of project
1. Data Collection

I collected my data from [kaggle](https://www.kaggle.com/datasets/CooperUnion/cardataset) that was scapped from twitter and Edmunds website.

2. Data Exploration and Cleaning

Wrangled my data into a better readable format for analysis, using the pandas library to drop irrelevant column, handling missing row and column, case formatting and removed outliers with IQR-interquartile range.

3. Data Analysis

Visualised the data with the interactive python library(plotly) along with saeaborn and matplot to see distributions and relationships.

4. Model Building and Prediction

Model the data with scikit-learn library, for preprocessing:
* Applied the test-train-split, splitted the data into independent(predictors) and dependent(response'(msrp)') test and train.
* One-hot encoding: to encode categorical features into machine format.
* Applied make-column-transformer: this applied seperate transformer on the numerical and categorical features.
* Model selection: examined 5 algorithm on the dataset to pick the best performing model on both trained and test set.
* Serialised the model with Pickle library into a byte file.

5. Deploy app to Heroku

## Others

Procfile file
* Indicate to heroku which file to start execution from, which is the app

Requirement.txt
* Stores all libraries and dependencies used in the project and makes it easier for third-parties to install libraries

venv: virtual environment for collecting libraries
* to create virtual enviroment (env) => ```python3 -m venv(env-name)```

* activate virtual enviroment => source (env-name)/bin/activate

* pip freeze > reqirement.txt

* when clone from git to local machine use pip install -r requirements.txt to install all packages

 Design and Template file
 * html and bootstrap template


