import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Update Record")

i = st.number_input(label="ID", min_value=0)
t = st.text_input("Title")
a = st.text_input("Author")
p = st.number_input(label="Price", min_value=0)
pg = st.number_input(label="Pages", min_value=0)
l = st.text_input("Language")

btn = st.button("Update")

if btn:
    b = BookListCreateRetrieveUpdateDelete()
    record = b.update(i, t, a, p, pg, l)
    print(record)
    if record:
        st.success("Updated successfully")
    else:
        st.error("No Record Found")