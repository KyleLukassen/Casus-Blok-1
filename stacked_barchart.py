import pandas as pd
import matplotlib.pyplot as plt
from load_data import load_data_from_db

outlier_bottom = 0
outlier_top = 2500
year = 2015
shown_pizzas = 10


# 2D-A Visualisatie: Visualiseer welke pizzanaam en in welke maat het meest is verkocht in 2015.
def create_stacked_barchart(remove_outlier_bottom=True, bottom_treshold=outlier_bottom,
                            remove_outlier_top=True, top_treshold=outlier_top):

    # Laadt de data uit de database.
    dataframe = load_data_from_db()

    # Zet order_date om naar datum/tijd door middel van datetime.
    dataframe['order_date'] = pd.to_datetime(dataframe['order_date'])

    # Filtert de data zodat alleen bestellingen uit het gekozen jaar overblijven.
    dataframe_for_year = dataframe[dataframe['order_date'].dt.year == year]

    # Groepeert data op naam en maat en berekent totaal aantal verkochte stuks.
    # sum() Telt de verkochte pizza's per naam en maat op.
    # reset_index() Zet de index (pizza_name en pizza_size) om naar getallen in volgorde  (0,1,2,3).
    sales = dataframe_for_year.groupby(['pizza_name', 'pizza_size'])['quantity'].sum().reset_index()

    # Sorteert de pizza's op aantal verkochte stuks, van hoog naar laag, en selecteert de top 'shown_pizzas' rijen.
    # Ascending sorteert de grafiek van hoog naar laag (False). True sorteert van laag naar hoog.
    # head() Bepaalt het aantal staven dat je wil laten zien.
    sales = sales.sort_values(by='quantity', ascending=False).head(shown_pizzas)

    # Stelt de titel van het venster in en zorgt ervoor dat deze in volledig venster opent.
    plt.figure().canvas.manager.set_window_title('Positive Potatoes - 2D-A: Stacked Barchart')
    plt.get_current_fig_manager().window.state('zoomed')

    # Verwijdert outliers als deze groter dan of kleiner dan en gelijk aan de treshold zijn.
    if remove_outlier_bottom:
        sales = sales[sales['quantity'] >= bottom_treshold]

    if remove_outlier_top:
        sales = sales[sales['quantity'] <= top_treshold]

    # Maakt een stacked barchart van de meest verkochte pizza's.
    plt.bar(sales['pizza_name'] + " (" + sales['pizza_size'] + ")", sales['quantity'], color='lightblue')

    plt.title(f'Meest verkochte pizza’s in {year}')  # Titel van het diagram.
    plt.ylabel('Aantal verkochte pizza’s')  # Hiermee pas je de tekst van het Y-label aan.
    plt.xlabel('Pizza naam (maat)')  # Hiermee pas je de tekst van het X-label aan.
    plt.xticks(rotation=45, ha='right')  # Rotatie van x-labels voor betere leesbaarheid (HA= Horizontal Alignment).
    plt.subplots_adjust(bottom=0.25)  # Zorgt voor afstand tussen de onderkant zodat alles leesbaar is.
    plt.show()  # Laat de grafiek zien.
