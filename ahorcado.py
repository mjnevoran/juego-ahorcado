from palabras import PALABRAS
import random

def menu():
    print("Menú")
    print("a. Jugar")
    print("b. Salir")

    opcion = input("Seleccione la opción a o b según desee: ").lower()

    while opcion not in ('a', 'b'):
        print("Opción inválida. Por favor, ingrese 'a' o 'b'.")
        opcion = input("Seleccione la opción a o b según desee: ").lower()

    return opcion

def inicio():
    print("Juego del ahorcado")
    jugador = input("Escriba su nombre para comenzar: ")
    return jugador

def elegir_palabra(PALABRAS):
    palabra_seleccionada = random.choice(PALABRAS)
    return palabra_seleccionada

def mostrar_guiones(palabra, letras_correctas):
    guiones_con_letras = ""
    for letra in palabra:
        if letra.lower() in letras_correctas:
            guiones_con_letras += letra
        else:
            guiones_con_letras += '_'
    print(guiones_con_letras)
    return guiones_con_letras
def muneco_ahorcado():
    muneco = [
        [
            "   O",
            "  /|\\",
            "  / \\"
        ],
    ]

    for line in muneco[0]:
        print(line)

def indicar_letra(letra, palabra, guiones, intentos, puntuacion):
    letra = letra.lower()
    juego_terminado = False 

    if letra in intentos or letra in guiones:
        print("Ya intentaste con esa letra. Intenta con otra.")
    elif letra in palabra.lower():
        print("¡Correcto!")
        guiones_actualizados = ""
        for i in range(len(palabra)):
            if palabra[i].lower() == letra:
                guiones_actualizados += letra
            else:
                guiones_actualizados += guiones[i]
        
        if guiones_actualizados == palabra.lower():
            puntuacion += 10
            print("¡Felicidades! Has adivinado la palabra.")
            print(f"Puntuación actual: {puntuacion}")
            juego_terminado = True 
        else:
            guiones, puntuacion = guiones_actualizados, puntuacion
    else:
        intentos.append(letra)
        if len(intentos) <= 5:
            print(f"La letra no se encuentra en la palabra. Intento fallido. ({len(intentos)} de 5 intentos)")
            puntuacion -= 5
        else:
            print("¡Perdiste! Llegaste al límite de intentos. La palabra era:", palabra)
            print(f"Puntuación actual: {puntuacion}")
            juego_terminado = True  

    return guiones, puntuacion, juego_terminado


def main():
    jugador = inicio()
    muneco_ahorcado()
    opcion = menu()

    while opcion == 'a':
        intentos_maximos = 5
        puntuacion = 0
        palabra_seleccionada = elegir_palabra(PALABRAS)
        guiones = mostrar_guiones(palabra_seleccionada, [])
        intentos = []
        juego_terminado = False

        while len(intentos) < intentos_maximos and not juego_terminado:
            letra = input("Ingresa una letra: ")
            guiones, puntuacion, juego_terminado = indicar_letra(letra, palabra_seleccionada, guiones, intentos, puntuacion)
            print(guiones)

        mensaje_ganador = "¡Felicidades! Has adivinado la palabra."
        mensaje_perdedor = f"¡Perdiste! La palabra era: {palabra_seleccionada}"
        print(mensaje_ganador if juego_terminado else mensaje_perdedor)
        print(f"Puntuación actual: {puntuacion}")
        muneco_ahorcado() if juego_terminado else None

        opcion = input("¿Quieres jugar de nuevo? (ingrese 'a' para sí, otra letra para no): ").lower()

    print("¡Hasta luego!")

main()
