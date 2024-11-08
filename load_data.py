import sqlite3
import pandas as pd


# Haalt de data op uit de database.
def load_data_from_db():

    # Verbindt met de database pizzasales.db.
    conn = sqlite3.connect('pizzasales.db')

    # Haalt de data op uit de pizza_sales tabel.
    query = 'SELECT * FROM pizza_sales'

    # Voert het ophalen van de data uit en laadt de data in in een dataframe (Maakt het dataframe aan).
    dataframe = pd.read_sql_query(query, conn)

    # Sluit de verbinding met de database.
    conn.close()

    # Returned het dataframe inclusief de data.
    return dataframe

# DONEEE