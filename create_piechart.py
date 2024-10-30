import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("PizzaSales.xlsx")  # Dataset aanmaken
df = pd.DataFrame(data)  # DataFrame aanmaken

# 1D Visualisatie: Visualiseer per pizzacategorie het percentage verkochte pizza’s.


def create_piechart():
    # plt.subplot(2, 2, 1)
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


plt.figure().canvas.manager.set_window_title('Casus Positive Patatoes')  # Aanpassen titel
plt.get_current_fig_manager().window.state('zoomed')  # Automatisch gemaximaliseerd openen

create_piechart()
plt.show()