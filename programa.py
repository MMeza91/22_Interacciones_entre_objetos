from tienda import Supermercado, Farmacia, Restaurante
import os
#3. En un archivo programa.py, implementa la lógica necesaria para crear una tienda e ingresar sus productos. 
# 
# Se debe solicitar ingresar productos hasta que el usuario indique lo contrario. 



#Elegir el tipo de tienda
##Se evalua que el dato ingresado sea correcto para continuar
print("=========== Bienvenido al programa especializado en Tiendas =======")
valido = False
while not valido:
    try:
        eleccion = int(input("""
Elija el tipo de tienda a trabajar:
    1.- Farmacia
    2.- Restaurant
    3.- Supermercado
elección: """))

        if eleccion == 1:
            valido = True
            tipo_tienda = "Farmacia"

        elif eleccion == 2:
            valido = True
            tipo_tienda = "Restaurante"

        elif eleccion == 3:
            valido = True
            tipo_tienda = "Supermercado"

        else:
            print("\n::: El valor ingresado no es válido ::: \nDebe elegir un valor entero entre 1 y 3 incluyendolos")
    except:
        print("\n::: Error, valor ingresado no válido :::\nDebe elegir un valor entero entre 1 y 3 incluyendolos")
    input("Aprete enter para continuar")
    os.system('cls')

#se piden los atributos de la clase
nombre = input(f"Ingrese el nombre de su {tipo_tienda}: ")

valido = False
while not valido:
    try:
        delivery = int(input(f"Ingrese el costo de delivery de su {tipo_tienda}: "))
        valido = True
    except:
        print("\n::: Error, Debe ser un valor entero mayor o igual a cero :::\n")
    input("Aprete enter para continuar")
    os.system('cls')

if tipo_tienda == "Farmacia":
    tienda = Farmacia(nombre, delivery)
if tipo_tienda == "Restaurante":
    tienda = Restaurante(nombre, delivery)
else:
    tienda = Supermercado(nombre, delivery)

print(f"Su tienda de tipo {tipo_tienda} fue creada con exito")
#ingresar productos
ingresar_productos = True
tienda.ingresar_producto()
while ingresar_productos:
    print("\nQuieres ingresar un nuevo producto? s/n")
    pregunta = input()
    if pregunta.lower() == "s" or pregunta.lower() == "si":
        tienda.ingresar_producto()
    else:
        ingresar_productos = False

os.system('cls')
while True:
    
print(tienda.listar_productos())

input("Aprete enter para continuar")
os.system('cls')
#ciclo para elegir listar productos, realizar venta o salir del programa