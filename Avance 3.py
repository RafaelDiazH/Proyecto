def evalua_mult(val_1, val_2):
    return val_1*val_2
def evalua_div(val_1, val_2):
    return val_1/val_2
lim = 100
obtenidos = int(input())
print("el total de puntos fue", obtenidos)
minas_detonadas = int(input())
print("detonaste", minas_detonadas, "minas")
racha_mayor = int(input())
print("tu mejor racha sin minas fue de", racha_mayor)
div = evalua_div(obtenidos, minas_detonadas)
multi = evalua_mult(div, racha_mayor)
print("El total de puntos es ", multi)
while multi > lim:
    print("Felicidades, pasaste el nivel")
while multi < lim:
    print("Lastima, mejor suerte a la próxima")

    