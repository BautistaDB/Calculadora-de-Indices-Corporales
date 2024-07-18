def obtener_peso():
    while True:
        peso = input("Ingrese el peso corporal en Kgs: ")
        peso = peso.replace(',', '.')
        try:
            return float(peso)
        except ValueError:
            print("Error: Ingresa un peso válido.")

def obtener_altura_cms():
    while True:
        altura = input("Ingrese la altura en Cms. : ")
        altura = altura.replace(',', "")
        altura = altura.replace('.', "")
            
        try:
            return float(altura)
        except ValueError:
            print("Error: Ingresa una altura válida.")
            
def obtener_altura_mts():
    while True:
        altura = input("Ingrese la altura en MTS.: ")
        altura = altura.replace(',', '.')
        try:
            return float(altura)
        except ValueError:
            print("Error: Ingresa una altura válida.")

def obtener_edad():
    while True:
        try:
            return int(input("Ingrese su edad: "))
        except ValueError:
            print("Error: Ingresa una edad válida.")

def obtener_genero():
    while True:
        valor_genero = input("Ingrese la letra M si es MASCULINO, F si es FEMENINO: ")
        if valor_genero in ['M', 'm', 'F', 'f']:
            return valor_genero
        else:
            print("Error: Ingresa la letra M si es MASCULINO, F si es FEMENINO.")