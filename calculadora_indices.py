def calcular_IMC(peso, altura):
    """
    Calcula el índice de masa corporal de una persona 
    a partir de la ecuación definida anteriormente.
    """
    imc = peso / (altura ** 2) 
    return imc

def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):

    """
    Calcula el porcentaje de grasa de una persona 
    a partir de la ecuación definida anteriormente.
    """

    if valor_genero == 'm' or valor_genero == "M":  
        valor_genero = 10.8
    elif valor_genero == 'f' or valor_genero == "F":
        valor_genero = 0

    gc = 1.2 * calcular_IMC(peso, altura) + 0.23 * edad - 5.4 - valor_genero 
    return gc

def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    """
    Calcula la cantidad de calorías que una persona quema estando enreposo 
    (esto es, su tasa metabólica basal), a partir de la ecuación definida anteriormente.
    """
    if valor_genero == 'm' or valor_genero == "M": 
            valor_genero = 5
    elif valor_genero == 'f' or valor_genero == "F":
            valor_genero = -161
    
    tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + valor_genero
    return tmb


def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
    """
    Calcula la cantidad de calorías que una persona quema al realizar algún
    tipo de actividad física (esto es, su tasa metabólica basal según actividad física),
    a partir de la ecuación definida anteriormente.
    """

    try:
            match valor_actividad:
                case 1:
                    valor_actividad = 1.2
        
                case 2:
                    valor_actividad = 1.375
           
                case 3:
                    valor_actividad = 1.55
        
                case 4:
                    valor_actividad = 1.725
            
                case 5:
                    valor_actividad = 1.9
            
                case _:
                    print("Opción no válida")

    except ValueError:
            print("Error: Ingresa una opcion válida.")

    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    tmb_actividad_fisica = tmb * valor_actividad
    return tmb_actividad_fisica


def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad,valor_genero):
    """
    Calcula el rango de calorías recomendado, que debe consumir una persona diariamente
    en caso de que desee adelgazar, a partir de la ecuación definida anteriormente.
    """

    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    calorias_min = tmb * 0.80
    calorias_max = tmb * 0.85
    return calorias_min, calorias_max

