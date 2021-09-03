def evalua_mult(val_1, val_2):
    return val_1*val_2
def evalua_div(val_1, val_2):
    return val_1/val_2
def total(requeridos, obtenidos, resultado):
    if obtenidos => requeridos :
        resultado = resultado + 1
    if resultado => 1:
        puntuacion_positiva(requeridos, obtenidos, resultado)
    return resultado
    if resultado < 1:
        puntuacion_negativa(requeridos, obtenidos, resultado)
    return resultado
def puntuacion_positiva(requeridos, obtenidos, resultados):
    print("Tus puntos fueron: ", obtenidos)
    print("Los puntos necesarios eran: ", requeridos)
    print("Felicidades pasaste de nivel")
def puntuacion_negativa(requeridos, obtenidos, resultado):
    print("Tus puntos fueron: ", obtenidos)
    print("Los puntos necesarios eran: ", requeridos)
    print("Mejor suerte a la próxima")
