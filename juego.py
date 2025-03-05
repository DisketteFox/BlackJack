from cartas import Carta
import random

mazo = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,10,10,10,10,10,10,10,10,10,10,10,10]
palos = ['Bastos', 'Copas', 'Oros', 'Espadas'] 
valores = ['As', '2', '3', '4', '5', '6', '7', '10', '11']

random.shuffle(mazo)

def obtener_carta_jugador():
    num = mazo.pop(len(mazo) - 1)

    if num == 1:
        choice = int(input("¿Quieres que tu As sea un 1 o un 11? (1/11): "))
        if choice == 1 or choice == 11:
            return choice
    else:
        return num

def obtener_carta_crupier():
    return mazo.pop(len(mazo) - 1)


def mostrar_mano(mano):
    resultado = "Mano: "
    for carta in mano:
        resultado = resultado + str(carta)
        resultado = resultado + ", "
    return resultado

# Variables del jugador
mano_jugador = []
suma_jugador = 0
continuar = True

while continuar:
    carta = obtener_carta_jugador()
    
    mano_jugador.append(carta)
    suma_jugador += carta
    
    print(mostrar_mano(mano_jugador))
    print(f"Cantidad: {suma_jugador}")
    
    if suma_jugador >= 21:
        continuar = False
    else:
        choice = input("¿Te plantas? (s/n): ")
        if choice.lower() == "s":
            continuar = False

print("")

# Variables del Crupier
continuar = True
mano_casa = []
suma_casa = 0

while continuar:
    carta = obtener_carta_crupier()
            
    mano_casa.append(carta)
    suma_casa += carta
    
    if suma_casa > 16:
        continuar = False
print(f"(Crupier) {mostrar_mano(mano_casa)}")
print(f"(Crupier) Cantidad: {suma_casa}")

print("")

# Lógica final
if suma_jugador > 21 and suma_casa > 21:
    print(f"\033[31mGana la casa")
elif suma_jugador > suma_casa and suma_jugador <= 21:
    print(f"\033[92mGana jugador")
elif suma_jugador > suma_casa and suma_jugador > 21:
    print(f"\033[31mGana la casa")
elif suma_jugador < suma_casa and suma_casa <= 21:
    print(f"\033[31mGana la casa")
elif suma_jugador < suma_casa and suma_casa > 21:
    print(f"\033[92mGana jugador")
elif suma_jugador == suma_casa:
    print(f"\033[31mGana la casa")

print(f"\033[37m")