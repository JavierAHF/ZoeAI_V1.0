import datetime
import os #para manejar archivos
import subprocess as sub #se utiliza para llamar otros programas de la programa

from tkinter import * #se utiliza para armar la interfaz y dar funcionalidades
from PIL import Image, ImageTk

import keyboard #reconocimiento de teclado
import pyttsx3 # reconocimiento de texto a voz 
import pywhatkit # reproducir videos de yt
import speech_recognition as sr #libreria para reconocimiento de voz 
import wikipedia #wikipedia :v
from pygame import mixer #libreria para interfaz grafica

import threading as tr # para hacer hilos, es como hacer mas de una actividad al mismo tiempo se ocupo en lo del alarma 

import colors # reconocimiento de colores 

import whatsapp as whapp

import browser # libreria para hacer que funcione la busqueda en el navegador pero de mejor manera

import database #para la base de datos

#librerias para que la IA pueda hablar contigo como un chatbot
from chatterbot import ChatBot
from chatterbot import preprocessors
from chatterbot.trainers import ListTrainer

#gpt sirve para la funcion de ayuda osea para que busque cosas en general
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


from customtkinter import *
from PIL import Image

# Variable para almacenar la referencia de la ventana de comandos
ventana_comandos = None


# Variable global para las ventanas
window_files = None
window_apps = None
window_pages = None
# Variable global para rastrear si la ventana está abierta  whatsapp 
window_contacts = None

#para que al presionar el boton de agregar no se habra la venatana a cada rato y habra demasiadas
is_window_files_is_open = False  # Variable global para controlar si la ventana de archivos/files ya está abierta
is_window_apps_is_open = False   # Variable global para controlar si la ventana de apps/aplicaciones ya está abierta
is_window_pages_is_open = False  # Variable global para controlar si la ventana de pages/paginas ya está abierta
is_window_contacts_is_open = False # Variable global para controlar si la ventana de contacts/contactos ya está abierta



