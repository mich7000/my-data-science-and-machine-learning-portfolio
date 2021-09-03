# necessary python libraries..
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from joblib import load

import locale
l = locale.setlocale(locale.LC_ALL, 'en_US')

# loading saved models
FILE_1 = 'output/model3.pkl'
model_= load(FILE_1)

st.set_page_config(page_title='house price predictor app.')
# interfaces
st.header("Project 2 - Predict the average house price of a given area in Taiwan, New Taipei city.")
st.image('images/front.jpg') 
st.subheader("""Sindian District, **New Taipei City**, Taiwan.""")

st.header("**Brief Analysis**") 
my_expander = st.beta_expander(label="Click to Exapnd")
with my_expander:
           st.markdown("""
           The chart above shows house prices across **Taipei city**.
           * As you can see, most of the high and mid-range priced houses are mostly located in **Shierzhang** district
           * Most of the cheap and moderately cheap houses are found in the **Akeng** and **Lingding** district.
           
           The chart clearly dipicts how houses are priced as relative to the allocation of **infrastructure** and **resources**. 
           You can see that most of the highly-prices homes are clustered around the location with much **resource**, and the smaller circles (low-priced) houses
           clustered around place with less **resource** and infrastructure.
              """)
           st.image('images/house-prices-across the district.png')
           

        
        
        
st.header("""Predict the **House Price** of a given area.""")
st.write('*Please fill every entry provided (and also with the right data type) to avoid any errors.*')
def predictor(house_age, 
              dist_nearest,
              number_of_stores,
              lat,
              long,
              transac_yr,
              transac_mth,
              transac_dayname,):
    
    new_instance = [house_age, 
              dist_nearest,
              number_of_stores, 
              lat,
              long,
              transac_yr,
              transac_mth,
              transac_dayname,]
    new = pd.DataFrame(new_instance, index=['house age',
                                            'dist to nearest MRT',
                                            'number of convenience stores',
                                            'latitude',
                                            'longitude',
                                            'transaction_year',
                                            'transaction_month',
                                            'transaction_dayname',]).T
    prediction= model_.predict(new)[0] * 10000
    return prediction


# main program where ML computations occurs..
def main():
    
    frame1, frame2= st.beta_columns([4, 3])

    with frame1:
        house_age= st.text_input('House Age', 0.0)
        number_of_stores = st.selectbox('Number of convenient stores (select 10 if higher)', np.arange(1, 11))
        dist_nearest= st.text_input('Distance to the nearest MRT station', )
        long= st.slider(label='Longitude', min_value=121.4, max_value=121.6,)
        lat = st.slider(label= 'Latitude', min_value=24.92, max_value=25.02)

    with frame2:
        transac_dayname= st.selectbox("(Week Day) of Transaction: ", ['Sunday' , 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday'])
        transac_mth = st.selectbox('(Month) of Transaction', ['January', 'March', 'April', 'May',  'June','July','August', 'September',  'October', 'November'])
        transac_yr = st.selectbox('(Year) of Transaction', [2012, 2013])

    
    result = ""
    
    
    if st.button('Submit'):
        result = predictor(house_age,  dist_nearest, number_of_stores,  lat, long,  transac_yr, transac_mth, transac_dayname,)
        result = np.round(result, 2)
        result= locale.format("%.2f", result, grouping= True)
        st.write("Average house price for the given area: ")
        st.success('Output (New Taiwan Dollar): '+str(result)+' NT$')
    
if __name__=='__main__':
         main()
