# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:03:03 2020

@author: Krithika
"""
from flask import Flask,request
import pandas as pd
import numpy as np
import flassger 
from flasgger import Swagger

app = Flask(__name__) #from which point to start
Swagger(app)

import pickle
pickle_in =  open('clfpk.pkl','rb')
clf = pickle.load(pickle_in)
print(clf)
#decorator
@app.route('/') #root page
def welcome():
    return "Welcome ALL!!"

@app.route('/predict', methods=["Get"])
def predict_note_auth():
    """Lets authenticate Bank Note!
    ---
    parameters:
       - name: variance
         in: query
         type: number
         required: true
       - name: skewness
         in: query
         type: number
         required: true
       - name: curtosis
         in: query
         type: number
         required: true
       - name: entropy
         in: query
         type: number
         required: true
    responses: 
        200:
            description:
                The ouput values

    """
    variance= request.args.get('variance')
    skewness= request.args.get('skewness')
    curtosis= request.args.get('curtosis')
    entropy= request.args.get('entropy')
    prediction = clf.predict([[variance,skewness,curtosis,entropy]])
    try:
        return "The predicted value is" + str(prediction)
    except Exception as e:
        return str(e)
@app.route('/predict_file',methods=['POST'])
def predict_note_file():
    """Lets Authenticate Bank Note
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
    responses:
        200:
            description:
                The output values

    """
    df_test = pd.read_csv(request.files.get("file"))
    predicted = clf.predict(df_test)    
    try:
        return "The predicted value is" + str(list(predicted))
    except Exception as e:
        return str(e)



if __name__ == '__main__':
    app.run()
