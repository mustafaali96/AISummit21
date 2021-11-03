import streamlit as st
import pymongo
import pandas as pd

# Initialize connection.
client = pymongo.MongoClient("mongodb+srv://mustafa:66762532mufa@aisummit21.5l1cf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.customer_complaints
cursor_items = db.complaints.find()

st.title('AI Summit 21 Demo!')
# st.header('This is a header')

st.write("Total Records", cursor_items.count(), 
         "Timely Done", db.complaints.count_documents({ "timely": "Yes"}), 
         "Timely Not Done", db.complaints.count_documents({ "timely": {"$ne":"Yes"}}))


all_records = []
for item in cursor_items:
    del item['_id']
    all_records.append(item)
df = pd.DataFrame(all_records)

st.table(df)
