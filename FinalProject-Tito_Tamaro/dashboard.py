from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import pickle
import base64
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/datviz')
def datviz():
    return render_template('datviz.html')


@app.route('/predict')
def predict():
    return render_template('prediksi.html')    

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        input_form = request.form
        RUUL = float(input_form['RevolvingUtilizationOfUnsecuredLines'])
        Age = float(input_form['age'])
        NT3059=float(input_form['NumberOfTime30-59DaysPastDueNotWorse'])
        DebtRatio=float(input_form['DebtRatio'])
        MI=float(input_form['MonthlyIncome'])
        NOCLL=float(input_form['NumberOfOpenCreditLinesAndLoans'])
        NT90=float(input_form['NumberOfTimes90DaysLate'])
        NRELL=float(input_form['NumberRealEstateLoansOrLines'])
        NT6089=float(input_form['NumberOfTime60-89DaysPastDueNotWorse'])
        ND= float(input_form['NumberOfDependents'])

        pred = Model.predict_proba([[RUUL,Age,NT3059,DebtRatio,MI,NOCLL,NT90,NRELL,NT6089,ND]])[0][1]
        
        if 0.744514 <= pred <= 1 :
            prediksi =  'Poor'
        elif 0.496343 <= pred <= 0.744513:
            prediksi =  'Fair'
        elif 0.248172 <= pred <= 0.496342:
            prediksi =  'Good'
        elif 0.000561 <= pred <= 0.248171:
            prediksi =  'Very Good'
        elif 0 <= pred <= 0.00056:
            prediksi =  'Exceptional'
        
        return render_template('result.html', data=input_form, prediksi=prediksi, pred=pred)

@app.route('/data')
def data():
    sqlengine = create_engine('mysql+mysqlconnector://root:cherryblossomtime@localhost/credit?host=localhost?port=3306')
    engine = sqlengine.raw_connection()
    cursor = engine.cursor()
    cursor.execute("SELECT * FROM credit")
    data2 = cursor.fetchall()
    return render_template('data.html', data=data2)


if __name__ == "__main__":
    with open('ModelFinal.sav', 'rb') as model:
        Model = pickle.load(model)
    app.run(debug=True)

