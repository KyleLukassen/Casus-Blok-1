import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def load_data_from_db():
    conn = sqlite3.connect('pizzasales.db')
    query = 'SELECT * FROM pizza_sales'
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# 1D Visualisatie: Visualiseer per pizzacategorie het percentage verkochte pizza’s.


def create_piechart():
    df = load_data_from_db()  # Laad de data uit de database
    percentage = 100

    # Groepeert het aantal bestellingen per pizzacategorie in de dataset
    pizza_category = df.groupby('pizza_category')['order_details_id'].count()

    # Berekent het verkooppercentage per pizzacategorie, elk aantal delen door de som en vermenigvuldigen met percentage
    sales_percentage = (pizza_category / pizza_category.sum()) * percentage

    plt.figure().canvas.manager.set_window_title('Positive Patatoes - 1D: Piechart')  # Aanpassen titel van het venster
    plt.get_current_fig_manager().window.state('zoomed')  # Automatisch gemaximaliseerd openen

    sales_percentage.plot(kind='pie',  # Type grafiek (in dit geval een cirkeldiagram)
                         autopct='%1.0f%%',  # Automatisch percentage > 1.1 betekend 1 cijfer achter komma, 1.0 geen
                         startangle=90,  # De hoek waaruit de piechart begint
                         colors=['skyblue', 'lightgreen', 'coral', 'lightpink'])  # Kleuren voor verschillende categorie

    plt.ylabel('')  # Verwijdert het label van de Y-as voor een nettere weergave
    plt.title('Percentage verkochte pizza’s per categorie:')  # Titel van het diagram
    plt.axis('equal')  # Zorgt ervoor dat de piechart rond is in plaats van ovaal
    plt.show()