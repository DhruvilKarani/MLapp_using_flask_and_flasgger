# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 13:30:17 2019

@author: DHRUVIL
"""

import pickle
from flask import Flask, request
import numpy as np
import pandas as pd
from flasgger import Swagger

with open('C:/Users/DHRUVIL/Desktop/Deploying ML models/rf_model.pkl', 'rb') as model_file:
    model=pickle.load(model_file)

app= Flask(__name__)
Swagger(app)

@app.route('/predict')
def predict_iris():
    '''
    Example endpoint returning a prediction of Iris
    ---
    parameters:
        - name: S_length
          in: query
          type: number
          required: True
        - name: S_width
          in: query
          type: number
          required: True
        - name: P_length
          in: query
          type: number
          required: True
        - name: P_width
          in: query
          type: number
          required: True
    '''

    s_length=request.args.get('S_length')
    s_width=request.args.get('S_width')
    p_length=request.args.get('P_length')
    p_width=request.args.get('S_width')
    
    prediction = model.predict(np.array([[s_length,s_width,p_length,p_width]]))
    return str(prediction[0])


@app.route('/predict_file',methods=["POST"]) #Here we try to predict from an input file
def predict_iris_file():
    '''
    Example FILE endpoint for returning Iris predictions
    ---
    parameters:
        - name: input_file
          in: formData
          type: file
          required: True
    
    '''
    input_data=pd.read_csv(request.files.get("input_file"),header=None)
    prediction = model.predict(np.array(input_data))
    return str(list(prediction))

if __name__=='__main__':
    app.run()