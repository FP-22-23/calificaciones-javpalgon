from calificaciones import *
def main():
    c1= lee_real("Dame la nota del C1: ")
    c2= lee_real("dame la nota del c2: ")
    c3= lee_real("dame la nota del c3: ")
    pr1= lee_real("dame la nota del proyecto en python: ")
    ex1= lee_real("dame la nota del examen práctico de python: ")
    cuatrimestre1 = calcula_nota_cuatrimestre(c1,c2,c3,pr1,ex1)
    print("Tu nota del primer cuatrimestre es: ", cuatrimestre1)
    c4= lee_real("dame la nota del c4: ")
    c5= lee_real("dame la nota del c5: ")
    c6= lee_real("dame la nota del c6: ")
    pr2= lee_real("dame la nota del proyecto en java: ")
    ex2= lee_real("dame la nota del examen practico de java: ")
    cuatrimestre2 = calcula_nota_cuatrimestre(c4,c5,c6,pr2,ex2)
    print("Tu nota del segundo cuatrimestre es: ", cuatrimestre2)
    datos = lee_notas("introduzca las notas que has sacado este año", 10)
    print("Tu nota final es: ", ((cuatrimestre1+cuatrimestre2)/2)
    
if __name__=="__main__":
    main()