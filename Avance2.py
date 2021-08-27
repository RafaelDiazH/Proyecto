def divide(num1, num2):
    return num1/num2
def multiplica(num1, num2):
    return num1*num2
total = int(input())
print("el total de puntos fue", total)
minas_detonadas = int(input())
print("detonaste", minas_detonadas, "minas")
racha_mayor = int(input())
print("tu mejor racha sin minas fue de", racha_mayor)
div = divide(total, minas_detonadas)
print("puntos menos por minas ", div)
multi = multiplica(div, racha_mayor)
print("puntos totales con multplicador por racha ", multi)