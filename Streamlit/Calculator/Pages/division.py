import streamlit as st

num1 = st.number_input(label="Enter num1", min_value=0)
num2 = st.number_input(label="Enter num2", min_value=0)

btn = st.button("DIVIDE")

if btn:
    s = num1 / num2
    st.write("Quotient is", s)