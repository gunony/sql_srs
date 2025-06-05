import streamlit as st
import pandas as pd
import duckdb

# create dataframe
data = {"a": [1,2,3], "b":[4,5,6]}
df=pd.DataFrame(data)

st.write("REQUETE SQL !") #imprime titre

tab1, tab2 = st.tabs(["REQUETE" ,"dog"]) #defini les tab avec leur noms
    sql_query = st.text_area(label="entrez votre requête")
    st.write(f"la requête demandée est : {sql_query}")
    result = duckdb.query(sql_query).df() #resultat du sql converti en df
    st.dataframe(result)


