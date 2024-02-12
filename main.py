import webbrowser
import pyautogui
from time import sleep
import speech_recognition as sr
import pyperclip
from word2number_es import w2n
import pyttsx3
import asyncio


async def entradas():
    salida_voz("Después de cada entrada por voz, esperé un segundo después de que terminé de hablar, para indicarme "
               "las acciones. De igual forma, indique los números cómo se escriben, por ejemplo, una vez, o una, "
               "por uno. Gracias por su atención y disfrute del script")
    salida_voz("Por favor, mencioné el nombre del contacto de WhatsApp al que le va a enviar el mensaje")
    contacto_whatsapp = entrada_voz("Por favor, mencioné el nombre del contacto de WhatsApp al que le va a enviar el "
                                    "mensaje: ")
    contacto_whatsapp = contacto_whatsapp.strip()
    salida_voz(f"Indique el mensaje que quiere enviar a {contacto_whatsapp}")
    mensaje = entrada_voz(f"Indique el mensaje que quiere enviar a {contacto_whatsapp}: ")
    salida_voz(f"Indique la cantidad de veces que le enviará el mensaje a {contacto_whatsapp}")
    cantidad = entrada_voz(f"Indique la cantidad de veces que le enviará el mensaje a {contacto_whatsapp}: ")

    cantidad = cantidad.strip()

    try:
        if cantidad:
            cantidad = w2n.word_to_num(cantidad)
            print(f"Número como entero: {cantidad}")
        else:
            raise ValueError("No se reconoció un número válido.")
        await ingresar_whatsapp_web()
        await enviar_mensaje(contacto_whatsapp, mensaje, cantidad)
        salida_voz(f"Mensajes enviados a {contacto_whatsapp}, correctamente")
    except Exception as e:
        raise ValueError("Ingrese un numero entero en la cantidad")


def entrada_voz(msj):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print(msj)
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=10)

        try:
            # Reconoce el texto a partir del audio
            text = recognizer.recognize_google(audio,  language='es-ES')
            print("Texto reconocido:", text)
        except sr.UnknownValueError:
            raise ValueError("No se pudo entender el audio")
        except sr.RequestError as e:
            raise ValueError(f"Error en la solicitud a Google API: {e}")

    return text


def salida_voz(mensaje):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(mensaje)
    engine.runAndWait()


async def ingresar_whatsapp_web():
    url = "https://web.whatsapp.com/"

    webbrowser.open(url)
    sleep(10)


async def enviar_mensaje(contacto_whatsapp, mensaje, cantida):
    width, height = pyautogui.size()
    pyautogui.moveTo(width / 5, height / 5)
    pyautogui.click()
    pyautogui.sleep(2)
    escribir(contacto_whatsapp)
    pyautogui.sleep(2)
    enviar_mensaje_x_cantidad(mensaje, cantida)


def escribir(cadena_caracteres):
    for tecla in cadena_caracteres:

        if 65 <= ord(tecla) <= 90:
            pyautogui.hotkey('shift', tecla.lower())
        elif ord(tecla) == 241:
            pyperclip.copy('ñ')
            pyautogui.hotkey('ctrl', 'v')
        elif ord(tecla) == 209:
            pyperclip.copy('Ñ')
            pyautogui.hotkey('ctrl', 'v')
        elif ord(tecla) == 225:
            pyperclip.copy('á')
            pyautogui.hotkey('ctrl', 'v')
        elif ord(tecla) == 233:
            pyperclip.copy('é')
            pyautogui.hotkey('ctrl', 'v')
        elif ord(tecla) == 237:
            pyperclip.copy('í')
            pyautogui.hotkey('ctrl', 'v')
        elif ord(tecla) == 243:
            pyperclip.copy('ó')
            pyautogui.hotkey('ctrl', 'v')
        elif ord(tecla) == 250:
            pyperclip.copy('ú')
            pyautogui.hotkey('ctrl', 'v')
        elif ord(tecla) == 193:
            pyperclip.copy('Á')
            pyautogui.hotkey('ctrl', 'v')
        elif ord(tecla) == 201:
            pyperclip.copy('É')
            pyautogui.hotkey('ctrl', 'v')
        elif ord(tecla) == 205:
            pyperclip.copy('Í')
            pyautogui.hotkey('ctrl', 'v')
        elif ord(tecla) == 211:
            pyperclip.copy('Ó')
            pyautogui.hotkey('ctrl', 'v')
        elif ord(tecla) == 218:
            pyperclip.copy('Ú')
            pyautogui.hotkey('ctrl', 'v')
        elif ord(tecla) == 252:
            pyperclip.copy('ü')
            pyautogui.hotkey('ctrl', 'v')
        elif ord(tecla) == 220:
            pyperclip.copy('Ü')
            pyautogui.hotkey('ctrl', 'v')
        else:
            pyautogui.press(tecla)
    pyautogui.press('enter')


def enviar_mensaje_x_cantidad(mensaje, cantida):
    for j in range(cantida):
        escribir(mensaje)
        print(j+1)


if __name__ == "__main__":
    asyncio.run(entradas())