def open_new_window():
    #ventana general de la ia
    main_window = CTk() 
    main_window.title("ZOE")

    #abrir una ventana y darle tamaño
    main_window.geometry("1200x500")
    main_window.resizable(0,0)
    set_appearance_mode("dark")
    main_window.iconbitmap("logoZ.ico")


    comandos = """
        Comandos de voz que puedes utilizar:

        -Reproduce (nombre de la canción)
        -Busca (Definición de algo)
        -Ayuda (te da información más general)
        -Alarma (hora de la alarma en formato 24:00 Hrs)
        -Colores (reconocimiento de colores rojo, verde, azul y amarillo)
        (q) para cerrar
        -Abre (di el nombre de la página web/app)
        -Archivo (nombre del archivo)
        -Escribe (di lo que quieres anotar)
        -Mensaje (espera un momento y di a quién quieres enviar el mensaje, luego la IA te escuchará)
        -Cierra (nombre del programa)
        -Cierra todo (cierra todos los programas a los que les hayas dado acceso)
        -Pausa (pausa las tareas del programa)
        -Descansa (cierra el programa)
    """
    #CONTROL F PARA BUSCAR ALGO

    #imagen ia principal
    label_title = CTkLabel(main_window, text="Asistente Virtual", text_color="#E3DAC9", font=('LEMON MILK Medium', 40))
    label_title.pack(pady=10)



    #realizacion de un canvas
    # Variable para almacenar la referencia de la ventana de comandos
    #ventana_comandos = None
    # Función para abrir una nueva ventana con los comandos de voz
    def abrir_ventana_comandos():
        global ventana_comandos
        if ventana_comandos is None or not ventana_comandos.winfo_exists():  # Verifica si la ventana no existe o se ha cerrado
            ventana_comandos = CTkToplevel()  # Crear una nueva ventana
            ventana_comandos.geometry("700x350")  # Establecer tamaño de la nueva ventana
            ventana_comandos.title("Comandos de Voz")
            ventana_comandos.resizable(0,0)
            ventana_comandos.iconbitmap("logoZ.ico")

            # Texto dentro de la nueva ventana
            label_comandos = CTkLabel(ventana_comandos, text=comandos, text_color="#FFFFFF", font=("Gareth Book", 14, "bold"), justify="left")
            label_comandos.pack(pady=20, padx=20)  # Empaquetar y centrar el texto
        else:
            ventana_comandos.lift()  # Si la ventana ya existe, la trae al frente
            ventana_comandos.iconbitmap("logoZ.ico")

    # Botón en la ventana principal para abrir la nueva ventana
    button_open_comands = CTkButton(main_window, text="Abrir Ventana de Comandos", command=abrir_ventana_comandos, font=("LEMON MILK Medium", 16), fg_color="#4F236F", hover_color="#A242A3",
                                corner_radius=32, width=250,   height=35)  #ajustar el ancho y alto
    button_open_comands.place(x=10, y=450)  # Colocar el botón en la esquina inferior izquierda





    # Cargar la imagen usando CTkImage
    imagen_ia = CTkImage(Image.open("logoT.png"), size=(250, 100))  # Ajusta el tamaño según lo que necesites

    # Mostrar la imagen en la ventana principal
    label_imagen = CTkLabel(main_window, image=imagen_ia, text="")
    label_imagen.pack(pady=5)

    # Crear la caja de texto con borde
    text_info = CTkTextbox(main_window, width=350, height=150, fg_color="#212121", border_width=4, border_color="#A242A3", text_color="#E3DAC9",  font=("Gareth Book", 14, "bold"))
    text_info.pack(pady=40)  # Ajustamos el espaciado vertical para ponerla debajo



    # #realizacion de la caja de texto
    # text_info = Text(main_window, bg="#2c3e50", fg="#FFFFFF")
    # text_info.place(x=0, y=200, height=150, width=353)

    # #poner la imagen de la GUI
    # imagen_ia = ImageTk.PhotoImage(Image.open("tomas.jpg")) 
    # window_ia = Label(main_window, image=imagen_ia)
    # window_ia.pack(pady=5)


    #voces
    def Salvadorian_voice():
        change_voice(0)

    def mexican_voice():
        change_voice(2)

    def change_voice(id):
        engine.setProperty('voice', voices[id].id)
        engine.setProperty('rate', 145)
        talk("Hola de nuevo")

    name = "zoe"
    listener = sr.Recognizer()
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 145)

    def charge_data(name_dict, name_file):
        try:
            with open(name_file) as f:
                for line in f:
                    (key, val) = line.split(",")
                    val = val.rsplit("\n")
                    name_dict[key] = val
        except FileNotFoundError as e:
            pass

    files=dict()
    charge_data(files, "archivos.txt")

    programs= dict()
    charge_data(programs, "apps.txt")
    with open('apps.txt', 'r') as file:
        for line in file:
            if ',' in line:
                name, path = line.strip().split(',', 1)
                programs[name] = path

    #print(programs)
    sites= dict()
    charge_data(sites, "pages.txt")
    contacts= dict()
    charge_data(contacts, "contacts.txt")

    #funcion de la ia para hablar
    def talk(text):
        engine.say(text)
        engine.runAndWait()

    def read_and_talk():
        text = text_info.get("1.0", "end")
        talk(text)

    def write_text(text_wiki):
        text_info.insert(INSERT, text_wiki)

    #funcion principal de escuchar


    # def listen(phrase=None):
    #     listener = sr.Recognizer()
    #     with sr.Microphone() as source:
    #         listener.adjust_for_ambient_noise(source)
    #         talk(phrase)
    #         pc = listener.listen(source)

    #     try:
    #         rec = listener.recognize_google(pc, language="es")
    #         rec = rec.lower()
    #     except sr.UnknownValueError:
    #         print("No te entendi, intenta de nuevo")   
    #     except sr.RequestError as e:
    #         print("Could not request results from Google Speech Recognition service; {0}".format(e))
    #     return rec

    def listen(phrase=None):
        listener = sr.Recognizer()    
        with sr.Microphone() as source:            
            listener.adjust_for_ambient_noise(source)
            talk(phrase)
            pc = listener.listen(source)
        try:
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
        except sr.UnknownValueError:
            print("No te entendí, intenta de nuevo")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return rec

    #funciones relacionadas a las palabras clave o comandos------------------

    def reproduce(rec):
        music = rec.replace('reproduce', '')
        print("Reproduciendo "+ music)
        talk("Reproduciendo "+ music)
        pywhatkit.playonyt(music)

    def busca(rec):
        search = rec.replace('busca','')
        wikipedia.set_lang("es")
        wiki = wikipedia.summary(search, 1)    
        talk(wiki)   
        write_text(search +": "+wiki)

    def thread_alarma(rec):
        t = tr.Thread(target=clock, args=(rec,)) #hilos sirven para que ejecuten mas de una funciona y no se pause al poner la alarma
        t.start()
        
    def colores(rec):
        talk("Enseguida")
        t = tr.Thread(target=colors.capture)
        t.start()

    def abre(rec):
        task = rec.replace('abre', '').strip()

        if task in sites:
            for site_task in sites:  # Cambiamos 'task' a 'site_task'
                if site_task in rec:
                    sub.call(f'start chrome.exe {sites[site_task]}', shell=True)
                    talk(f'Abriendo {site_task}')
        elif task in programs:
            for prog_name in programs:  # Cambiamos 'task' a 'prog_name' para evitar sobrescritura
                if prog_name in rec:
                    talk(f'Abriendo {prog_name}')       
                    os.startfile(programs[prog_name])  # Abre el programa usando la ruta correcta
        else:
            talk("Lo siento, al parecer aun no haz agregado esa app o pagina web, puedes usar los botones \
                    para agregarlas!")
    
    def archivo(rec):
        file = rec.replace('archivo', '').strip()  # Elimina la palabra 'archivo' y espacios en blanco
        if file in files:
            file_path = files[file]
            
            # Verifica si file_path es una lista, y si lo es, la convierte en una cadena
            if isinstance(file_path, list):
                file_path = ' '.join(file_path)
            
            # Abre el archivo o programa
            sub.Popen([file_path], shell=True)
            talk(f'Abriendo {file}')
        else:
            talk("Lo siento, al parecer aun no has agregado ese archivo. Puedes usar los botones para agregarlo.")

    # def archivo(rec):
    #     file = rec.replace('archivo', '').strip()
    #     if file in files:
    #         for file in files:
    #             if file in rec:
    #                 sub.Popen([files[file]], shell=True) 
    #                 talk(f'Abriendo {file}')    
    #                 #print("Abriendo")   
    #     else:
    #         talk("Lo siento, al parecer aun no haz agregado ese archivo puedes usar los botones \
    #                 para agregarlas!")  

    def escribe(rec):
        try:
            with open("nota.txt", 'a') as f:
                write(f)
        
        except FileNotFoundError as e:
            file = open("nota.txt", 'w')
            write(file)

    def enviar_mensaje(rec):
        talk("¿Un mensaje? ¿A quien quieres que envie el mensaje?")
        contact = listen("Te escucho")
        contact = contact.strip()

        if contact in contacts:
            for cont in contacts:
                if cont  == contact: 
                    contact = contacts[cont]
                    talk("¿Que mensaje deseas enviarle?")
                    message = listen("Te escucho")
                    talk("Enviando mensaje...")
                    whapp.send_message(contact, message) 

        else:
            talk("Parece que no haz agregado a ese contacto, utiliza el boton para agregar dicho contacto")    

    def cierra(rec):
        for task in programs:
            kill_task = programs[task].split('\\')
            kill_task = kill_task[-1]    
            if task in rec:
                sub.call(f'TASKKILL /IM {kill_task} /F', shell=True)
                talk(f'Cerrando {task}')  
            if 'todo' in rec:
                sub.call(f'TASKKILL /IM {kill_task} /F', shell=True)
                talk(f'Cerrando {task}')
        if 'descansa' in rec:
            talk(f'Adios')
            sub.call('TASKKILL /IM ZOE_Beta.exe /F', shell=True)

    def buscame(rec):
        something = rec.replace('ayuda', '').strip()
        talk("Buscando..." + something)
        
        # Inicializa el servicio y el navegador solo cuando sea necesario
        service = Service(executable_path='C:\\Chromedriver\\chromedriver.exe')
        browser = webdriver.Chrome(service=service)

        # Usa la instancia de webdriver
        browser.get(f'https://www.google.com/search?q={something}')

        # Espera y luego cierra el navegador
        time.sleep(5)  # Espera 5 segundos (puedes ajustar el tiempo)
        browser.quit()  # Cierra el navegador
    
    #alarma normal  
    def clock(rec):
        clock = rec.replace('alarma','')
        clock = clock.strip()
        talk("Alarma activa a las " + clock + " horas")
        print("Alarma activa a las " + clock + " horas")

        if clock[0] != '0' and len(clock) < 5:
            clock = '0' + clock
        print(clock)    

        while True:
            if datetime.datetime.now().strftime('%H:%M') == clock:
                print("TIENES ALGO PENDIENTE")
                mixer.init()
                mixer.music.load("AlarmaChampiñon.mp3")
                mixer.music.play()

            else: 
                continue
            
            if keyboard.read_key() == "p":
                mixer.music.stop()
                break   

    # hasta aqui las palabras-----------------------------------------------

    #diccionario con las palabras clave o comando que se utilizan 
    key_words = {
        'reproduce': reproduce, #rep
        'busca': busca, #buscar en la wikipedia
        'ayuda': buscame, #buscar de manera mas general
        'alarma': thread_alarma, #alarma
        'colores': colores, #colores y abre la ventana
        'abre': abre, #abre y nombre de la aplicacion
        'archivo': archivo, #archivo y el nombre de el archivo
        'escribe': escribe, #notas de bloc de notas
        'mensaje': enviar_mensaje, #mensaje de whatsapp
        'cierra': cierra, # cierra normal y dices el programa que quieres cerrar o cerrar todo y  cierras todos los programas
        'descansa': cierra, # este cierrate es con tilde y es para cerrar el programa de la ia completo
    }

    #funcion principal
    def run_zoe():
        chat = ChatBot("zoe", database_uri=None)
        trainer = ListTrainer(chat)
        trainer.train(database.get_questions_answers())
        talk("Te escucho")
        while True:
            try:
                rec = listen("")
            except UnboundLocalError:
                talk("no te entendi, puedes intentarlo de nuevo")
                continue
            if 'busca' in rec:
                key_words['busca'](rec)
                break

            elif rec.split()[0] in key_words:
                key = rec.split()[0]        
                key_words[key](rec)

            else:
                print("Tú: ", rec)
                answer = chat.get_response(rec)
                print("zoe: ", answer)
                talk(str(answer))  # Asegúrate de que sea un string
                if 'pausa' in rec:
                    break
        

            # else:
            #     print("Tú: ", rec)
            #     answer = chat.get_response(rec)
            #     print("zoe: ", answer)
            #     talk(answer)
            #     if 'pausa' in rec:
            #         break
                
        main_window.update()

    #para las notas
    def write(f):
        talk("¿Que quieres que escriba?")
        rec_write = listen("Te escucho")
        f.write( rec_write + os.linesep)
        f.close()
        talk("Listo ya puedes revisarlo")
        sub.Popen("nota.txt", shell=True)

    #las primeras 3 para agregar archivos, apps y paginas web mediante las cajas de texto
    def open_w_files():
        global is_window_files_is_open, namefile_entry, pathf_entry

        if not is_window_files_is_open:  # Solo se abre la ventana si no está abierta
            is_window_files_is_open = True  # Marca que la ventana está abierta

            window_files = CTkToplevel()  # Usa CTkToplevel para crear una ventana de nivel superior
            window_files.title("Agregar Archivos")
            set_appearance_mode("dark")  # Cambia el modo a oscuro
            window_files.geometry("550x250")  # Cambia la geometría para que sea similar
            window_files.resizable(0, 0)
            main_window.eval(f'tk::PlaceWindow {str(window_files)} center')
            window_files.attributes('-topmost', True)  # Mantener la ventana siempre en la parte superior
            window_files.iconbitmap("logoZ.ico")

            # Usa CTkLabel y CTkEntry para que respeten el modo oscuro
            title_label = CTkLabel(window_files, text="Agrega un archivo que podrás abrir con la IA", font=('LEMON MILK Medium', 16), text_color="#FFFFFF")
            title_label.pack(pady=6)

            name_label = CTkLabel(window_files, text="Ingresa el Nombre del archivo", font=('LEMON MILK Medium', 14), text_color="#FFFFFF")
            name_label.pack(pady=4)

            namefile_entry = CTkEntry(window_files, placeholder_text="Nombre del archivo", width=300, font=('LEMON MILK Medium', 12), text_color="WHITE")
            namefile_entry.pack(pady=2)

            path_label = CTkLabel(window_files, text="Ruta del archivo", font=('LEMON MILK Medium', 14), text_color="#FFFFFF")
            path_label.pack(pady=4)

            pathf_entry = CTkEntry(window_files, placeholder_text="Escribe la ruta aquí...", width=300, font=('LEMON MILK Medium', 12), text_color="WHITE")
            pathf_entry.pack(pady=2)

            save_button = CTkButton(window_files, text="Guardar", corner_radius=32, fg_color="#76358B", hover_color="#A242A3", width=200, height=30, font=('LEMON MILK Medium', 12), command=add_files)
            save_button.pack(pady=8)

            # Cuando la ventana se cierra, establece is_window_open en False
            window_files.protocol("WM_DELETE_WINDOW", lambda: on_close_window_files(window_files))

    def on_close_window_files(window):
        global is_window_files_is_open
        window.destroy()  # Cierra la ventana
        is_window_files_is_open = False  # Marca que la ventana se ha cerrado
    
        



    def open_w_apps():
        global is_window_apps_is_open, nameapps_entry, patha_entry

        if not is_window_apps_is_open:  # Solo abre la ventana si no está abierta
            is_window_apps_is_open = True  # Marca que la ventana está abierta

            window_apps = CTkToplevel()
            window_apps.title("Agregar Apps")
            set_appearance_mode("dark")  # Cambia el modo a oscuro
            window_apps.geometry("550x250")
            window_apps.resizable(0, 0)
            main_window.eval(f'tk::PlaceWindow {str(window_apps)} center')
            window_apps.attributes('-topmost', True)
            window_apps.iconbitmap("logoZ.ico")

            title_label = CTkLabel(window_apps, text="Agrega un app que podrás abrir con la IA", font=('LEMON MILK Medium', 16), text_color="#FFFFFF")
            title_label.pack(pady=6)

            name_label = CTkLabel(window_apps, text="Ingresa el Nombre de la app", font=('LEMON MILK Medium', 14), text_color="#FFFFFF")
            name_label.pack(pady=4)

            nameapps_entry = CTkEntry(window_apps, placeholder_text="Nombre de la app", width=300, font=('LEMON MILK Medium', 12), text_color="WHITE")
            nameapps_entry.pack(pady=2)

            path_label = CTkLabel(window_apps, text="Ruta de la app", font=('LEMON MILK Medium', 14), text_color="#FFFFFF")
            path_label.pack(pady=4)

            patha_entry = CTkEntry(window_apps, placeholder_text="Escribe la ruta aquí...", width=300, font=('LEMON MILK Medium', 12), text_color="WHITE")
            patha_entry.pack(pady=2)

            save_button = CTkButton(window_apps, text="Guardar", corner_radius=32, fg_color="#76358B", hover_color="#A242A3", width=200, height=30, font=('LEMON MILK Medium', 12), command=add_apps)
            save_button.pack(pady=8)

            # Cuando la ventana se cierra, restablece is_window_apps_open
            window_apps.protocol("WM_DELETE_WINDOW", lambda: on_close_apps(window_apps))

    def on_close_apps(window):
        global is_window_apps_is_open
        window.destroy()
        is_window_apps_is_open = False




    def open_w_pages():
        global is_window_pages_is_open, namepages_entry, pathp_entry

        if not is_window_pages_is_open:  # Solo abre la ventana si no está abierta
            is_window_pages_is_open = True  # Marca que la ventana está abierta

            window_pages = CTkToplevel()  # Crea la ventana como Toplevel
            window_pages.title("Agregar Paginas")
            set_appearance_mode("dark")
            window_pages.geometry("550x250")
            window_pages.resizable(0, 0)
            main_window.eval(f'tk::PlaceWindow {str(window_pages)} center')
            window_pages.attributes('-topmost', True)
            window_pages.iconbitmap("logoZ.ico")

            title_label = CTkLabel(window_pages, text="Agrega una pagina que podrás abrir con la IA", font=('LEMON MILK Medium', 16), text_color="#FFFFFF")
            title_label.pack(pady=6)

            name_label = CTkLabel(window_pages, text="Ingresa el Nombre de la pagina", font=('LEMON MILK Medium', 14), text_color="#FFFFFF")
            name_label.pack(pady=4)

            namepages_entry = CTkEntry(window_pages, placeholder_text="Nombre de la pagina", width=300, font=('LEMON MILK Medium', 12), text_color="WHITE")
            namepages_entry.pack(pady=2)

            path_label = CTkLabel(window_pages, text="Ruta de la pagina", font=('LEMON MILK Medium', 14), text_color="#FFFFFF")
            path_label.pack(pady=4)

            pathp_entry = CTkEntry(window_pages, placeholder_text="Escribe la ruta aquí...", width=300, font=('LEMON MILK Medium', 12), text_color="WHITE")
            pathp_entry.pack(pady=2)

            save_button = CTkButton(window_pages, text="Guardar", corner_radius=32, fg_color="#76358B", hover_color="#A242A3", width=200, height=30, font=('LEMON MILK Medium', 12), command=add_pages)
            save_button.pack(pady=8)

            # Cuando la ventana se cierra, restablece window_pages
            window_pages.protocol("WM_DELETE_WINDOW", lambda: on_close_pages(window_pages))

    def on_close_pages(window):
        global is_window_pages_is_open
        window.destroy()
        is_window_pages_is_open = False




    # agregar contactos de whatsapp 
     
    def open_w_contacts():
        global is_window_contacts_is_open, namecontact_entry, phone_entry

        if not is_window_contacts_is_open:  # Solo abre la ventana si no está abierta
            is_window_contacts_is_open = True  # Marca que la ventana está abierta

            contacts_window = CTkToplevel()  # Usa CTkToplevel para mantener la apariencia
            contacts_window.title("Agregar un Contacto")
            set_appearance_mode("dark")
            contacts_window.geometry("550x250")
            contacts_window.resizable(0, 0)
            main_window.eval(f'tk::PlaceWindow {str(contacts_window)} center')
            contacts_window.attributes('-topmost', True)
            contacts_window.iconbitmap("logoZ.ico")
            
            # Establece la ventana como siempre en la parte superior
            contacts_window.attributes('-topmost', True)

            title_label = CTkLabel(contacts_window, text="Agrega un contacto que podrás abrir con la IA", 
                                font=('LEMON MILK Medium', 16), text_color="#FFFFFF")
            title_label.pack(pady=6)

            name_label = CTkLabel(contacts_window, text="Ingresa el Nombre del contacto", 
                                font=('LEMON MILK Medium', 14), text_color="#FFFFFF")
            name_label.pack(pady=4)

            namecontact_entry = CTkEntry(contacts_window, placeholder_text="Escribe el nombre de tu contacto...", 
                                        width=300, font=('LEMON MILK Medium', 12), text_color="WHITE")
            namecontact_entry.pack(pady=2)

            phone_label = CTkLabel(contacts_window, text="Teléfono del contacto (con código de país)", 
                                font=('LEMON MILK Medium', 14), text_color="#FFFFFF")
            phone_label.pack(pady=4)

            phone_entry = CTkEntry(contacts_window, placeholder_text="Escribe el número de tu contacto...", 
                                    width=300, font=('LEMON MILK Medium', 12), text_color="WHITE")
            phone_entry.pack(pady=2)

            save_button = CTkButton(contacts_window, text="Guardar", corner_radius=32, 
                                    fg_color="#76358B", hover_color="#A242A3", 
                                    width=200, height=30, font=('LEMON MILK Medium', 12), 
                                    command=add_contacts)
            save_button.pack(pady=8)
            # Cuando la ventana se cierra, restablece window_pages
            contacts_window.protocol("WM_DELETE_WINDOW", lambda: on_close_contacts(contacts_window))

    def on_close_contacts(window):
        global is_window_contacts_is_open
        window.destroy()
        is_window_contacts_is_open = False       


    #guardar archivos en un txt dependiendo el tipo archivo o ruta
    def add_files():
        name_file = namefile_entry.get().strip()
        path_file = pathf_entry.get().strip()

        files[name_file] = path_file

        save_data(name_file, path_file, "archivos.txt")

        namefile_entry.delete(0, "end")
        pathf_entry.delete(0, "end")

    def add_apps():
        name_file = nameapps_entry.get().strip()
        path_file = patha_entry.get().strip()

        programs[name_file] = path_file

        save_data(name_file, path_file, "apps.txt")

        nameapps_entry.delete(0, "end")
        patha_entry.delete(0, "end")
        
    def add_pages():
        name_page = namepages_entry.get().strip()
        url_pages = pathp_entry.get().strip()

        sites[name_page] = url_pages

        save_data(name_page, url_pages, "pages.txt")

        namepages_entry.delete(0, "end")
        pathp_entry.delete(0, "end")

    #contactos de whatsapp en un txt 
    def add_contacts():
        name_contact = namecontact_entry.get().strip()
        phone = phone_entry.get().strip()

        contacts[name_contact] = phone
        save_data(name_contact, phone, "contacts.txt")
        namecontact_entry.delete(0, "end")
        phone_entry.delete(0, "end")

    #guardar datos 
    def save_data(key, value, file_name):
        try:
            with open(file_name, 'a') as f:
                f.write(key + "," + value + "\n")
        except FileNotFoundError:
            file = open(file_name, 'a')
            file.write(key + "," + value + "\n")

    #decir las paginas,apps,archivos y contactos que estan ya agregados en el txt
    def talk_pages():
        if bool(sites) == True:
            talk("Haz agregado las siguientes paginas web")
            for site in sites:
                talk(site)
        else:
            talk("Aun no haz agregado ninguna pagina web")

    def talk_apps():
        if bool(programs) == True:
            talk("Haz agregado las siguientes apps")
            for app in programs:
                talk(app)
        else:
            talk("Aun no haz agregado ninguna app")

    def talk_files():
        if bool(files) == True:
            talk("Haz agregado los siguientes archivos")
            for file in files:
                talk(file)
        else:
            talk("Aun no haz agregado ningun archivo")

    #contactos de whatsapp
    def talk_contacts():
        if bool(contacts) == True:
            talk("Haz agregado los siguientes contactos")

            for cont in contacts:
                talk(cont)
        else:
            talk("Aun no haz agregado ningun contacto")        

    #para obtener el nombre de el usuario
    def give_me_name():
        talk("Hola ¿como te llamas?")
        name = listen()
        name = name.strip()
        talk(f"Bienvenido {name}")

        try:
            with open("name.txt", 'w') as f:
                f.write(name)
        except FileNotFoundError: 
            file = open("name.txt", 'w')       
            file.write(name)

    #simplemente una funcion para que hable y diga hola
    def say_hello():     
        if os.path.exists("name.txt"):
            with open("name.txt") as f:
                for name in f:
                    talk(f"Hola, bienvenido {name}")
        else:
            give_me_name()   

    def thread_hello():
        t = tr.Thread(target=say_hello)
        t.start()

    thread_hello()    

    #Funciones para la creacion de botones

    # Botón para escuchar
    button_listen = CTkButton(main_window, text="ESCUCHAR", corner_radius=32, fg_color="#4F236F", hover_color="#A242A3",
                                font=('LEMON MILK Medium', 18), width=150, height=35, command=run_zoe)
    button_listen.place(x=425, y=420)  # Colocar el botón ESCUCHAR debajo de la caja de texto

    # Botón de hablar de la IA
    button_speak = CTkButton(main_window, text="HABLAR", corner_radius=32, fg_color="#4F236F", hover_color="#A242A3",
                                font=('LEMON MILK Medium', 18), width=150,   height=35, command=read_and_talk)
    button_speak.place(x=625, y=420)  # Colocar el botón HABLAR a la derecha del botón ESCUCHAR




    # Crear un marco para los botones de cambiar voz con tamaño definido
    frame_voice_change = CTkFrame(main_window, fg_color="#212121", width=400, height=100)  # Especificar ancho y alto aquí
    frame_voice_change.place(x=50, y=50)  # Ajustar la posición del marco

    # Etiqueta del título
    label_voice_change = CTkLabel(frame_voice_change, text="Cambiar de voz", font=("LEMON MILK Medium", 20), text_color="#E3DAC9")
    label_voice_change.pack(pady=6)  # Espacio superior dentro del marco

    # Botones para cambiar la voz
    # Cambiar voz español sv
    button_voice_es = CTkButton(frame_voice_change, text="CAMBIAR DE VOZ (SV)", corner_radius=32, fg_color="#4F236F", hover_color="#A242A3",
                                    font=('LEMON MILK Medium', 13), command=Salvadorian_voice)
    button_voice_es.pack(pady=6, padx=10)  # Añadir el botón al marco

    # Cambiar voz inglés USA
    button_voice_us = CTkButton(frame_voice_change, text="CAMBIAR DE VOZ (MX)", corner_radius=32, fg_color="#4F236F", hover_color="#A242A3",
                                    font=('LEMON MILK Medium', 13), command=mexican_voice)
    button_voice_us.pack(pady=6, padx=10)  # Añadir el botón al marco






    # Crear un marco para los botones de agregar archivos, apps y páginas con tamaño definido
    frame_add_options = CTkFrame(main_window, fg_color="#212121")  # Especificar ancho y alto aquí
    frame_add_options.place(x=50, y=225)  # Colocarlo debajo del marco de cambiar de voz

    # Etiqueta del título para "Dar Acceso"
    label_access = CTkLabel(frame_add_options, text="Dar Acceso", font=("LEMON MILK Medium", 20), text_color="#E3DAC9")
    label_access.pack(pady=6)  # Espacio superior dentro del marco

    # Botón de agregar archivos
    button_add_files = CTkButton(frame_add_options, text="Agregar Archivos", corner_radius=32, fg_color="#4F236F", hover_color="#A242A3",
                                font=('LEMON MILK Medium', 13), width=190, height=28, command=open_w_files)
    button_add_files.pack(pady=6, padx=10)  # Añadir el botón al marco con espacio

    # Botón de agregar apps
    button_add_apps = CTkButton(frame_add_options, text="Agregar Apps", corner_radius=32, fg_color="#4F236F", hover_color="#A242A3",
                                font=('LEMON MILK Medium', 13), width=190, height=28, command=open_w_apps)
    button_add_apps.pack(pady=6, padx=10)  # Añadir el botón al marco con espacio

    # Botón de agregar páginas de internet
    button_add_pages = CTkButton(frame_add_options, text="Agregar Páginas", corner_radius=32, fg_color="#4F236F", hover_color="#A242A3",
                                font=('LEMON MILK Medium', 13), width=190, height=28, command=open_w_pages)
    button_add_pages.pack(pady=6, padx=10)  # Añadir el botón al marco con espacio





    # Crear un marco para los botones de WhatsApp con tamaño definido
    frame_whatsapp_options = CTkFrame(main_window, fg_color="#212121")
    frame_whatsapp_options.place(x=850, y=50)  # Especificar ancho y alto aquí

    # Etiqueta del título para los botones de WhatsApp
    label_whatsapp = CTkLabel(frame_whatsapp_options, text="WhatsApp", font=("LEMON MILK Medium", 20), text_color="#E3DAC9")
    label_whatsapp.pack(pady=6)  # Espacio superior dentro del marco

    # Botón de agregar contactos
    button_add_contacts = CTkButton(frame_whatsapp_options, text="Agregar contactos", corner_radius=32, fg_color="#4F236F", hover_color="#A242A3",
                                    font=('LEMON MILK Medium', 13), width=190, height=28, command=open_w_contacts)
    button_add_contacts.pack(pady=6, padx=20)  # Añadir el botón al marco con espacio

    # Botón de contactos agregados
    button_tell_contacts = CTkButton(frame_whatsapp_options, text="Contactos agregados", corner_radius=32, fg_color="#4F236F", hover_color="#A242A3",
                                    font=('LEMON MILK Medium', 13), width=190, height=28, command=talk_contacts)
    button_tell_contacts.pack(pady=6, padx=10)  # Añadir el botón al marco con espacio





    # Crear un marco para los botones de WhatsApp con tamaño definido
    frame_tell_adds = CTkFrame(main_window, fg_color="#212121")
    frame_tell_adds.place(x=850, y=225)  # Especificar ancho y alto aquí

    # Etiqueta del título para los botones de WhatsApp
    label_adds = CTkLabel(frame_tell_adds, text="Accesos concedidos", font=("LEMON MILK Medium", 20), text_color="#E3DAC9")
    label_adds.pack(pady=6, padx=10)  # Espacio superior dentro del marco

    #boton de decir cuales paginas estan agregadas   
    button_tell_pages= CTkButton(frame_tell_adds, text="Paginas agregadas", corner_radius=32, fg_color="#4F236F", hover_color="#A242A3",
                            text_color="#E3DAC9",font=('LEMON MILK Medium', 13), width=190, height=28, command=talk_pages)
    button_tell_pages.pack(pady=6, padx=10)  # Añadir el botón al marco con espacio


    #boton de decir cuales apps estan agregadas   
    button_tell_apps= CTkButton(frame_tell_adds, text="Apps agregadas", corner_radius=32, fg_color="#4F236F", hover_color="#A242A3",
                             text_color="#E3DAC9",font=('LEMON MILK Medium', 13), width=190, height=28, command=talk_apps)
    button_tell_apps.pack(pady=6, padx=10)  # Añadir el botón al marco con espacio


    #boton de decir cuales archivos estan agregados   
    button_tell_files= CTkButton(frame_tell_adds, text="Archivos agregados", corner_radius=32, fg_color="#4F236F", hover_color="#A242A3",
                             text_color="#E3DAC9",font=('LEMON MILK Medium', 13), width=190, height=28, command=talk_files)
    button_tell_files.pack(pady=6, padx=10)  # Añadir el botón al marco con espacio




    main_window.mainloop()

#open_new_window()