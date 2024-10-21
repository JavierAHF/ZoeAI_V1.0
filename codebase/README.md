pyinstaller.exe: Llama a la herramienta PyInstaller.
--onefile: Indica que se desea empaquetar todo el programa en un único archivo ejecutable. Esto evita que se creen múltiples carpetas con archivos auxiliares.
--icon=juanita_photo.ico: Especifica el archivo de icono (.ico) que se usará para el ejecutable. En este caso, se está utilizando un archivo llamado juanita_photo.ico.
juanita_guiyt.py: Este es el nombre del script de Python que se está convirtiendo en ejecutable. Es probable que este script sea la interfaz gráfica del proyecto en cuestión.
En resumen, este comando genera un archivo ejecutable a partir del script juanita_guiyt.py, empaquetado en un solo archivo y con un icono personalizado.

pyinstaller.exe --onefile --icon=juanita_photo.ico script_principal.py


-------------------------------------------------------------------
pyinstaller.exe --onefile --icon=logoZ.ico first_window.py 
--esto lo cambie

este era para comprimirlo mas fácilmente pero se habría la terminal al principio

--entonces usamos este :D
pyinstaller.exe --noconsole --icon=logoZ.ico first_window.py 




-----------------------------------------------------------
BROWSER.PY

from selenium import webdriver: Importa el módulo webdriver, que es el corazón de Selenium. Permite controlar el navegador.
from selenium.webdriver.common.keys import Keys: Importa el objeto Keys, que contiene los códigos de las teclas que se pueden simular en el navegador, como ENTER.

def search(something):: Define una función llamada search que toma un argumento something. Este argumento es la cadena de búsqueda que se desea ingresar en Google.

browser = webdriver.Chrome(...): Crea una instancia del navegador Chrome. Se especifica la ruta al ejecutable de ChromeDriver, que es un controlador necesario para que Selenium interactúe con el navegador. En este caso, se está utilizando C:\\Chromedriver\\chromedriver.exe como la ruta del ejecutable.

browser.maximize_window(): Maximiza la ventana del navegador, asegurando que todos los elementos sean visibles y que la visualización sea óptima.

browser.get('https://www.google.com/'): Indica al navegador que navegue a la URL especificada, que en este caso es la página principal de Google.


findElem = browser.find_element_by_name('q'): Utiliza el método find_element_by_name para localizar el campo de búsqueda de Google. En Google, el campo de búsqueda tiene el atributo name con el valor 'q'. Este método devuelve un objeto que representa el campo de texto. si le Damos inspeccionar y vemos el campo de búsqueda de google se define con la letra q

findElem.send_keys(something): Utiliza el método send_keys para enviar la cadena de búsqueda (el argumento something) al campo de búsqueda que se ha localizado.

findElem.send_keys(Keys.RETURN): Simula la presión de la tecla ENTER para enviar el formulario de búsqueda, lo que resulta en que se realice la búsqueda de la cadena que se ingresó.


pip show selenium
version tiene que ser compatible con python 3.8.6:
Name: selenium
Version: 4.25.0
Summary: Official Python bindings for Selenium WebDriver
Home-page: https://www.selenium.dev
Author: None
Author-email: None
License: Apache 2.0
Location: c:\users\mineducyt\appdata\local\programs\python\python38\lib\site-packages
Requires: trio, typing-extensions, certifi, websocket-client, trio-websocket, urllib3
Required-by: 

----------------------------------------------------------------------------------------------------------------------------------------------

COLORS.PY

import cv2: Importa la biblioteca OpenCV, que es una herramienta popular para la visión por computadora.
import numpy as np: Importa NumPy, que se utiliza aquí para trabajar con arreglos y matrices, especialmente en la manipulación de imágenes.



def draw(mask, color, frame_c):: Define una función llamada draw que toma tres argumentos:
mask: La máscara de color detectado.
color: El color para dibujar los contornos.
frame_c: El marco actual del video donde se dibujarán los contornos.
contours, _ = cv2.findContours(...): Encuentra los contornos en la máscara. cv2.RETR_EXTERNAL se usa para obtener solo los contornos externos, y cv2.CHAIN_APPROX_SIMPLE comprime los contornos eliminando puntos redundantes.



for c in contours:: Itera sobre cada contorno encontrado.
area = cv2.contourArea(c): Calcula el área del contorno.
if area > 1000:: Filtra los contornos, procesando solo aquellos que tienen un área mayor a 1000 píxeles.
new_contour = cv2.convexHull(c): Calcula el envolvente convexo del contorno.
cv2.drawContours(...): Dibuja el contorno en frame_c con el color especificado y un grosor de 3.


M = cv2.moments(c): Calcula los momentos del contorno c, que se utilizan para encontrar el centro del contorno.
if(M["m00"]==0): M['m00']=1: Evita la división por cero al verificar si M["m00"] es cero.
x=int(M['m10']/M['m00']) y y=int(M['m01']/M['m00']): Calcula las coordenadas del centro del contorno.


font = cv2.FONT_HERSHEY_COMPLEX: Define el tipo de letra para el texto que se dibuja.
cv2.putText(...): Dibuja el texto en el marco en la posición (x+10, y) con un tamaño de fuente de 0.75, el color correspondiente y un grosor de 1.


