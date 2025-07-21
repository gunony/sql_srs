# pylint: disable = missing-module-docstring
import ast

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
        "Que souhaitez-vous réviser ?",
        ("cross_joins", "GroupBy", "window_functions"),
        index=None,
        placeholder="Choisissez le theme...",
    )
    st.write("Vous avez choisi :", theme)

    # Récupère les données dans la base db et imprime le tableau
    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercise)

# Creation ligne avec la query à renseigner
st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")  # cree l'encart

# Verification de la réponse utilisateur si elle est correcte

if query:
    try :
        result = con.execute(query).df()  # resultat du sql converti en df
        st.dataframe(result)
    except :
        st.write("LA REQUETE SQL N'EST PAS EXECUTABLE ! IL FAUT LA CORRIGER.")

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
tab2, tab3 = st.tabs(["Tables", "Solution"])  # defini les onglets.

with tab2:
    exercise_tables = ast.literal_eval(exercise.loc[0,"tables"]) #recup les noms des tables à afficher
    for table in exercise_tables: # creer une boucle pour chaque table
        st.write(f"table: {table}") # inscrire nom de la table
        df_table = con.execute(f"SELECT * FROM {table}").df() #recupere la table depuis db et convertit en dataframe
        st.dataframe(df_table) # apparaitre la table

with tab3:
    exercise_name = exercise.loc[0,"exercise_name"]
    with open(f"data/{exercise_name}.sql", "r") as f: #ouvre le fichier sql et l'associe a l'objet f
        answer = f.read() #lit l'objet f précédement ouvert
    st.write(answer)
