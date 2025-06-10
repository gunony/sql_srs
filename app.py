import streamlit as st
import pandas as pd
import duckdb

# create dataframe
data = {"a": [1,2,3], "b":[4,5,6]}
df=pd.DataFrame(data)

# Titre de la page
st.write("""
# SQL SRS
SPACED REPETITION SYSTEM SQL PRACTICE
""") #imprime titre

#Creation menu déroulant
option = st.selectbox(
    'What would you like to review ?',
    ('Joins', 'GroupBy', 'Windows Functions'),
    index=None,
    placeholder='Select a theme...'
)

st.write('Youselected:',option)
tab1, tab2 = st.tabs(["REQUETE" ,"dog"]) #defini les tab avec leur noms

with tab1:
    sql_query = st.text_area(label="entrez votre requête")
    st.write(f"la requête demandée est : {sql_query}")
    result = duckdb.query(sql_query).df() #resultat du sql converti en df
    st.dataframe(result)


