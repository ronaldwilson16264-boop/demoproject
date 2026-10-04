import streamlit as st

st.title("BMI Calculator")

weight = st.number_input("weight in kg")
height = st.number_input("height in cm")






if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / ((height / 100) ** 2)
        st.write(f"bmi: {bmi:.2f}")
        
        if bmi < 18.5:
            st.write("---underweight")
        elif 18.5 <= bmi < 25:
            st.write("---normal")
        elif 25 <= bmi < 30:
            st.write("--overweight")
        else:
            st.write("--obesity")