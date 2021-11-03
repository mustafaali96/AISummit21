import streamlit as st
import pymongo
import pandas as pd
# from pandas.io.json import json_normalize

# Initialize connection.
# client = pymongo.MongoClient(**st.secrets["mongo"])
client = pymongo.MongoClient("mongodb+srv://mustafa:66762532mufa@aisummit21.5l1cf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


db = client.customer_complaints
cursor_items = db.complaints.find()
# items = list(cursor_items)
# df = pd.DataFrame(items)
# df = json_normalize(list(cursor_items))

st.title('AI Summit 21 Demo!')
# st.header('This is a header')

st.write("Total Records", cursor_items.count(), "Timely Done", db.complaints.count_documents({ "timely": "Yes"}), "Timely Not Done", db.complaints.count_documents({ "timely": {"$ne":"Yes"}}))


all_records = []
for item in cursor_items:
    # st.write(f"{item['product']} has a :{item['complaint_what_happened']}:")
    all_records.append(item)
df = pd.DataFrame(all_records)

st.write(df)
