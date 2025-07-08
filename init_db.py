# pylint: disable = missing-module-docstring

import io
import duckdb
import pandas as pd

# creation de la connexion a la table sql
con = duckdb.connect(database="data/exercises_sql_table.duckdb", read_only=False)

#-----------------------------------------------------------------------------
# EXERCISES LIST
#-----------------------------------------------------------------------------
# creation du dictionnaire avec détail theme, exo,...
data = {
     "theme": ["cross_joins", "window_functions"],
     "exercise_name": ["beverages_and_food", "simple_window"],
     "tables": [["beverages","food_items"], "simple_window"],
     "last_reviewed": ["1970-01-01","1970-01-01"]
}
memory_state_df = pd.DataFrame(data)
con.execute("CREATE TABLE IF NOT EXISTS memory_state AS SELECT * FROM memory_state_df")

#-----------------------------------------------------------------------------
# CROSS JOIN EXERCISES
#-----------------------------------------------------------------------------

# creation des dataframes
CSV = """
beverage,price
orange juice,2.5
expresso,2
tea,3
"""
beverages = pd.read_csv(io.StringIO(CSV))
# io.StringIO : permet de simuler un fichier en mémoire à partir de cette chaîne de caractères.

# creation de la table beverages sur la connexion de depart.
con.execute("CREATE TABLE IF NOT EXISTS beverages AS SELECT * FROM beverages")

CSV2 = """
food_item,food_price
cookie,2.5
chocolatine,2
muffin,3
croissant,2.8
"""
food_items = pd.read_csv(io.StringIO(CSV2))

#creation de la table food a partir de la connexion de depart.
con.execute("CREATE TABLE IF NOT EXISTS food_items AS SELECT * FROM food_items")
