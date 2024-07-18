import calculadora_indices as calc
import obtener_datos as obdat

def ejecutar():
    peso = obdat.obtener_peso()
    altura = obdat.obtener_altura_cms()
    edad = obdat.obtener_edad()
    valor_genero = obdat.obtener_genero()
    
    calorias_min, calorias_max = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    print(f"Para adelgazar es recomendado que consumas entre: {calorias_min:.2f} y {calorias_max:.2f} calorías al día.")


                               
