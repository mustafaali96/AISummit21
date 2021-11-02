import streamlit as st
import pymongo

# Initialize connection.
# client = pymongo.MongoClient(**st.secrets["mongo"])
client = pymongo.MongoClient("mongodb+srv://mustafa:66762532mufa@aisummit21.5l1cf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


db = client.customer_complaints
items = db.complaints.find()
items = list(items)

for item in items:
    st.write(f"{item['product']} has a :{item['complaint_what_happened']}:")

st.write("Hello world")
# st.write(items)