def capture():: Define la función capture, que se encargará de capturar el video desde la cámara.
cap = cv2.VideoCapture(0): Abre la cámara (0 generalmente corresponde a la cámara predeterminada).


Se definen los rangos de color en el espacio de color HSV (Hue, Saturation, Value) para los colores que se desean detectar (amarillo, azul, verde, rojo).
Bucle Principal


while True:: Inicia un bucle infinito que continuará hasta que se presione 'q'.
comp, frame = cap.read(): Captura un frame de la cámara. comp indica si la captura fue exitosa.
frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV): Convierte el frame de BGR a HSV para facilitar la detección de colores.
cv2.imshow('Webcam', frame): Muestra el frame capturado en una ventana llamada 'Webcam'.


cap.release(): Libera la cámara al finalizar.
cv2.destroyAllWindows(): Cierra todas las ventanas de OpenCV abiertas.


pip show opencv-python
Name: opencv-python
Version: 4.10.0.84
Summary: Wrapper package for OpenCV python bindings.
Home-page: https://github.com/opencv/opencv-python
Author: None
Author-email: None
License: Apache 2.0
Location: c:\users\mineducyt\appdata\local\programs\python\python38\lib\site-packages
Requires: numpy, numpy
Required-by: 


pip show numpy
Name: numpy
Version: 1.24.4
Summary: Fundamental package for array computing in Python
Home-page: https://www.numpy.org
Author: Travis E. Oliphant et al.
Author-email: None
License: BSD-3-Clause
Location: c:\users\mineducyt\appdata\local\programs\python\python38\lib\site-packages
Requires:
Required-by: opencv-python

----------------------------------------------------------------------------------------------------------------------------------------------

DATABASE.PY

import sqlite3: Importa el módulo sqlite3, que permite interactuar con bases de datos SQLite.


def create_connection():: Define una función llamada create_connection que no recibe argumentos.
connection = sqlite3.connect("brain.db"): Crea una conexión a la base de datos brain.db. Si el archivo de la base de datos no existe, SQLite lo creará automáticamente.
return connection: Devuelve la conexión establecida a la base de datos.



def get_table():: Define una función llamada get_table que no recibe argumentos.
connection = create_connection(): Llama a create_connection para establecer una conexión a la base de datos.
cursor = connection.cursor(): Crea un cursor a partir de la conexión. El cursor se utiliza para ejecutar comandos SQL en la base de datos.
cursor.execute("SELECT * FROM question_answers"): Ejecuta una consulta SQL para seleccionar todas las filas de la tabla question_answers.
return cursor.fetchall(): Recupera todas las filas resultantes de la consulta y las devuelve como una lista de tuplas.

bot_list = list(): Inicializa una lista vacía llamada bot_list. Esta lista se utilizará para almacenar las preguntas y respuestas recuperadas de la base de datos.


def get_questions_answers():: Define una función llamada get_questions_answers que no recibe argumentos.
rows = get_table(): Llama a get_table para recuperar todas las filas de la tabla question_answers y las almacena en rows.
for row in rows:: Itera sobre cada fila en rows.
bot_list.extend(list(row)): Convierte la fila (que es una tupla) en una lista y la extiende a bot_list, añadiendo todos los elementos de la fila a bot_list.
return bot_list: Devuelve la lista bot_list, que ahora contiene todas las preguntas y respuestas de la tabla.

version de sqlite3 ya instalada con la version de python para conexiones de base de datos
python --version
Python 3.8.6.


El archivo "brain.db" es la base de datos que utilizamos para nuestro proyecto.

---------------------------------------------------------------------

Whatsapp.py

import webbrowser
Esta línea importa la biblioteca estándar webbrowser, que permite abrir URLs en el navegador predeterminado del sistema.


import pyautogui as at
Aquí se importa la biblioteca pyautogui y se le asigna un alias (at). Esta biblioteca permite automatizar movimientos y acciones del ratón y teclado, como simular la pulsación de teclas.

import time
Se importa la biblioteca time, que permite controlar la ejecución mediante pausas o esperas.

def send_message(contact, message):
Esta es la definición de la función send_message, que recibe dos parámetros:

contact: el número de teléfono del destinatario (con código de país, sin signos como + o -).
message: el texto del mensaje que quieres enviar.

webbrowser.open(f"https://web.whatsapp.com/send?phone={contact}&text={message}")
Esta línea abre el navegador en WhatsApp Web con una URL especial que:

phone: es el número de teléfono del destinatario.
text: es el mensaje a enviar.

time.sleep(15)
Esta instrucción pausa la ejecución por 15 segundos, para darle tiempo a WhatsApp Web de cargarse completamente. Si la conexión es lenta, se podría aumentar este tiempo.

at.press('enter')
Esta línea usa pyautogui para simular la pulsación de la tecla "Enter", enviando así el mensaje al contacto.
---------------------------------------------------------------------

Los archivos ZOE_AI.py y zoe_gui_func.py ya tienen la maryoria de codigo comentado.... 