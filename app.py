import streamlit as st
import pymongo
import pandas as pd

from streamlit_pandas_profiling import st_profile_report

from pandas_profiling import ProfileReport



# Initialize connection.
client = pymongo.MongoClient("mongodb+srv://mustafa:66762532mufa@aisummit21.5l1cf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.customer_complaints
cursor_items = db.complaints.find()

st.title('AI Summit 21 Demo!')
st.header('Financial Consumer Complaints Dashboard')

st.write("Total Complaints Count", cursor_items.count(), 
         "Timely Done Complaints", db.complaints.count_documents({ "timely": "Yes"}), 
         "Timely Not Done", db.complaints.count_documents({ "timely": {"$ne":"Yes"}}),
         "No of States", len(db.complaints.distinct( "state" ))
         )


all_records = []
for item in cursor_items:
    del item['_id']
    all_records.append(item)
df = pd.DataFrame(all_records)


profile = ProfileReport(df,

                        title="Financial Consumer Data",

        dataset={

        "description": "This is the Demo of AI Summit 21",
        "Demo URL": "https://github.com/mustafaali96/AISummit21"

    }
)
st_profile_report(profile)
# st.table(df)
