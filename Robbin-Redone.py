import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("PizzaSales.xlsx")  # Dataset aanmaken
df = pd.DataFrame(data)  # DataFrame aanmaken

# 1D Visualisatie: Visualiseer per pizzacategorie het percentage verkochte pizza’s.


def create_piechart():
    plt.subplot(2, 2, 1)
    percentage = 100
    pizza_category = df.groupby('pizza_category')['order_details_id'].count()
    sales_percentage = (pizza_category / pizza_category.sum()) * percentage

    sales_percentage.plot(kind='pie',  # Type grafiek
                         autopct='%1.0f%%',  # Automatisch percentage > 1.1 betekend 1 cijfer achter komma, 1.0 geen.
                         startangle=90,  # De hoek waaruit de piechart begint
                         colors=['skyblue', 'lightgreen', 'coral', 'lightpink'])

    plt.ylabel('')  # Verwijderen/toevoegen van label Y-as
    plt.title('Percentage verkochte pizza’s per categorie:')  # Titel van het diagram
    plt.axis('equal')  # Zorgt ervoor dat de piechart rond is i.p.v. ovaal


# 2D Visualisatie: Visualiseer welke pizzanaam en in welke maat het meest is verkocht in 2015.

def create_barchart():
    plt.subplot(2, 2, 2)  # Zet de grafiek in de 4e positie van een 2x2 grid
    year = 2015
    shown_pizzas = 10

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


# 2D Visualisatie: Visualiseer per pizzacategorie de pizzanamen en toon het verkochte aantal.


def drie_d_visualisatie():
    plt.subplot(2, 2, 3)
    category_sales = df.groupby('pizza_category')['quantity'].sum().reset_index()  # Groepeer per categorie en tel verkochte aantallen

    plt.bar(category_sales['pizza_category'], category_sales['quantity'], color='lightgreen')  # Maak een staafdiagram
    plt.title('Aantal verkochte pizza’s per pizzacategorie')
    plt.xlabel('')
    plt.ylabel('Aantal verkochte pizza’s')
    plt.xticks(rotation=25, ha='right')  # Rotatie van x-labels voor betere leesbaarheid

def sold_per_category():
    plt.subplot(2, 2, 4)

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

create_piechart()
create_barchart()
drie_d_visualisatie()
sold_per_category()
# plt.tight_layout()
plt.show()