import matplotlib.pyplot as plt
from load_data import load_data_from_db

outlier_bottom = 0
outlier_top = 2500


# 2D-B Visualisatie: Visualiseer per pizzacategorie de pizzanamen en toon het verkochte aantal.
def create_barchart(remove_outlier_bottom=True, bottom_treshold=outlier_bottom,
                    remove_outlier_top=True, top_treshold=outlier_top):

    # Laadt de data uit de database.
    dataframe = load_data_from_db()

    # Groepeert de data per pizzacategorie en naam. Telt het verkochte aantal op per naam en categorie.
    # sum() telt het aantal verkochte pizza's per pizzacategorie en naam op.
    # reset_index() Zet de index (pizza_category en pizza_name) om naar getallen in volgorde  (0,1,2,3).
    category_sales = dataframe.groupby(['pizza_category', 'pizza_name'])['quantity'].sum().reset_index()

    # unique() Haalt de unique categorieën op uit pizza_category.
    categories = category_sales['pizza_category'].unique()

    # Stelt de titel van het venster in en zorgt ervoor dat deze in volledig venster opent.
    plt.figure().canvas.manager.set_window_title('Positive Patatoes - 2D-B: Barchart')
    plt.get_current_fig_manager().window.state('zoomed')

    # Verwijdert outliers als deze groter dan of kleiner dan en gelijk aan de treshold zijn.
    if remove_outlier_bottom:
        category_sales = category_sales[category_sales['quantity'] >= bottom_treshold]
    if remove_outlier_top:
        category_sales = category_sales[category_sales['quantity'] <= top_treshold]

    # Itereert door pizzacategorieën om een barchart te maken voor elke categorie.
    for category in categories:

        # Controleert of de pizzacategorie gelijk is aan de huidige categorie die wordt verwerkt in de loop.
        category_data = category_sales[category_sales['pizza_category'] == category]

        #  Maakt de barchart aan voor de pizzacategorie met de naam en het aantal verkochte pizza's.
        plt.bar(category_data['pizza_name'], category_data['quantity'],
                label=category,  # Voegt de pizzacategorie toe aan de legenda.
                alpha=0.7)  # Transparant effect voor de bars zodat de oogjes niet gaan branden.

    plt.title('Aantal verkochte pizza’s per pizzacategorie en naam')  # Titel van het diagram.
    plt.ylabel('Aantal verkochte pizza’s')  # Hiermee pas je de tekst van het het Y-label aan.
    plt.xlabel('Pizza naam')  # Hiermee pas je de tekst van het X-label aan.
    plt.xticks(rotation=45, ha='right')  # Rotatie van x-labels voor betere leesbaarheid (HA= Horizontal Alignment).
    plt.subplots_adjust(bottom=0.3)  # Zorgt voor afstand tussen de onderkant zodat alles leesbaar is.
    plt.legend(title='Pizzacategorie')  # Toon de legenda voor de categorieën.
    plt.show()  # Laat de grafiek zien.

# DONEEE