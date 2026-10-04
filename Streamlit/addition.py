import streamlit as st

st.title("Addition")

number1 = st.number_input("number1")
number2 = st.number_input("number2")









if st.button("Add"):
    total = number1 + number2
    st.write(f"Sum is {total}")