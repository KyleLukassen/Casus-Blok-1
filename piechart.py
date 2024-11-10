import matplotlib.pyplot as plt
from load_data import load_data_from_db

outlier_bottom = 0
outlier_top = 100
percentage = 100


# 1D Visualisatie: Visualiseer per pizzacategorie het percentage verkochte pizza’s.
def create_piechart(remove_outlier_bottom=True, bottom_treshold=outlier_bottom,
                    remove_outlier_top=True, top_treshold=outlier_top):

    # Laadt de data uit de database.
    dataframe = load_data_from_db()

    # Groepeert de data per pizzacategorie.
    # count() telt het aantal bestellingen in order_details_id (+1). Dit alleen als het veld niet leeg is (geen waarde).
    pizza_category = dataframe.groupby('pizza_category')['order_details_id'].count()

    # Berekent het verkooppercentage per categorie, sum() geeft totaal aantal bestellingen voor alle categorieën.
    sales_percentage = (pizza_category / pizza_category.sum()) * percentage

    # Stelt de titel van het venster in en zorgt ervoor dat deze in volledig venster opent.
    plt.figure().canvas.manager.set_window_title('Positive Potatoes - 1D: Piechart')
    plt.get_current_fig_manager().window.state('zoomed')

    # Verwijdert outliers als deze groter dan of kleiner dan en gelijk aan de treshold zijn.
    if remove_outlier_bottom:
        sales_percentage = sales_percentage[(sales_percentage >= bottom_treshold)]
    if remove_outlier_top:
        sales_percentage = sales_percentage[(sales_percentage <= top_treshold)]

    # Maakt de pierchart aan op basis van sales_percentage.
    sales_percentage.plot(kind='pie',  # Het type van de grafiek in dit geval een piechart.
                          autopct='%1.0f%%',  # Geeft het percentage in heel getal terug (1.1 geeft float terug).
                          startangle=90,  # De hoek waaruit de piechart begint.
                          colors=['skyblue', 'lightgreen', 'coral', 'lightpink'])  # Kleuren van de categorieën.

    plt.title('Percentage verkochte pizza’s per categorie:')  # Titel van het diagram.
    plt.ylabel('')  # Hiermee pas je de tekst van het Y-label aan (Niet nodig in een piechart vandaar dat deze leeg is).
    plt.axis('equal')  # Zorgt ervoor dat de piechart rond is in plaats van ovaal door de X en Y as gelijk te houden.
    plt.show()  # Laat de grafiek zien.
