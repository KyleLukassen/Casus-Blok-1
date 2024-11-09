import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from load_data import load_data_from_db

outlier_bottom = 0
outlier_top = 200


# 3D Visualisatie: Toon per maand per pizzanaam en per maat het totaal aantal verkochte pizza’s.
def create_scatterplot(remove_outlier_bottom=True, bottom_threshold=outlier_bottom,
                       remove_outlier_top=True, top_treshold=outlier_top):

    # Laadt de data uit de database.
    dataframe = load_data_from_db()

    # Zet order_date om naar datum/tijd door middel van datetime.
    dataframe['order_date'] = pd.to_datetime(dataframe['order_date'])

    # Maanden worden opgehaald uit de 'order_date' en worden opgeslagen in een nieuwe kolom 'month'.
    dataframe['month'] = dataframe['order_date'].dt.month

    # Groepeert data op maand, pizza_name en pizza_size en telt het total_sold op.
    # .agg('sum') telt de totaal aantal verkochte pizza’s per groep op.
    # reset_index() Zet de index (month, pizza_name en pizza_size) om naar getallen in volgorde (0,1,2,3).
    grouped_data = (dataframe.groupby(['month', 'pizza_name', 'pizza_size'])
                    .agg(total_sold=('quantity', 'sum')).reset_index())

    # Zet de maten van Small (S), Medium (M) en Large (L) om naar getallen (1,2,3).
    size_to_number = {'S': 1, 'M': 2, 'L': 3}

    # map() zoekt naar de waarden in de pizza_size en die omzet naar getalen volgens de size_in_number dictionary.
    grouped_data['size_in_number'] = grouped_data['pizza_size'].map(size_to_number)

    # Stelt de titel van het venster in en zorgt ervoor dat deze in volledig venster opent.
    fig = plt.figure()
    fig.canvas.manager.set_window_title('Positive Potatoes - 3D: Scatterplot')
    plt.get_current_fig_manager().window.state('zoomed')
    ax = fig.add_subplot(projection='3d')

    # Verwijdert outliers als deze groter dan of kleiner dan en gelijk aan de treshold zijn.
    if remove_outlier_bottom:
        grouped_data = grouped_data[grouped_data['total_sold'] >= bottom_threshold]
    if remove_outlier_top:
        grouped_data = grouped_data[grouped_data['total_sold'] <= top_treshold]

    # unique() Haalt de unique categorieën op uit pizza_name.
    for pizza_name in grouped_data['pizza_name'].unique():

        # Controleert de data zodat alleen de data van de pizza_name in de loop wordt geselecteerd.
        data = grouped_data[grouped_data['pizza_name'] == pizza_name]

        # np.random.normal zorgt voor visueele spreiding van de data.
        adjusted_sizes = data['size_in_number'] + np.random.normal(0, 0.1, size=len(data))

        # Maakt een scatterplot met maand, aangepaste grootte en totaal verkochte pizza's.
        ax.scatter(data['month'], adjusted_sizes, data['total_sold'], label=pizza_name, s=50)

    ax.set_title('Verkochte Pizza\'s per Maand, Pizza Grootte en Aantal')  # Titel van het diagram.
    ax.set_ylabel('Pizza Grootte', labelpad=8)  # Hiermee pas je de tekst en afstand tussen de as van het Y-label aan.
    ax.set_yticks([1, 2, 3])  # Aanpassen van de y-as ticks om alleen 1, 2, 3 weer te geven.
    ax.set_yticklabels(['Small', 'Medium', 'Large'])  # Hiermee pas je de tekst van het Y-ticklabel aan.
    ax.set_xlabel('Maand')  # Hiermee pas je de tekst van het X-label aan.
    ax.set_xticks(np.arange(1, 13))  # Maakt een lijst van getalen aan van 1 tot 13 niet inclusief 13 (stopt bij 12).
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec'])
    ax.set_zlabel('Totaal Aantal Verkochte Pizza\'s')  # Hiermee pas je de tekst van het Z-label aan.

    plt.legend(bbox_to_anchor=(-0.6, 0.5), loc='center left')  # Zorgt voor ruimte tussen de scatterplot en legenda.
    plt.show()  # Laat de grafiek zien.

# DONEEE