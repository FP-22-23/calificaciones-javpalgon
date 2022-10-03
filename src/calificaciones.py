def lee_entero(mensaje):
    res = int(input(mensaje))
    return res

def calcula_nota_cuestionario(aciertos, errores, respuestas_totales):
    return 10*(aciertos/respuestas_totales - errores/(50-respuestas_totales))

def lee_real(mensaje):
    res = float(input(mensaje))
    return res

def calcula_nota_cuatrimestre(cuestionarios, pr, ex):
    res = 10.0
    if pr < 5:
        res = 3.0
    else:
        res = 0.1*((cuestionarios[0] + cuestionarios[1] + cuestionarios[2])) + 0.1 * pr + 0.6 * ex

