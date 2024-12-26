import streamlit as st 
import pandas as pd 

st.write("Welcome to AVD73")

data = {"Task":["Extract","Transform","Load"],
        "Status":["Completed","Inprogress","Pending"] }

df = pd.DataFrame(data)
st.write("ETL Pipeline Execution Process",df)
