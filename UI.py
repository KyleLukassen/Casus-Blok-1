import tkinter as tk  # Importeert de tkinter module voor het maken van de UI.
from piechart import create_piechart  # Importeert de functie voor het maken van een piechart.
from stacked_barchart import create_stacked_barchart  # Importeert de functie voor het maken van een stacked barchart.
from barchart import create_barchart  # Importeert de functie voor het maken van een barchart.
from scatterplot import create_scatterplot  # Importeert de functie voor het maken van een scatterplot.
from sqlite import check_for_data_and_import  # Controleert of de database bestaat en importeert de data.

# Controleert of de database bestaat en importeert de data.
check_for_data_and_import()


# Maakt de UI aan.
def create_ui():

    # Maakt het hoofdvenster voor de UI.
    root = tk.Tk()

    # Stelt de titel van het venster in.
    root.title('Positive Potatoes - Data Visualisatie')

    # Center de UI in het scherm.
    window_width = 400  # Breedte van de UI.
    window_height = 300  # Hoogte van de UI.
    screen_width = root.winfo_screenwidth()  # Breedte van het scherm van de gebruiker.
    screen_height = root.winfo_screenheight()  # Hoogte van het scherm van de gebruiker.
    x = (screen_width // 2) - (window_width // 2)  # Berekent de x-coördinaat voor horizontale centrering.
    y = (screen_height // 2) - (window_height // 2)  # Berekent de y-coördinaat voor verticale centrering.
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')  # Stelt de grootte en positie van het venster in.

    # Maakt de knoppen aan voor de grafieken.
    button1 = tk.Button(root, text='1D: Piechart', command=create_piechart)
    button1.pack(pady=10)

    button2 = tk.Button(root, text='2D-A: Stacked Barchart', command=create_stacked_barchart)
    button2.pack(pady=10)

    button3 = tk.Button(root, text='2D-B: Barchart', command=create_barchart)
    button3.pack(pady=10)

    button4 = tk.Button(root, text='3D: Scatterplot', command=create_scatterplot)
    button4.pack(pady=10)

    # Start de tkinter event loop voor de UI.
    root.mainloop()


# Start de UI
create_ui()
