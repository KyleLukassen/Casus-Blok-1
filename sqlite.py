import sqlite3
import pandas as pd
import os


# Plaatst de data in de database.
def import_excel_to_db():
    data = pd.read_excel('pizzasales.xlsx')
    dataframe = pd.DataFrame(data)
    conn = sqlite3.connect('pizzasales.db')
    cursor = conn.cursor()

    # Maakt een tablad voor pizza_sales in de database als deze nog niet bestaat.
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pizza_sales (
        order_details_id INTEGER,
        order_id INTEGER,
        pizza_id TEXT,
        quantity INTEGER,
        order_date TEXT,
        order_time TEXT,
        unit_price REAL,
        total_price REAL,
        pizza_size TEXT,
        pizza_category TEXT,
        pizza_ingredients TEXT,
        pizza_name TEXT
    )
    ''')

    dataframe.to_sql('pizza_sales', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()


# Haalt de data op de database, als er geen database bestaat wordt deze aangemaakt.
def check_for_data_and_import():
    # Controleer of de databasebestand bestaat
    if not os.path.exists('pizzasales.db'):
        print('Database bestaat niet. Data wordt geïmporteerd vanuit pizzasales.xlsx.')
        import_excel_to_db()  # Maak de database en vul met Excel-data
    else:
        print('Database bestaat al. Data wordt ingeladen vanuit pizzasales.xlsx')

    # Legt verbinding met de database.
    conn = sqlite3.connect('pizzasales.db')
    cursor = conn.cursor()

    # Controleert of de tabel pizza_sales al in de database bestaat.
    cursor.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'pizza_sales\';')

    # Laad de data in een DataFrame en sluit de verbinding met de database.
    dataframe = pd.read_sql_query('SELECT * FROM pizza_sales', conn)
    conn.close()
    return dataframe
