import streamlit as st
from datetime import date

n = st.text_input("Name")
a = st.number_input(label="Age", min_value=0)
d = st.date_input(
    label="DOB",
    min_value=date(year=1990, month=1, day=1),
    max_value=date.today(),
    value=date(year=2006, month=1, day=1),
)


e = st.text_input("Email")

g = st.radio(label="Gender", options=["male", "female"])
c = st.selectbox(label="Courses", options=["python", "dotnet", "testing", "java"])

b = st.button("Register")










if b:
  st.write("Name:", n)
  st.write("Age:", a)
  st.write("DateOfBirth:", d)
  st.write("Email:", e)
  st.write("Gender:", g)
  st.write("Course:", c)