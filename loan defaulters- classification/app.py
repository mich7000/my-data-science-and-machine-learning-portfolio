
# libraries to help build the web application
import streamlit as st
from joblib import  load
import pandas as pd
import numpy as np
import datetime

# we load the model we built using random forest.
FILE= 'output/tuned_rf.pkl' 
model= load(open(FILE, 'rb'))
st.set_page_config(page_title='loan defaulters predictor app.')
# header and intro code..
st.write("Today's Date: ", str(datetime.datetime.today()).split()[0])
st.header("Project 3 -  Predict where a loan applicant will default a loan or not.")
st.write("Classify loan applicants into defaulters and non-defaulters.")
st.image('images/front.jpg')
st.markdown("""
            Build a model to classify loan applicant to whether they will default a loan or not.
            This web application runs on model built with random forest algorithm.\n
            
            Thresholds and Metrics
            -----------------------
            **model threshold**: 0.5\n
            **f1 score (class N)**: 54% (Approx).\n
            **f1 score (class Y)**: 84% (Approx)
            """, 
            unsafe_allow_html=True)
            
st.subheader("**Note**")
st.write("*Please fill all entries before you click the **submit** button in other to avoid any errors*")

# predictor function
def predictor(dependents, 
              education, 
              selfemp,  
              property_area,
              term_range,
              applicant_income_range,
              coapp_income_range,
              appincome, 
              coappincome, 
              loan_amt,
              term_loan_amount,
              credit_history):
              
    new_instance = [    dependents, 
                        education, 
                        selfemp,  
                        property_area,
                        term_range,
                        applicant_income_range,
                        coapp_income_range,
                        appincome, 
                        coappincome, 
                        loan_amt,
                        term_loan_amount,
                        credit_history]
                     
    new = pd.DataFrame(new_instance, index=['Dependents',
                                            'Education',
                                            'Self_Employed',
                                            'Property_Area',
                                            'Loan_Amount_Term1',
                                            'app_income_cut',
                                            'coapp_income_cut',
                                            'ApplicantIncome',
                                            'CoapplicantIncome',
                                            'LoanAmount',
                                            'Loan_Amount_Term',
                                            'Credit_History',]).T
    prediction= model.predict(new)[0]
    
    if prediction == 0:
        out = 'Deny'
    elif prediction == 1:
        out  = "Approve"

    return out


# application interface code...
def main():
    

    frame1, frame2= st.beta_columns([4, 6])
    
    with frame1:
        dependents = st.selectbox('Dependents', ['0', '1', '2', '3+'])
        education = st.radio('Education', ['Graduate', 'Not Graduate'])
        selfemp= st.selectbox('Employment Status (Self Employed)', ['No', 'Yes'])
        property_area = st.radio('Propery Area', ['Rural', 'Urban', 'Semiurban'])
     
    with frame2:
        appincome= st.text_input( 'Applicant Income', 0.0)
        
        applicant_income_range = st.selectbox("Applicant's Income Range (Choose the appropriate range of Applicant's income )", 
                                                                                                ['0-12.5K', '12.5K-25K', '25K+'])
       
        if np.float(appincome) < 12500:
            applicant_income_range == '0-12.5K'
            
        elif np.float(appincome) >=12500 and  np.float(appincome) < 25000:
            applicant_income_range ==  '12.5K-25K'

        else:
            applicant_income_range ==  '25K+'

            
        credit_history= st.radio('Applicant Credit History', [0., 1.])
        coappincome = st.text_input(  "Co-Applicant Income", 0.0)
        coapp_income_range = st.selectbox("Co-Applicant's Income Range (Choose the appropriate range of Co-Applicant's income )", ['0-5K','5K-10K', '10K+', ])

        if np.float(coappincome) < 5000:
            coapp_income_range == '0-5K'
            
        elif np.float(coappincome) >=5000 and  np.float(coappincome) < 10000:
            coapp_income_range ==  '5K-10K'

        else:
            coapp_income_range ==  '10K+'

        loan_amt = st.text_input('Loan Amount',"type here")
        term_loan_amount = st.text_input('Term of the Loan', 0.)

        warn= """Loan's Term Range \n (Please choose the appropriate term range from the **Term of the Loan*** to avoid misclassifcation.)"""
        term_range = st.selectbox(warn, ['200-500', '100-200', '10-100'])

        if np.float(term_loan_amount) >=10 and np.float(term_loan_amount) < 100:
            term_range  == '10-100'
        elif np.float(term_loan_amount) >=100 and np.float(term_loan_amount) < 200:
            term_range == '100-200'
        else:
            term_range == '200-500'
    
    result = str()
    
    if st.button('submit'):
            result = predictor( dependents, 
              education, 
              selfemp,  
              property_area,
              term_range,
              applicant_income_range,
              coapp_income_range,
              appincome, 
              coappincome, 
              loan_amt,
              term_loan_amount,
              credit_history)[:]
            result = result
        
            st.success('LOAN STATUS: '+str(result))
    
    with st.beta_expander('help'):
        
        info= """ \n [Approve] - **Approve** loan application of the client.
                  \n [Deny] - **Deny** loan application of the client.
                  \n The boolean values underneath the range boxes shows if you have selected the right range.
                  \n**true** - indicates you have selected the right range.
                  \n**false** - indicates the range you have selected is incorrect.
                  """
        st.success(info)


    with st.beta_expander('About'):
        about_me = st.markdown(
                   """
                     **Author(s)**: Aboagye Michael, Student, Machine Learning and Data science enthusiast.\n
                     **Last Modified**: September-2021\n
                     **Project type**: Personal
                   """, unsafe_allow_html=True
                   )




# activates the app.   
if __name__=='__main__':
         main()


     
 