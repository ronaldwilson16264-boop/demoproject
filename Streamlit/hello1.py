import streamlit as st

st.title("My Portfolio")
st.header("About Me")
st.write("My name is Ronald")
st.write("I am full stack developer in python language")

st.header("MY Skills")
st.subheader("Programming languages")
st.write("   python,c,c++,java   ")
st.subheader("Frameworks")
st.write("   Django   ")
st.subheader("Databases")
st.write("   MySQL,Postgres   ")





#Radio Button
g = st.radio("Gender", ['male', 'female'])
st.write(g)

#checkbox
l = st.checkbox("Python")
st.write(l)

#Select
s = st.selectbox("Places", ['Ernakulam', 'Thrissur', 'Trivandrum'])
st.write(s)