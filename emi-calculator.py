import streamlit as st
import numpy as np
import pandas as pd

@st.cache()
def calculate_emi(p , n , r):
  emi = p * (r/100) * ((1 + (r/100))**n)/(((1 + (r/100))**n) - 1)
  return round(emi , 3)

st.title("EMI Calculator App") 

principle = st.slider("Principal Loan Amount" , 1000.0 , 1000000.0)
tenure = st.slider("Loan period (in years)" , 1.0 , 30.0)
roi = st.slider("	Rate of Interest (in % per annum)" , 1.0 , 15.0)

if st.button("Calculate"):
  ans = calculate_emi(principle , tenure*12 , roi/12)
  st.write("Calculate EMI:" , ans)