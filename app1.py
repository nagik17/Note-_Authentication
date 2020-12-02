# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:03:03 2020

@author: Krithika
"""
from flask import Flask,request
import pandas as pd
import numpy as np
#import flassger 
#from flasgger import Swagger

#app = Flask(__name__) #from which point to start
#Swagger(app)
import streamlit as st
from PIL import Image
import pickle
pickle_in =  open('clfpk.pkl','rb')
clf = pickle.load(pickle_in)
#print(clf)
#decorator
#@app.route('/') #root page
def welcome():
    return "Welcome ALL!!"

#@app.route('/predict', methods=["Get"])
def predict_note_auth(variance,skewness,curtosis,entropy):
    
    prediction = clf.predict([[variance,skewness,curtosis,entropy]])
    try:
        return "The predicted value is" + str(prediction)
    except Exception as e:
        return str(e)
#@app.route('/predict_file',methods=['POST'])
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

def main():
    st.title("BankNote Authentication")
    html_temp="""
    <div style = "background-color:tomato;padding:10px">
    <h2 style ="color:white;text-align:center;">Streamlit Bank Note Authenticator ML App </h2>
    <div/>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("Skewness","Type Here")
    curtosis = st.text_input("Curtosis","Type Here")
    entropy = st.text_input("Entropy","Type Here")
    result=''
    if st.button('Predict'):
        result = predict_note_auth(variance,skewness,curtosis,entropy)
    st.success("The output is {}".format(result))
    if st.button("About:"):
        st.text('Lets Learn')
        st.text('Build with Streamlit')
    

if __name__ == '__main__':
    main()
