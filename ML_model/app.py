import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Placement Predictor 🚀")

cgpa = st.number_input("Enter CGPA")
iq = st.number_input("Enter IQ")

if st.button("Predict"):
    result = model.predict([[cgpa, iq]])
    
    if result[0] == 1:
        st.success("Placement Milega ✅")
    else:
        st.error("Placement Nahi Milega ❌")