import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data_from_db():
    conn = sqlite3.connect('pizzasales.db')
    query = 'SELECT * FROM pizza_sales'
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# 3D Visualisatie: Toon per maand per pizzanaam en per maat het totaal aantal verkochte pizza’s.


def create_scatterplot():
    df = load_data_from_db()  # Laad de data uit de database
    # Data voorbereiden
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.month

    # Groeperen op maand, pizza_name en pizza_size
    grouped_data = df.groupby(['month', 'pizza_name', 'pizza_size']).agg(total_sold=('quantity', 'sum')).reset_index()

    # Omzetten van pizza_size naar numerieke waarden
    size_mapping = {'S': 1, 'M': 2, 'L': 3}
    grouped_data['size_numeric'] = grouped_data['pizza_size'].map(size_mapping)

    # Visualisatie: 3D Scatterplot
    fig = plt.figure()
    fig.canvas.manager.set_window_title('Positive Patatoes - 3D: Scatterplot')  # Aanpassen titel van het venster
    plt.get_current_fig_manager().window.state('zoomed')  # Automatisch gemaximaliseerd openen
    ax = fig.add_subplot(projection='3d')

    # 3D scatterplot
    for pizza_name in grouped_data['pizza_name'].unique():
        subset = grouped_data[grouped_data['pizza_name'] == pizza_name]
        adjusted_sizes = subset['size_numeric'] + np.random.normal(0, 0.1, size=len(subset))
        ax.scatter(subset['month'], adjusted_sizes, subset['total_sold'], label=pizza_name, s=50)

    # Labels en aanpassingen
    ax.set_title('Verkochte Pizza\'s per Maand, Pizza Grootte en Aantal')
    ax.set_xlabel('Maand')
    ax.set_ylabel('Pizza Grootte', labelpad=8)
    ax.set_zlabel('Totaal Aantal Verkochte Pizza\'s')
    ax.set_xticks(np.arange(1, 13))
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec'])

    # Handmatige aanpassing van de y-as ticks om alleen 1, 2, 3 weer te geven
    ax.set_yticks([1, 2, 3])
    ax.set_yticklabels(['Small', 'Medium', 'Large'])

    # Legenda en tonen van plot
    plt.legend(bbox_to_anchor=(-0.6, 0.5), loc='center left')
    plt.show()
