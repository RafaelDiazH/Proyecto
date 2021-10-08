#Posiciones de las minas
import random
posiciones = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

minas = 18

while minas != 0:
    columnas = random.randint(0, 9)
    filas = random.randint(0, 9)
    if posiciones[filas][columnas] == 0:
        posiciones[filas][columnas] = 1
        minas = minas - 1

print(posiciones)

#Fin de juego
'''def evalua_mult(val_1, val_2):
    return val_1*val_2
def evalua_div(val_1, val_2):
    return val_1/val_2
x = 100
obtenidos = int(input())
print("el total de puntos fue", obtenidos)
minas_detonadas = int(input())
print("detonaste", minas_detonadas, "minas")
racha_mayor = int(input())
print("tu mejor racha sin minas fue de", racha_mayor)
div = evalua_div(obtenidos, minas_detonadas)
multi = evalua_mult(div, racha_mayor)
print("El total de puntos es ", multi)
while x <= multi:
    print("Felicidades, pasaste el nivel")
while multi <= x:
    print("Lastima, mejor suerte a la próxima")'''
