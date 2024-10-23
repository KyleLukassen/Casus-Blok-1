import pandas as pd
import matplotlib.pyplot as plt

# Dataset aanmaken
data = pd.read_excel("PizzaSales.xlsx")

# DataFrame aanmaken
df = pd.DataFrame(data)

# Het DataFrame bekijken
# print(df)

# Pizza categorieen groeperen + aantal keer verkocht
pizza_category = df.groupby('pizza_category')['order_details_id'].count()

# Verkopen per categorie in procenten
sales_percentage = (pizza_category / pizza_category.sum()) * 100


# Piechart maken voor "1D Visualisatie: Visualiseer per pizzacategorie het percentage verkochte pizza’s."

# Kind = type grafiek, 
# Autopct = Automatic Percentage > 1.1 betekent 1 cijfer achter de komma, 1.0 staat voor géén cijfer achter de komma,
# Startangle = de hoek waarop de piechart begint,
sales_percentage.plot(kind='pie', autopct='%1.0f%%', startangle=90, colors=['skyblue', 'lightgreen', 'coral', 'lightpink'])

# Y-as verwijderen
plt.ylabel('')

# Titel van de diagram
plt.title('Percentage verkochte pizza’s per categorie:')

# Zorgt ervoor dat de piechart rond is i.p.v. ovaal
plt.axis('equal')

# Laat de piechart zien
plt.show()