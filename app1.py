import streamlit as st
import pickle
import numpy as np
data= pickle.load(open('data.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))
st.title("Electricity Price Predictor")
Day= st.number_input('Day(Day of Date)',min_value=1,max_value=31)
Month=st.number_input('Month(Month of Date)',min_value=1,max_value=12)
ForecastWindProduction=st.number_input("ForecastWindProdection(range from 0.0 to 1600.0)",min_value=0.0,max_value=1600.0)
SystemLoadEA=st.number_input('SystemLoadEA(range from 2100.0 to 6500.0)',min_value=2100.0,max_value=6500.0)
SMPEA=st.number_input('SMPEA(range from 10.0 to 110.0)',min_value=10.0,max_value=110.0)
ORKTemperature=st.number_input('ORKTemperature(range from -2.0 to 50.0)',min_value=-2.0,max_value=50.0)
ORKWindspeed=st.number_input('ORKWindspeed(range from 0.0 to 40.0)',min_value=0.0,max_value=40.0)
CO2Intensity=st.number_input('CO2Intensity(range from 250.0 to 750.0)',min_value=250.0,max_value=750.0)
ActualWindProduction=st.number_input('ActualWindProduction(range from 1.0 to 1600.0)',min_value=1.0,max_value=1600.0)
SystemLoadEP2=st.number_input('SystemLoadEP2(range from 1000.0 to 6500.0)',min_value=1000.0,max_value=6500.0)
if st.button('Predict Price'):
        features = np.array([[Day,Month,ForecastWindProduction,SystemLoadEA,SMPEA,ORKTemperature,ORKWindspeed,CO2Intensity,ActualWindProduction,SystemLoadEP2]])
        # predicted_time=lm.predict(features)
        SMPEP2=float(model.predict(features))
        # st.title("The predicted time of Delivery " + str(int(lm.predict(features)))+"minutes")
        st.title(f"The predicted price of electricity {SMPEP2:.2f}")
        # st.write(f"Predicted Delivery time in {predicted_time[0]:.2f} Minutes")
