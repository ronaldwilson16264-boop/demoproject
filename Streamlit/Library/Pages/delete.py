import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Delete Record")

i = st.number_input(label="Enter Id", min_value=0)
btn = st.button("Delete")

if btn:
    b = BookListCreateRetrieveUpdateDelete()
    record = b.delete(i)
    print(record)
    if record:
        st.success("Record deleted Successfully")
    else:
        st.error("No Record Found")