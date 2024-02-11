import webbrowser
import pyautogui
from time import sleep
import pyperclip


def entradas():
    contacto_whatsapp = input("Ingrese el nombre del contanto del whatsapp: ")
    mensaje = input("Ingrese el mensaje que va enviar: ")
    cantidad = input("Ingrese la cantidad de veces que quiere enviar este mensaje: ")

    contacto_whatsapp = contacto_whatsapp.strip()

    try:
        cantidad = int(cantidad)
        ingresar_whatsapp_web()
        enviar_mensaje(contacto_whatsapp, mensaje, cantidad)
    except Exception as e:
        print("Ingrese un numero entero en la cantidad")


def ingresar_whatsapp_web():
    url = "https://web.whatsapp.com/"

    webbrowser.open(url)
    sleep(30)


def enviar_mensaje(contacto_whatsapp, mensaje, cantida):
    width, height = pyautogui.size()
    pyautogui.moveTo(width / 4, height / 5)
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
        else:
            pyautogui.press(tecla)
    pyautogui.press('enter')


def enviar_mensaje_x_cantidad(mensaje, cantida):
    for j in range(cantida):
        escribir(mensaje)
        print(j)


if __name__ == "__main__":
    entradas()
