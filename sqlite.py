import sqlite3
import pandas as pd
import os

# Functie om de Excel-data eenmalig te importeren in de database
def import_excel_to_db():
    data = pd.read_excel('pizzasales.xlsx')
    df = pd.DataFrame(data)

    conn = sqlite3.connect('pizzasales.db')
    cursor = conn.cursor()

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

    df.to_sql('pizza_sales', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

# Functie om data uit de database te laden, en zo nodig de database aan te maken
def load_data_from_db():
    # Controleer of de databasebestand bestaat
    if not os.path.exists('pizzasales.db'):
        print('Database bestaat niet. Data wordt geïmporteerd vanuit pizzasales.xlsx.')
        import_excel_to_db()  # Maak de database en vul met Excel-data
    else:
        print('Database bestaat al. Data wordt ingeladen vanuit pizzasales.xlsx')

    # Verbind met de database en controleer of de tabel bestaat
    conn = sqlite3.connect('pizzasales.db')
    cursor = conn.cursor()

    # Controleer of de tabel bestaat
    cursor.execute('SELECT name FROM sqlite_master WHERE type=\'table\' AND name=\'pizza_sales\';')
    table_exists = cursor.fetchone()

    # Laad de data in een DataFrame
    df = pd.read_sql_query("SELECT * FROM pizza_sales", conn)
    conn.close()
    return df