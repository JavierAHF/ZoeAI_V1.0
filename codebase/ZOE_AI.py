import tkinter as tk  # Importar tkinter
import customtkinter as ctk
from PIL import Image, ImageTk
import os

# Variables globales para controlar las ventanas de información
info_window = None  # Ventana de más información
info_window1 = None  # Ventana de información 1
info_window2 = None  # Ventana de información 2
info_window3 = None  # Ventana de información 3
info_window_height = 200  # Altura de las ventanas de información
info_window_offset = 50  # Desplazamiento vertical entre ventanas

def zoe_window_funcionalidades():
    start_window.destroy()  # Cierra la ventana actual
    import zoe_gui_func  # Asegúrate de que este archivo esté en el mismo directorio
    zoe_gui_func.open_new_window()  # Llama a la función que abre la nueva ventana

def show_info1():
    global info_window1  # Usar la variable global para controlar la ventana 1

    if info_window1 is None or not info_window1.winfo_exists():
        info_window1 = ctk.CTkToplevel(start_window)
        info_window1.resizable(0,0)
        info_window1.title("Duo de Creadores ZOE")
        info_window1.geometry(f"300x{info_window_height}")  # Configurar la altura
        
        label = ctk.CTkLabel(info_window1, text="""Fabricio Daniel Vanegas Avilés.
    Javier Alexander Hernández Flamenco.
        ^^""", font=("Gareth Book", 14, "bold"))
        label.pack(pady=20)
        # Colocar la ventana en la parte superior derecha
        x_pos = start_window.winfo_screenwidth() - 300  # Coordenada X para la esquina derecha
        y_pos = info_window_offset  # Coordenada Y inicial
        info_window1.geometry(f"+{x_pos}+{y_pos}")
    else:
        info_window1.lift()  # Llevar al frente si ya existe
        info_window1.iconbitmap("logoZ.ico")
        

def show_info2():
    global info_window2  # Usar la variable global para controlar la ventana 2

    if info_window2 is None or not info_window2.winfo_exists():
        info_window2 = ctk.CTkToplevel(start_window)
        info_window2.resizable(0,0)
        info_window2.title("Actualizaciones ZOE")
        info_window2.geometry(f"430x{info_window_height}")  # Configurar la altura
        label = ctk.CTkLabel(info_window2, text="""Se integro una nueva funcionalidad dentro de el asistente:
Ahora puedes mantener una conversación simple con ZOE 
    mediante el entrenamiento de la IA :3""", font=("Gareth Book", 14, "bold"))
        label.pack(pady=20)
        # Colocar la ventana en la parte superior derecha, debajo de la anterior
        x_pos = start_window.winfo_screenwidth() - 300  # Coordenada X para la esquina derecha
        y_pos = info_window_offset + info_window_height  # Coordenada Y para la siguiente ventana
        info_window2.geometry(f"+{x_pos}+{y_pos}")
    else:
        info_window2.lift()  # Llevar al frente si ya existe
        info_window2.iconbitmap("logoZ.ico")

def show_info3():
    global info_window3  # Usar la variable global para controlar la ventana 3

    if info_window3 is None or not info_window3.winfo_exists():
        info_window3 = ctk.CTkToplevel(start_window)
        info_window3.resizable(0,0)
        info_window3.title("Información 3")
        info_window3.geometry(f"450{info_window_height}")  # Configurar la altura
        label = ctk.CTkLabel(info_window3, text="""¡Importante!
    Presiona Iniciar, esta ventana te llevara a otra en donde
    se encuentra la interfaz de el asistente, dale los accesos
a tus contactos, aplicaciones, etc... mediante los botones y luego
    presiona ESCUCHAR y empieza a interactuar :)""", font=("Gareth Book", 14, "bold"))
        label.pack(pady=20)
        # Colocar la ventana en la parte superior derecha, debajo de la anterior
        x_pos = start_window.winfo_screenwidth() - 300  # Coordenada X para la esquina derecha
        y_pos = info_window_offset + (2 * info_window_height)  # Coordenada Y para la siguiente ventana
        info_window3.geometry(f"+{x_pos}+{y_pos}")
    else:
        info_window3.lift()  # Llevar al frente si ya existe
        info_window3.iconbitmap("logoZ.ico")

