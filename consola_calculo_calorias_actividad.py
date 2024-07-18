import calculadora_indices as calc
import obtener_datos as obdat

def ejecutar():

    peso = obdat.obtener_peso()
    altura = obdat.obtener_altura_cms()
    edad = obdat.obtener_edad()
    valor_genero = obdat.obtener_genero()

    print("Error: Ingresa la letra M si es MASCULINO, F si es FEMENINO.")
    print("1: poco o ningún ejercicio")
    print("2: ejercicio ligero (1 a 3 días a la semana)")
    print("3: ejercicio moderado (3 a 5 días a la semana)")
    print("4: deportista (6 -7 días a la semana)")
    print("5: atleta (entrenamientos mañana y tarde.")
    valor_actividad = float(input("Ingrese la opcion que mas lo representa: "))
   
    calorias_actividad = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    ca_redondeado = round(calorias_actividad, 2)

    print(" ")
    print(f"LA CANTIDAD DE CALORÍAS QUE LA PERSONA QUEMA EN ACTIVIDAD ES: {ca_redondeado} cal.")
    print(" ")