# pylint: disable = missing-module-docstring

import duckdb
import streamlit as st

# Connexion a la base db
con = duckdb.connect(database="data/exercises_sql_table.duckdb", read_only=False)


# # creation de la solution
# ANSWER_STR = """
# SELECT * FROM beverages
# CROSS JOIN food_items
# """
# solution_df = duckdb.sql(ANSWER_STR).df()

# Titre de la page
st.write(
    """
# SQL SRS
SPACED REPETITION SYSTEM SQL PRACTICE
"""
)  # imprime titre

# creation sidebar gauche
with st.sidebar:
    # Creation menu deroulant
    theme = st.selectbox(
        "What would you like to review ?",
        ("cross_joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected:", theme)

    # Récupère les données selectionné par user sur le base db
    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercise)

# Creation ligne avec la query a renseigner
st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")  # cree l'encart

# Verification de la réponse utilisateur si elle est correcte

# if query:
#     result = duckdb.sql(query).df()  # resultat du sql converti en df
#     st.dataframe(result)
#
#     # verifie le nb de colonnes de la reponse fournie ainsi que l'ordre soit correct.
#     try:
#         result = result[solution_df.columns]
#         # ordonne les colonnes du df utilisateur comme les colonnes de la solution
#         st.dataframe(result.compare(solution_df))  # compare les deux dataframe
#     except KeyError as e:
#         st.write("des colonnes sont manquantes")
#
#     # verifie le nb de lignes de la reponse.
#     n_lines_difference = result.shape[0] - solution_df.shape[0]
#     if n_lines_difference != 0:
#         st.write(
#             f"le resultat a {n_lines_difference} lignes de difference avec la solution"
#         )
#
# tab2, tab3 = st.tabs(["Tables", "Solution"])  # defini les tab avec leur noms
#
# with tab2:
#     st.write("table : beverages")
#     st.dataframe(beverages)
#     st.write("table : food_items")
#     st.dataframe(food_items)
#     st.write("table attendue")
#     st.dataframe(solution_df)
#     sql_query = st.text_area(label="entrez votre requête")
#
# with tab3:
#     st.write(ANSWER_STR)