def open_info_window():
    global info_window  # Usar la variable global para controlar la ventana

    if info_window is None or not info_window.winfo_exists():
        # Crear una nueva ventana para más información
        info_window = ctk.CTkToplevel(start_window)
        info_window.resizable(0,0)
        info_window.title("Más Información")
        info_window.geometry("300x200")  # Configurar tamaño
        info_window.lift()  # Asegurarse de que esté en frente
        info_window.transient(start_window)  # Mantenerla como una ventana secundaria
        info_window.iconbitmap("logoZ.ico")

        # Crear botones en la nueva ventana
        btn_info1 = ctk.CTkButton(info_window, text="Creadores", fg_color="#4F236F", hover_color="#A242A3", font=("LEMON MILK Medium", 18), text_color="#E3DAC9", command=show_info1)
        btn_info1.pack(pady=10)

        btn_info2 = ctk.CTkButton(info_window, text="Actualizaciones", fg_color="#4F236F", hover_color="#A242A3", font=("LEMON MILK Medium", 18), text_color="#E3DAC9", command=show_info2)
        btn_info2.pack(pady=10)

        btn_info3 = ctk.CTkButton(info_window, text="¿Como utilizarlo?", fg_color="#4F236F", hover_color="#A242A3", font=("LEMON MILK Medium", 18), text_color="#E3DAC9", command=show_info3)
        btn_info3.pack(pady=10)
    else:
        info_window.lift()  # Si ya existe, llevarla al frente
        info_window.iconbitmap("logoZ.ico")

# Crear la ventana principal
ctk.set_appearance_mode("dark")  # Modo de apariencia del sistema

# Crear la ventana
start_window = ctk.CTk()    
start_window.title("Ventana Principal")
start_window.resizable(0,0)
start_window.geometry("800x500")  # Cambiar el tamaño a 700x500
start_window.iconbitmap("logoZ.ico")

# Centrar la ventana en la pantalla
screen_width = start_window.winfo_screenwidth()  # Ancho de la pantalla
screen_height = start_window.winfo_screenheight()  # Alto de la pantalla
x_coordinate = int((screen_width / 2) - (800 / 2))  # Calcular coordenada X
y_coordinate = int((screen_height / 2) - (500 / 2))  # Calcular coordenada Y
start_window.geometry(f"+{x_coordinate}+{y_coordinate}")  # Posicionar la ventana en el centro

# Crear un Frame para el borde
border_frame = ctk.CTkFrame(start_window, width=710, height=510, corner_radius=10, fg_color="purple")  # Frame morado
border_frame.pack(padx=5, pady=5)  # Añadir un poco de espacio alrededor del marco

# Crear un canvas para manejar el fondo y el logo
canvas = ctk.CTkCanvas(border_frame, width=800, height=500, bg="black")  # Fondo negro
canvas.pack(fill="both", expand=True)

# Verificar si la imagen de fondo existe
if not os.path.exists("imagenfondoG.jpg"):
    print("Error: La imagen de fondo 'imagenfondoG.jpg' no se encuentra.")
else:
    # Cargar y configurar la imagen de fondo
    background_image = Image.open("imagenfondoG.jpg")
    background_image = background_image.resize((800, 500), Image.LANCZOS)  # Ajustar al tamaño de la ventana
    background_image_tk = ImageTk.PhotoImage(background_image)

    # Dibujar la imagen de fondo en el canvas
    canvas.create_image(0, 0, anchor="nw", image=background_image_tk)

# Verificar si la imagen del logo existe
if not os.path.exists("logoT.png"):
    print("Error: La imagen del logo 'nuevLogo.png' no se encuentra.")
else:
    # Cargar la imagen del logo
    logo_image = Image.open("logoT.png")  # Asegúrate de que la ruta sea correcta
    logo_image = logo_image.resize((250, 100), Image.LANCZOS)  # Cambiar el tamaño del logo a 100x100
    logo_image_tk = ImageTk.PhotoImage(logo_image)

    # Dibujar la imagen del logo en el canvas (ajustando la posición hacia arriba)
    canvas.create_image(400, 180, anchor="center", image=logo_image_tk)  # Colocar el logo más arriba

# Añadir texto "ZOE IA" entre el logo y el botón
canvas.create_text(400, 280, text="Asistente Virtual", fill="#E3DAC9",  font=("LEMON MILK Medium", 40, "bold"), anchor="center")  # Colocar el texto en el canvas

# Crear el botón para abrir pruebasinterfaz
btn_start_window = ctk.CTkButton(master=start_window, text="INICIAR", corner_radius=32, width=150, height=30, font=("LEMON MILK Medium", 18), command=zoe_window_funcionalidades, fg_color="#4F236F", hover_color="#A242A3", text_color="#E3DAC9")
btn_start_window.place(relx=0.5, rely=0.7, anchor="center")  # Colocar el botón en el centro inferior

# Crear el botón en la parte inferior derecha para más información
btn_more_info = ctk.CTkButton(master=start_window, text="MAS INFORMACION", corner_radius=32, width=250, height=30, font=("LEMON MILK Medium", 18), command=open_info_window, fg_color="#4F236F", hover_color="#A242A3", text_color="#E3DAC9")
btn_more_info.place(relx=0.5, rely=0.8, anchor="center")  # Colocar el botón en la parte inferior derecha

# Iniciar el bucle principal de la ventana
start_window.mainloop()




















