import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def load_data_from_db():
    conn = sqlite3.connect('pizzasales.db')
    query = 'SELECT * FROM pizza_sales'
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# 2D-B Visualisatie: Visualiseer per pizzacategorie de pizzanamen en toon het verkochte aantal.


def create_barchart():
    df = load_data_from_db()  # Laad de data uit de database
    # Groepeer per pizzacategorie en naam, tel de verkochte aantallen
    category_sales = df.groupby(['pizza_category', 'pizza_name'])['quantity'].sum().reset_index()

    # Voor elke pizzacategorie een aparte kleur
    categories = category_sales['pizza_category'].unique()
    colors = plt.colormaps['tab10']  # Gebruik een colormap voor verschillende kleuren

    plt.figure().canvas.manager.set_window_title('Positive Patatoes - 2D-B: Barchart')  # Aanpassen titel
    plt.get_current_fig_manager().window.state('zoomed')  # Automatisch gemaximaliseerd openen

    # Maak een staafdiagram
    for i, category in enumerate(categories):
        category_data = category_sales[category_sales['pizza_category'] == category]
        plt.bar(category_data['pizza_name'], category_data['quantity'],
                label=category, color=colors(i), alpha=0.7)  # Gebruik een doorzichtigheid voor overlappen

    plt.title('Aantal verkochte pizza’s per pizzacategorie en naam')
    plt.xlabel('Pizza naam')
    plt.ylabel('Aantal verkochte pizza’s')
    plt.xticks(rotation=45, ha='right')  # Rotatie van x-labels voor betere leesbaarheid
    plt.subplots_adjust(bottom=0.3)  # Zorgt voor afstand tussen de onderkant zodat alles leesbaar is.
    plt.legend(title='Pizzacategorie')  # Toon de legenda voor categorieën
    plt.show()
