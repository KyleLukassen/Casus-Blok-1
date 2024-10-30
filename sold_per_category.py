import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("PizzaSales.xlsx")  # Dataset aanmaken
df = pd.DataFrame(data)  # DataFrame aanmaken

def sold_per_category():
    # plt.subplot(2, 2, 4)
    # Groepeer per pizzacategorie en naam, tel de verkochte aantallen
    category_sales = df.groupby(['pizza_category', 'pizza_name'])['quantity'].sum().reset_index()

    # Voor elke pizzacategorie een aparte kleur
    categories = category_sales['pizza_category'].unique()
    colors = plt.cm.get_cmap('tab10', len(categories))  # Gebruik een colormap voor verschillende kleuren

    # Maak een staafdiagram
    for i, category in enumerate(categories):
        category_data = category_sales[category_sales['pizza_category'] == category]
        plt.scatter(category_data['pizza_name'], category_data['quantity'],
                label=category, color=colors(i), alpha=0.7)  # Gebruik een doorzichtigheid voor overlappen

    plt.title('Aantal verkochte pizza’s per pizzacategorie en naam')
    plt.xlabel('Pizza naam')
    plt.ylabel('Aantal verkochte pizza’s')
    plt.xticks(rotation=45, ha='right')  # Rotatie van x-labels voor betere leesbaarheid
    plt.legend(title='Pizzacategorie')  # Toon de legenda voor categorieën
    plt.tight_layout()  # Zorg ervoor dat alles goed past


plt.figure().canvas.manager.set_window_title('Casus Positive Patatoes')  # Aanpassen titel
plt.get_current_fig_manager().window.state('zoomed')  # Automatisch gemaximaliseerd openen

sold_per_category()
plt.show()