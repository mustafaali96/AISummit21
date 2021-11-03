import streamlit as st
import pymongo
import pandas as pd

# Initialize connection.
# client = pymongo.MongoClient(**st.secrets["mongo"])
client = pymongo.MongoClient("mongodb+srv://mustafa:66762532mufa@aisummit21.5l1cf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


db = client.customer_complaints
cursor_items = db.complaints.find()
items = list(cursor_items)
df = pd.DataFrame(items)

st.title('AI Summit 21 Demo!')
# st.header('This is a header')

st.write("Total Records", cursor_items.count())
st.write("Timely Done", db.complaints.count_documents({ "timely": "Yes"}))
st.write("Timely Not Done", db.complaints.count_documents({ "timely": {"$ne":"Yes"}}))

# for item in items:
#     st.write(f"{item['product']} has a :{item['complaint_what_happened']}:")

st.write(df)
