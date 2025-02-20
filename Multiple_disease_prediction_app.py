# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 10:08:39 2024

@author: machay
"""

import streamlit as st
import numpy as np
import pickle
from streamlit_option_menu import option_menu




heart_model=pickle.load(open('C:/Users/macha/OneDrive/Desktop/NEW PROJECT/Trained_models/heart_model.sav','rb'))

parkinsons_model=pickle.load(open('C:/Users/macha/OneDrive/Desktop/NEW PROJECT/Trained_models/parkinsons_model.sav','rb'))

diabetes_model=pickle.load(open('C:/Users/macha/OneDrive/Desktop/NEW PROJECT/Trained_models/diabetes_model.sav','rb'))





def parkinsons_model_prediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

  # reshaping the array 
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = parkinsons_model.predict(input_data_reshaped)

    if (prediction[0] == 0):
        return 'The person does not have Parkinsons disease'
    else:
        return 'The person has Parkinsons disease'



def heart_disease_predict(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

  # reshaping the array 
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = heart_model.predict(input_data_reshaped)

    if (prediction[0] == 0):
        return 'The person does not have heart disease'
    else:
        return 'The person has heart disease'




def diabetes_predict(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

  # reshaping the array 
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = diabetes_model.predict(input_data_reshaped)

    if (prediction[0] == 0):
        
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'


    
with st.sidebar:
        selected=option_menu('Multiple disease prediction',
                     ['Diabetes prediction',
                      'heart disease prediction',
                       'parkinsons prediction'],
                     icons=['activity','heart','person'])
        
if(selected=='Diabetes prediction'):
        
        st.title('Diabetes Prediction')
        
        c1,c2,c3=st.columns(3)
        
        with c1:
            Pregnancies=st.text_input('No.of Pregnancies')
            
        with c2:
            Glucose=st.text_input('Glucose Level')
            
        with c3:
            BloodPressure=st.text_input('BloodPressure Value')
            
        with c1:
            SkinThickness=st.text_input('SkinThickness Value')
            
        with c2:
            Insulin=st.text_input('Insulin Level')
            
        with c3:
            BMI=st.text_input('BMI Value')
            
        with c1:
            DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction')
            
        with c2:
            Age=st.text_input('Age')
            
        output=''
        
        if st.button('Diabetes Test Result'):
            output=diabetes_predict([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
            
        st.success(output)
            
if(selected=='heart disease prediction'):
        
        st.title('Heart Disease Prediction')
        
        c1,c2,c3,c4=st.columns(4)
   
        with c1:
           age=st.text_input('Age')
       
        with c2:
           sex=st.text_input('Sex')
       
        with c3:
           chest_pain=st.text_input('Chest Pain types')
       
        with c4:
           restbp=st.text_input('Resting Blood Pressure')
       
        with c1:
           chol=st.text_input('Serum Cholestoral in mg/dl')
       
        with c2:
           fbs=st.text_input('Fasting Blood Sugar > 120 mg/dl')
       
        with c3:
           restecg=st.text_input('Resting Electrocardiographic results')
       
        with c4:
           thalach=st.text_input('Maximum Heart Rate achieved')
       
        with c1:
           exang=st.text_input('Exercise Induced Angina')
       
        with c2:
           oldpeak=st.text_input('ST depression induced by exercise')
       
        with c3:
           slope=st.text_input('Slope of the peak exercise ST segment')
       
        with c4:
           ca=st.text_input('Major vessels colored by flourosopy')
       
        with c1:
          thal=st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
       

        output=''
   
        if st.button('Heart Disease Test Result'):
              output=heart_disease_predict([age,sex,chest_pain,restbp,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])                          
       
        st.success(output)
       
   
if(selected=='parkinsons prediction'):
        
    st.title('Parkinsons Prediction')
        
    c1,c2,c3,c4,c5=st.columns(5)  
    
    with c1:
        fo=st.text_input('MDVP:Fo(Hz)')
        
    with c2:
        fhi=st.text_input('MDVP:Fhi(Hz)')
        
    with c3:
        flo=st.text_input('MDVP:Flo(Hz)')
        
    with c4:
        Jitter_percent=st.text_input('MDVP:Jitter(%)')
        
    with c5:
        Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')
        
    with c1:
        RAP=st.text_input('MDVP:RAP')
        
    with c2:
        PPQ=st.text_input('MDVP:PPQ')
        
    with c3:
        DDP=st.text_input('Jitter:DDP')
        
    with c4:
        Shimmer=st.text_input('MDVP:Shimmer')
        
    with c5:
        Shimmer_dB=st.text_input('MDVP:Shimmer(dB)')
        
    with c1:
        APQ3=st.text_input('Shimmer:APQ3')
        
    with c2:
        APQ5=st.text_input('Shimmer:APQ5')
        
    with c3:
        APQ=st.text_input('MDVP:APQ')
        
    with c4:
        DDA=st.text_input('Shimmer:DDA')
        
    with c5:
        NHR=st.text_input('NHR')
        
    with c1:
        HNR=st.text_input('HNR')
        
    with c2:
        RPDE=st.text_input('RPDE')
        
    with c3:
        DFA=st.text_input('DFA')
        
    with c4:
        spread1=st.text_input('spread1')
        
    with c5:
        spread2=st.text_input('spread2')
        
    with c1:
        D2=st.text_input('D2')
        
    with c2:
        PPE=st.text_input('PPE')
        
    output=''
   
    if st.button("Parkinson's Test Result"):
        output=parkinsons_model_prediction([fo,fhi,flo,Jitter_percent,Jitter_Abs,RAP,PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE])  
       
    st.success(output)
       
   
    
        
        
        

    
    
    
    
    
    
    
    
       
        
        
        

    
    
    
    
    
    
    
    
    
    