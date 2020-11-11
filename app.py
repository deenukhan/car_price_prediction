
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 01:27:23 2020

@author: deenuk
"""

# =============================================================================
# Sequence :  Fuel Type
#             Seller Type
#             Transmission
#             Present Price
#             KMS Driven
#             Owner
#             years Old''
# 
# ============================================================================
# =============================================================================
# Fuel Type-> Diesel=0, Petrol=1
# Seller Type-> Dealer=0, Individual=1
# Transmission-> Manual=1, Automatic= 0
# =============================================================================

import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np
import pickle

st.title("Car Price Prediction")
st.markdown('''Hi Folks, This App is fairly simple and the sole purpose of this Machine Learning Web App
            is to understand and grasp the fair idea about the complete life cycle of the project 
            from Scratch to deployment in the cloud. 
            This App is inspired by one of the videos of Krish Naik, you can find the video
            <a href="https://www.youtube.com/watch?v=p_tpQSY1aTs&t=3654s" target="_blank">here</a>. 
            Also, the Github link for this App is Available
            <a href="https://github.com/deenukhan/streamlit_car_dekho" target="_blank">here</a>.
            ''', unsafe_allow_html=True)

def gui():
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        fuel_type = st.selectbox("Fuel Type", ("Diesel", "Petrol", "CNG"))
    with col2: 
        seller_type = st.selectbox("Seller Type", ("Dealer", "Individual"))
    with col3:
        transmission = st.selectbox("Transmission", ("Manual", "Automatic"))
    
    col4, col5, col6 = st.beta_columns(3)
    with col4:
        current_price = st.number_input("Current Price in Lacs")
    with col5:
         kms_drive = st.text_input("KMS Driven")   
    with col6:
        owner_number = st.text_input("Number of Owners")
            
    purchase_year = st.text_input("Purchase Year")
    
    return fuel_type, seller_type, transmission, current_price, \
            kms_drive, owner_number, purchase_year


def predict(fuel_type, seller_type, transmission, current_price, \
                kms_drive, owner_number, purchase_year):
    
    model = pickle.load(open('model_rf_regressor.pkl', 'rb') )
    current_year = datetime.now().year
    
    fuel_type_diesel = None
    fuel_type_petrol = None
    
    if (fuel_type == 'Diesel'):
        fuel_type_diesel = 1
        fuel_type_petrol = 0
    elif (fuel_type=='Petrol'):
        fuel_type_diesel = 0
        fuel_type_petrol = 1
    else:
        fuel_type_diesel = 0
        fuel_type_petrol = 0
    
    if (seller_type == 'Dealer'):
        seller_type = 0
    else: 
        seller_type = 1
    
    if (transmission == 'Manual'):
        transmission = 1
    else:
        transmission = 0
        
    prediction = model.predict(np.array([fuel_type_diesel, fuel_type_petrol, 
                                          seller_type, transmission, current_price, 
                                          int(kms_drive), int(owner_number), 
                                          current_year - int(purchase_year)]).reshape(1, -1))

    return prediction

def main():
    fuel_type, seller_type, transmission, current_price, \
                kms_drive, owner_number, purchase_year = gui()
    predict_button = st.button("What is the Car Price ?")
    
    if(predict_button):
        prediction = predict(fuel_type, seller_type, transmission, current_price,
                             kms_drive, owner_number, purchase_year)
        "Predicted Price of Car is : ", float(prediction), " Lacs"
        
        
if __name__=="__main__":
    main()