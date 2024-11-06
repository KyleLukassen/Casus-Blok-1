import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def load_data_from_db():
    conn = sqlite3.connect('pizzasales.db')
    query = 'SELECT * FROM pizza_sales'
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# 2D-A Visualisatie: Visualiseer welke pizzanaam en in welke maat het meest is verkocht in 2015.


def create_stacked_barchart():
    year = 2015
    shown_pizzas = 10
    df = load_data_from_db()  # Laad de data uit de database
    df['order_date'] = pd.to_datetime(df['order_date'])  # Zet de kolom order_date om naar datum/tijd
    df_for_year = df[df['order_date'].dt.year == year]  # Filtert data voor bestellingen in het gekozen jaar

    # Groepeert data per pizza en grootte en berekent totaal aantal verkochte stuks
    sales = df_for_year.groupby(['pizza_name', 'pizza_size'])['quantity'].sum().reset_index()

    # Sorteert de pizza's op aantal verkochte stuks, van hoog naar laag, en selecteert de top 'shown_pizzas' rijen
    sales = sales.sort_values(by='quantity', ascending=False).head(shown_pizzas)

    plt.figure().canvas.manager.set_window_title('Positive Patatoes - 2D-A: Stacked Barchart')  # Aanpassen titel van het venster
    plt.get_current_fig_manager().window.state('zoomed')  # Automatisch gemaximaliseerd openen

    # Maakt een staafdiagram van de meest verkochte pizza's en toont het aantal verkochte stuks
    plt.bar(sales['pizza_name'] + " (" + sales['pizza_size'] + ")", sales['quantity'], color='lightblue')

    plt.title('Meest verkochte pizza’s in 2015')  # Titel van het diagram
    plt.xlabel('Pizza naam (maat)')  # Verwijderen/toevoegen van label X-as
    plt.ylabel('Aantal verkochte pizza’s')  # Verwijderen/toevoegen van label Y-as
    plt.xticks(rotation=45, ha='right')  # Rotatie van x-labels voor betere leesbaarheid. Ha=Horizontal alignment
    plt.subplots_adjust(bottom=0.25)  # Zorgt voor afstand tussen de onderkant zodat alles leesbaar is.
    plt.show()
