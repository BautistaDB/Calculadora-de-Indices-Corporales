import calculadora_indices as calc
import obtener_datos as obdat

def ejecutar():
    
    peso = obdat.obtener_peso()
    altura = obdat.obtener_altura_cms()
    edad = obdat.obtener_edad()
    valor_genero = obdat.obtener_genero()


    calorias_reposo = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    cr_redondeado = round(calorias_reposo, 2)

    print(" ")
    print(f"LA CANTIDAD DE CALORÍAS QUE LA PERSONA QUEMA EN REPOSO ES: {cr_redondeado} cal.")
    print(" ")