import tkinter as tk
from piechart import create_piechart  # Importeert de piechart functie
from stacked_barchart import create_stacked_barchart  # Importeert de barchart functie
from barchart import create_barchart  # Importeert de scatterplot functie
from scatterplot import create_scatterplot  # Importeert de scatterplot functie
from sqlite import load_data_from_db  # Maakt aan of laad de database.
from PIL import Image, ImageTk

# Hoofdfunctie voor de UI
load_data_from_db()


def create_ui():
    root = tk.Tk()
    root.title('Positive Potatoes - Data Visualisatie')

    icon = Image.open('run-regular-24.png')
    photo = ImageTk.PhotoImage(icon)
    root.wm_iconphoto(False, photo)

    # Center de UI in het scherm
    window_width = 400
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    # Knoppen voor het genereren van de grafieken
    button1 = tk.Button(root, text='1D: Piechart', command=create_piechart)  # Verwijder haakjes
    button1.pack(pady=10)

    button2 = tk.Button(root, text='2D-A: Stacked Barchart', command=create_stacked_barchart)  # Verwijder haakjes
    button2.pack(pady=10)

    # Extra knoppen die later kunnen worden aangepast
    button3 = tk.Button(root, text='2D-B: Barchart', command=create_barchart)
    button3.pack(pady=10)

    button4 = tk.Button(root, text='3D: Scatterplot', command=create_scatterplot)
    button4.pack(pady=10)

    root.mainloop()


# Start de UI
create_ui()
