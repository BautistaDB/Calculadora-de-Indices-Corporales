import calculadora_indices as calc
import obtener_datos as obdat

def ejecutar():

    peso = obdat.obtener_peso()
    altura = obdat.obtener_altura_mts()


    indice_masa_corporal = calc.calcular_IMC(peso,altura)
    imc_redondeado = round(indice_masa_corporal, 2)
        
    print(" ")
    print(f"SU INDICE DE MASA CORPORAL ES: {imc_redondeado}%")
    print(" ")

    
    

