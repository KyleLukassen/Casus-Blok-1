import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("PizzaSales.xlsx")  # Dataset aanmaken
df = pd.DataFrame(data)  # DataFrame aanmaken

""""-----------------------------------------BELANGRIJK-----------------------------------------------"""

"""De opdracht stelt het volgende: Visualiseer welke pizzanaam en in welke maat het meest is verkocht in 2015
Inprincipe is dit precies wat de opdracht vraagt ik zou niet weten hoe ik dit anders moet interpeteren"""


def test():
    year = 2015
    df['order_date'] = pd.to_datetime(df['order_date'])  # Zorg ervoor dat de order_date kolom het juiste datatype heeft
    df_2015 = df[df['order_date'].dt.year == year]  # Filter voor het jaar 2015

# Groepeer per pizzanaam en pizzamaat, tel de verkochte aantallen
    sales_data = df_2015.groupby(['pizza_name', 'pizza_size'])['quantity'].sum().reset_index()

# Bepaal de bestverkopende pizza
    best_selling = sales_data.loc[sales_data['quantity'].idxmax()]

# 3. Data visualisatie
    plt.bar(best_selling['pizza_name'] + " (" + best_selling['pizza_size'] + ")", best_selling['quantity'], color='lightblue')
    plt.title('Best verkochte pizza in 2015')
    plt.xlabel('Pizza naam (maat)')
    plt.ylabel('Aantal verkochte pizza’s')
    plt.ylim(0, best_selling['quantity'] + 5)  # Geef wat ruimte boven de bar


plt.figure().canvas.manager.set_window_title('Casus Positive Patatoes')  # Aanpassen titel
plt.get_current_fig_manager().window.state('zoomed')  # Automatisch gemaximaliseerd openen

test()
plt.show()