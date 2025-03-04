from cartas import Carta
import random

cartas = [1,2,3,4,5,6,7,10,10,10] 
cantidad = [4,4,4,4,4,4,4,4,4,4]
palos = ['Bastos', 'Copas', 'Oros', 'Espadas'] 
valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10']

mazo = []

for valor in valores:
    for j in range(cantidad[valores.index(valor)]):
        for palo in palos:
            mazo.append(Carta(palo, cartas[valores.index(valor)], valor))

def obtener_carta():
    if len(mazo) > 0:
        return mazo.pop(random.randint(0, len(mazo)-1))
    return None

def obtener_valor_mano(mano):
    suma = sum(carta.valor for carta in mano)
    num_ases = sum(1 for carta in mano if carta.nombre == 'As')
    
    while suma > 21 and num_ases:
        suma -= 10
        num_ases -= 1
    
    return suma

def mostrar_mano(mano):
    resultado = ""
    for carta in mano:
        resultado = resultado + str(carta)
        resultado = resultado + ", "
    return resultado[:-2]

mano_jugador = []
suma_jugador = 0
continuar = True

while continuar:
    contin = True
    while contin:
        carta = obtener_carta()
        if carta:
            contin = False
            
    mano_jugador.append(carta)
    
    if carta.nombre == 'As':
        choice = int(input("¿Quieres que tu As sea un 1 o un 11? (1/11): "))
        if choice == 1 or choice == 11:
            carta.valor = choice
            suma_jugador += choice
    else:
        suma_jugador += carta.valor
    
    print(f"Mano: {mostrar_mano(mano_jugador)}")
    print(f"Cantidad: {suma_jugador}")
    
    if suma_jugador >= 21:
        continuar = False
    else:
        choice = input("¿Te plantas? (s/n): ")
        if choice.lower() == "s":
            continuar = False

continuar = True
mano_casa = []
suma_casa = 0

while continuar:
    contin = True
    while contin:
        carta = obtener_carta()
        if carta:
            contin = False
            
    mano_casa.append(carta)
    suma_casa += carta.valor
    
    if suma_casa > 16:
        continuar = False

print(f"(Crupier) Mano: {mostrar_mano(mano_casa)}")
print(f"(Crupier) Cantidad: {suma_casa}")

if suma_jugador > 21 and suma_casa > 21:
    print("Gana la casa")
elif suma_jugador > suma_casa and suma_jugador <= 21:
    print("Gana jugador")
elif suma_jugador > suma_casa and suma_jugador > 21:
    print("Gana la casa")
elif suma_jugador < suma_casa and suma_casa <= 21:
    print("Gana la casa")
elif suma_jugador < suma_casa and suma_casa > 21:
    print("Gana jugador")
elif suma_jugador == suma_casa:
    print("Gana la casa")