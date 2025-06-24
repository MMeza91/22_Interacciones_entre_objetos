from tienda import Tienda, Supermercado, Farmacia, Restaurante
import os
#3. En un archivo programa.py, implementa la lógica necesaria para crear una tienda e ingresar sus productos. 
# 
# Se debe solicitar ingresar productos hasta que el usuario indique lo contrario. 



#Elegir el tipo de tienda
##Se evalua que el dato ingresado sea correcto para continuar
print("=========== Bienvenido al programa especializado en Tiendas =======")

frase = """
Elija el tipo de tienda a trabajar:
    1.- Farmacia
    2.- Restaurant
    3.- Supermercado
elección: """

eleccion = Tienda.validador_numero_1al3(frase)

if eleccion == 1:
    valido = True
    tipo_tienda = "Farmacia"

elif eleccion == 2:
    valido = True
    tipo_tienda = "Restaurante"

elif eleccion == 3:
    valido = True
    tipo_tienda = "Supermercado"


#se piden los atributos de la clase
nombre = input(f"Ingrese el nombre de su {tipo_tienda}: ")

frase = f"Ingrese el costo de delivery de su {tipo_tienda}: "
delivery = Tienda.validador_numero_positivo(frase)

if tipo_tienda == "Farmacia":
    tienda = Farmacia(nombre, delivery)
elif tipo_tienda == "Restaurante":
    tienda = Restaurante(nombre, delivery)
elif tipo_tienda == "Supermercado": 
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
    elif pregunta.lower() == "n" or pregunta.lower() == "no":
        ingresar_productos = False
    else:
        print("\nValor ingresado no válido\n")

os.system('cls')
#ciclo para elegir listar productos, realizar venta o salir del programa

print(f"\n========== Bienvenido a nuestra tienda de {tipo_tienda} ==========\n")
while True:
    
    frase = """Ingrese su elección:
            1.- Listar los productos.
            2.- Realizar una venta.
            3.- Salir del programa.
        elección: """
    eleccion = Tienda.validador_numero_1al3(frase)

    if eleccion == 1:
        print(tienda.listar_productos())

    elif eleccion == 2:
        
        
        nombre_producto = input("Ingrese el nombre del producto a comprar: ") #realizar un buscar
        if tienda.buscador(nombre_producto) is None:
            print("\n\nEl Producto ingresado no se encuentra en nuestra base de datos\n\n")
            input("Aprete enter para continuar")
            os.system('cls')
            break
        cantidad_producto = Tienda.validador_numero_positivo("Ingrese la cantidad a comprar: ")

        existe, cantidad, monto = tienda.venta(nombre_producto, cantidad_producto)

        if existe:
            print(f"El monto a pagar es ${monto} pesos por {cantidad} {nombre_producto} más delivery")
        else: 
            print(f"{monto} {cantidad}")

    elif eleccion == 3:
        print("Un buen momento para descansar, adiós")
        exit()
    
    input("Aprete enter para continuar")
    os.system('cls')

    
    


