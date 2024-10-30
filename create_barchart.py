import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("PizzaSales.xlsx")  # Dataset aanmaken
df = pd.DataFrame(data)  # DataFrame aanmaken

# 2D Visualisatie: Visualiseer welke pizzanaam en in welke maat het meest is verkocht in 2015.


def create_barchart():
    # plt.subplot(2, 2, 2)  # Zet de grafiek in de 4e positie van een 2x2 grid
    year = 2015
    shown_pizzas = 1000

    df['order_date'] = pd.to_datetime(df['order_date'])  # Zorg ervoor dat de order_date kolom het juiste datatype heeft
    df_for_year = df[df['order_date'].dt.year == year]  # Filter de data voor het aangegeven jaar
    sales = df_for_year.groupby(['pizza_name', 'pizza_size'])['quantity'].sum().reset_index()  # Groeperen van data
    sales = sales.sort_values(by='quantity',   # Ascending betekend van hoog naar laag (True = Laag > Hoog)
                              ascending=False).head(shown_pizzas)  # Hoe groter de shown_pizzas hoe meer pizza's je ziet

    # Maak een staafdiagram
    plt.bar(sales['pizza_name'] + " (" + sales['pizza_size'] + ")", sales['quantity'], color='lightblue')
    plt.title('Meest verkochte pizza’s in 2015')
    plt.xlabel('Pizza naam (maat)')
    plt.ylabel('Aantal verkochte pizza’s')
    plt.xticks(rotation=45, ha='right')  # Rotatie van x-labels voor betere leesbaarheid


plt.figure().canvas.manager.set_window_title('Casus Positive Patatoes')  # Aanpassen titel
plt.get_current_fig_manager().window.state('zoomed')  # Automatisch gemaximaliseerd openen

create_barchart()
plt.show()