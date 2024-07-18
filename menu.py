import consola_calculo_calorias_actividad
import consola_calculo_calorias_adelgazar
import consola_calculo_calorias_reposo
import consola_calculo_imc
import consola_calculo_porcentaje_grasa
                                                                        

while True:
    print("Esta es una calculadora de indices corporales")
    print("1 - Indice de masa corporal")
    print("2 - Porcentaje de grasa")
    print("3 - Calorias en reposo")
    print("4 - Calorias en actividad")
    print("5 - Calorias recomendadas para adelgazar")
    print("0 - Para salir del programa")      

    menu = int(input("Ingrese la opcion que desea realizar: "))

    match menu:
        case 1:
            print("Has seleccionado - Indice de masa corporal")
            rta = consola_calculo_imc.ejecutar()
        case 2:
            print("Has seleccionado - Porcentaje de grasa")
            rta = consola_calculo_porcentaje_grasa.ejecutar()
        case 3:
            print("Has seleccionado - Calorias en reposo")
            rta = consola_calculo_calorias_reposo.ejecutar()
        case 4:
            print("Has seleccionado - Calorias en actividad")
            rta = consola_calculo_calorias_actividad.ejecutar()
        case 5:
            print("Has seleccionado - Calorias recomendadas para adelgazar")
            rta = consola_calculo_calorias_adelgazar.ejecutar()
        case 0:
            print("Has salido del prgrama")
            break
        case _:
            print("Opción no válida")
