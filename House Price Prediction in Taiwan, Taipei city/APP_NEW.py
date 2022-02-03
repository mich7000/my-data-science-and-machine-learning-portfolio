# necessary python libraries.
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from joblib import load

import locale
l = locale.setlocale(locale.LC_ALL, 'en_US')



# loading saved models
FILE_1 = 'output/SUPPORT_VECTOR_MODEL.pkl'
model_= load(FILE_1)

st.set_page_config(page_title='house price predictor app.')

# interfaces
st.markdown("""<font size=5.5><b>Project 2</b> - Predict the average house price of a given area in Taiwan, New Taipei city.</font>""", 
    unsafe_allow_html=True)
st.image('images/front.jpg') 
st.markdown("""<i>Sindian District, New Taipei City, Taiwan.</i>""", 
    unsafe_allow_html=True)

st.markdown("""<font size=4><b>Brief Analysis</font></b>""", 
    unsafe_allow_html=True) 

my_expander = st.expander(label="Click to Exapnd")
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
           

        
        
        
st.markdown("""<font size=5>Predict the **House Price** of a given area.</font>""", 
    unsafe_allow_html=True)
st.write('*Please fill every entry provided (and also with the right data type) to avoid any errors.*')



def predictor(house_age,  dist_nearest, number_of_stores, ):
    new_instance = [house_age,  
                    dist_nearest, number_of_stores, ]
    new = pd.DataFrame(new_instance, index=['house age', 'dist to nearest MRT', 'number of convenience stores',]).T
    prediction= model_.predict(new)[0] * 10000
    return prediction


# main program where ML computations occurs..
def main():
    
        house_age= st.text_input('House Age', 0.0)
        number_of_stores = st.selectbox('Number of convenient stores (select 10 if higher)', np.arange(1, 11))
        dist_nearest= st.text_input('Distance to the nearest MRT station', 0.0)

        result = ""
    
    
        if st.button('Submit'):
            result = predictor(house_age,  dist_nearest, number_of_stores, )
            result = np.round(result, 2)
            result= locale.format("%.2f", result, grouping= True)
            st.write("Average house price for the given area: ")
            st.success('Output (New Taiwan Dollar): '+str(result)+' NT$')
    
if __name__=='__main__':
         main()
