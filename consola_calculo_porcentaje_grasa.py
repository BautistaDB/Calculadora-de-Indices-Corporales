import calculadora_indices as calc
import obtener_datos as obdat

def ejecutar():

    peso = obdat.obtener_peso()
    altura = obdat.obtener_altura_mts()
    edad = obdat.obtener_edad()
    valor_genero = obdat.obtener_genero()

    grasa_corporal = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    gc_redondeado = round(grasa_corporal, 2)

    print(" ")
    print(f"SU GRASA CORPORAL ES: {gc_redondeado}%")
    print(" ")
                    