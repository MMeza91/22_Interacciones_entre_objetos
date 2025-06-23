from abc import ABC, abstractmethod
from producto import Producto

#El equipo te ha solicitado diseñar e implementar la arquitectura de clases que involucra a la entidad principal “Tienda”. Estas son las consideraciones que se deben tener en cuenta respecto de las tiendas:

#● Existen por el momento 3 tipos de tienda (en el futuro podría haber más), los cuales son: “Restaurante”, “Supermercado” y “Farmacia”.
    
#● Todas las tiendas deben poder ingresar un producto, listar los productos existentes, y realizar ventas.
    
#● Cada tienda creada, independiente de su tipo,
#  posee un nombre, 
# un listado de productos 
# y un costo de delivery. 
# 
# Al momento de crear una nueva tienda, se debe solicitar el nombre y el costo de delivery (todas las tiendas se crean inicialmente sin productos). En una tienda ya existente, no se puede modificar el nombre ni el costo de delivery, pero sí se puede modificar los productos (mediante el ingreso de un producto,o mediante la realización de ventas).

class Tienda(ABC):
    # 2. En un archivo tienda.py, definir la o las clases necesarias para instanciar los distintos tipos de tienda (utilice ABSTRACCIÓN y ENCAPSULAMIENTO). Cada clase que permita instanciar una tienda debe tener (considerar para cada punto la información entregada en la descripción de la problemática):

    # a. Un método constructor
    def __init__(self, nombre:str, delivery):
        self.__nombre = nombre
        self.__delivery = delivery
        self.__lista_productos = []

    @staticmethod
    def validador_numero_entero(stock:int) -> bool:
        #Evalúa si el valor ingresado es entero
        if stock >= 0:
            return True
        else:
            return False

        
    @staticmethod
    def buscador(objetivo:str,lista:list[str]) -> int:
        #Se entrega el valor objetivo y la lista donde se buscará, devuelve la posición dentro de la lista
        for posicion in range(len(lista)):
            if objetivo.lower() == lista[posicion].nombre.lower():
                return posicion
            else:
                return None

    #b. Un método para ingresar un producto (utilice COMPOSICIÓN, y opcionalmente COLABORACIÓN) 
    @abstractmethod
    def ingresar_producto(self):
        pass

        #● Para ingresar un producto a una tienda, se debe solicitar los datos requeridos del producto. Una vez creado el producto, éste se añade a la lista de productos a la tienda.
        # Si el producto ya existe en la tienda (dado por su nombre), se debe modificar su stock, sumando al valor existente el stock del nuevo ingreso. Se conserva el precio del primer ingreso de un mismo producto.

    #c. Un método para listar productos
    @abstractmethod
    def listar_productos(self):
        #● Al listar los productos existentes, se debe ocultar el stock de los productos en el caso de las tiendas de tipo Restaurante y Farmacia. Las tiendas de tipo Supermercado deben añadir el mensaje “Pocos productos disponibles” junto a la cantidad de stock del producto, en caso de que el stock del producto sea inferior a 10. Las tiendas de tipo Farmacia deben añadir el mensaje “Envío gratis al solicitar este producto” junto al precio de los productos con un valor superior a $15.000.

#NOTA: Considera que el método para listar los productos será llamado dentro de print, por lo que debe retornar un string.

        pass

    # d. Un método para realizar ventas (utilice COLABORACIÓN)
    @abstractmethod
    def venta(self):
        #● Para realizar una venta, se debe solicitar el nombre del producto que se desea vender y la cantidad requerida. Las tiendas de tipo Farmacia y Supermercado deben tener stock existente del producto indicado (si no poseen stock, o no existe el producto solicitado, no se realiza ninguna acción). Sin embargo, los productos de las tiendas de tipo Restaurante siempre tienen stock 0, por lo que no es necesario hacer esta validación ni modificar el stock (Tip: puede usar pass). Además, en el caso específico de las tiendas de tipo Farmacia, no se puede solicitar una cantidad superior a 3 por producto en cada venta (si se solicita una cantidad mayor a 3, no se realiza ninguna acción). En el caso de las tiendas de tipo Farmacia o Supermercado, si la cantidad requerida es superior a la existente, solo se venderá la cantidad disponible (quedando entonces el stock del producto en 0). 

        pass



class Restaurante(Tienda):
    def __init__(self, nombre, delivery):
        self.__nombre = nombre
        self.__delivery = delivery
        self.__lista_productos = []

    def ingresar_producto(self):
        nombre_producto = input("\nIngrese el nombre del producto: ")
        #Evaluamos que el precio del producto sea un número entero mayor o igual a 0
        #En caso de no ser valido, se vuelve a pedir que se ingrese el valor
        valido = False
        while not valido:
            try:
                precio = int(input("Ingrese el precio del producto: "))
                valido = Tienda.validador_numero_entero(precio)
                if not valido:
                    print("\n¡Error! Se debe ingresar un valor entero mayor o igual a cero.\n")
            except:
                print("\n¡Error! Se debe ingresar un valor entero mayor o igual a cero.\n")
        
        #se busca el nombre del producto en la lista, si no se encuentra, se añade, si se encuentra se actualiza el stock
        posicion = Tienda.buscador(nombre_producto, self.__lista_productos)
        if posicion is None:
            producto = Producto(nombre_producto, precio,)
            self.__lista_productos.append(producto)
            print("\n:::::: Producto ingresado ::::::::\n")

        else:
            print("\nEl producto ya se encuentra en la lista del Restaurante\n")

    def listar_productos(self):
        #● Al listar los productos existentes, se debe ocultar el stock de los productos en el caso de las tiendas de tipo Restaurante.
        #NOTA: Considera que el método para listar los productos será llamado dentro de print, por lo que debe retornar un string.
        retorno = (f"::::: Productos de nuestro Restaurante {self.__nombre} ::::\nProducto\tPrecio\n")

        items = [f"{i.nombre}\t\t{i.precio}\n" for i in self.__lista_productos]

        return f"{retorno}{''.join(items)}"

        
    def venta(self,nombre_producto, cantidad):
        #● Para realizar una venta, se debe solicitar el nombre del producto que se desea vender y la cantidad requerida. 
        # los productos de las tiendas de tipo Restaurante siempre tienen stock 0, por lo que no es necesario hacer validación ni modificar el stock (Tip: puede usar pass). 

        #Se busca la posición del producto dentro de la lista
        posicion = Tienda.buscador(nombre_producto, self.__lista_productos)
        if posicion is None:
            return False, 0
        else:
            #se calcula el monto de la venta considerando el precio y cantidad del producto solicitado y el monto del delibery
            monto = self.__lista_productos[posicion].precio * cantidad + self.__delivery


            return True, cantidad, monto



class Farmacia(Tienda):
    def __init__(self, nombre, delivery):
        self.__nombre = nombre
        self.__delivery = delivery
        self.__lista_productos = []

    def ingresar_producto(self):
        nombre_producto = input("\nIngrese el nombre del producto: ")
        #Evaluamos que el precio del producto sea un número entero mayor o igual a 0
        #En caso de no ser valido, se vuelve a pedir que se ingrese el valor
        valido = False
        while not valido:
            try:
                precio = int(input("Ingrese el precio del producto: "))
                valido = Tienda.validador_numero_entero(precio)
                if not valido:
                    print("\n¡Error! Se debe ingresar un valor entero mayor o igual a cero.\n")
            except:
                print("\n¡Error! Se debe ingresar un valor entero mayor o igual a cero.\n")
        
        #Evaluamos el stock ingresado, en caso de no ser valido, se asume stock 0
        try:
            stock_ingresado = int(input("Ingrese el stock del producto: "))
            valido = Tienda.validador_numero_entero(stock_ingresado)
            if not valido:
                stock_ingresado = 0
        except:
            stock_ingresado = 0            

        #se busca el nombre del producto en la lista, si no se encuentra, se añade, si se encuentra se actualiza el stock
        posicion = Tienda.buscador(nombre_producto, self.__lista_productos)
        if posicion is None:
            producto = Producto(nombre_producto, precio, stock_ingresado)
            self.__lista_productos.append(producto)
        
        else:
            self.__lista_productos[posicion].stock = stock_ingresado

    def listar_productos(self):
        #● Al listar los productos existentes, se debe ocultar el stock de los productos en el caso de las tiendas de tipo Farmacia. 
        # Las tiendas de tipo Farmacia deben añadir el mensaje “Envío gratis al solicitar este producto” junto al precio de los productos con un valor superior a $15.000.

        retorno = (f"::::: Productos de nuestra Farmacia {self.__nombre} ::::\nProducto\tPrecio\n")

        envio_gratis = "Envío gratis al solicitar este producto"
        items = []
        for i in self.__lista_productos:
            if i.precio > 15000:
                extra = envio_gratis
            else:
                extra = ""
            items.append(f"{i.nombre}\t\t${i.precio}pesos {extra}\n")
                

        return f"{retorno}{''.join(items)}"
        

    # d. Un método para realizar ventas (utilice COLABORACIÓN)

    def venta(self,nombre_producto, cantidad):
        #● Para realizar una venta, se debe solicitar el nombre del producto que se desea vender y la cantidad requerida.
        # Las tiendas de tipo Farmacia deben tener stock existente del producto indicado (si no poseen stock, o no existe el producto solicitado, no se realiza ninguna acción). 
        # En el caso específico de las tiendas de tipo Farmacia, no se puede solicitar una cantidad superior a 3 por producto en cada venta (si se solicita una cantidad mayor a 3, no se realiza ninguna acción). 
        # En el caso de las tiendas de tipo Farmacia, si la cantidad requerida es superior a la existente, solo se venderá la cantidad disponible (quedando entonces el stock del producto en 0). 



        #Se busca la posición del producto dentro de la lista
        posicion = Tienda.buscador(nombre_producto, self.__lista_productos)
        #se evalua condiciones de problema
        if cantidad > 3: 
            return False, cantidad, "La cantidad debe ser menor o igual a 3 unidades y tú solicitaste:"
        
        elif self.__lista_productos[posicion].stock == 0:
            return False, self.__lista_productos[posicion].stock, "No nos queda stock de este producto, stock ="
        
        elif cantidad > self.__lista_productos[posicion].stock:
            #se actualiza la cantidad a comprar por el stock disponible
            cantidad = self.__lista_productos[posicion].stock

        #se calcula el monto de la venta considerando el precio y cantidad del producto solicitado y el monto del delibery
        delivery = self.__delivery
        if self.__lista_productos[posicion].precio > 15000:
            delivery = 0
        monto = self.__lista_productos[posicion].precio * cantidad + delivery
        self.__lista_productos[posicion].stock -= cantidad

        return True, cantidad, monto

 

class Supermercado(Tienda):
    def __init__(self, nombre, delivery):
        self.__nombre = nombre
        self.__delivery = delivery
        self.__lista_productos = []

    def ingresar_producto(self):
        nombre_producto = input("\nIngrese el nombre del producto: ")
        #Evaluamos que el precio del producto sea un número entero mayor o igual a 0
        #En caso de no ser valido, se vuelve a pedir que se ingrese el valor
        valido = False
        while not valido:
            try:
                precio = int(input("Ingrese el precio del producto: "))
                valido = Tienda.validador_numero_entero(precio)
                if not valido:
                    print("\n¡Error! Se debe ingresar un valor entero mayor o igual a cero.\n")
            except:
                print("\n¡Error! Se debe ingresar un valor entero mayor o igual a cero.\n")
        
        #Evaluamos el stock ingresado, en caso de no ser valido, se asume stock 0
        try:
            stock_ingresado = int(input("Ingrese el stock del producto: "))
            valido = Tienda.validador_numero_entero(stock_ingresado)
            if not valido:
                stock_ingresado = 0
        except:
            stock_ingresado = 0            

        #se busca el nombre del producto en la lista, si no se encuentra, se añade, si se encuentra se actualiza el stock
        posicion = Tienda.buscador(nombre_producto, self.__lista_productos)
        if posicion is None:
            producto = Producto(nombre_producto, precio, stock_ingresado)
            self.__lista_productos.append(producto)
        
        else:
            self.__lista_productos[posicion].stock = stock_ingresado

    def listar_productos(self):
        #● Al listar los productos existentes, las tiendas de tipo Supermercado deben añadir el mensaje “Pocos productos disponibles” junto a la cantidad de stock del producto, en caso de que el stock del producto sea inferior a 10. 

#NOTA: Considera que el método para listar los productos será llamado dentro de print, por lo que debe retornar un string.

        retorno = (f"::::: Productos de nuestra Farmacia {self.__nombre} ::::\nProducto\tPrecio\t\tstock\n")

        disponibles = "Pocos productos disponibles"
        items = []
        for i in self.__lista_productos:
            if i.stock < 10:
                extra = disponibles
            else:
                extra = ""

            items.append(f"{i.nombre}\t\t${i.precio}pesos\t{i.stock} {extra}\n")
                

        return f"{retorno}{''.join(items)}"

    # d. Un método para realizar ventas (utilice COLABORACIÓN)

    def venta(self, nombre_producto, cantidad):
        #● Para realizar una venta, se debe solicitar el nombre del producto que se desea vender y la cantidad requerida. 
        # Las tiendas de tipo Supermercado deben tener stock existente del producto indicado (si no poseen stock, o no existe el producto solicitado, no se realiza ninguna acción). 
        # En el caso de las tiendas de tipo Supermercado, si la cantidad requerida es superior a la existente, solo se venderá la cantidad disponible (quedando entonces el stock del producto en 0). 

        posicion = Tienda.buscador(nombre_producto, self.__lista_productos)
        #se evalua condiciones de problema
        if cantidad > 3: 
            return False, cantidad, "La cantidad debe ser menor o igual a 3 unidades y tú solicitaste:"
        
        elif self.__lista_productos[posicion].stock == 0:
            return False, self.__lista_productos[posicion].stock, "No nos queda stock de este producto, stock ="
        
        elif cantidad > self.__lista_productos[posicion].stock:
            #se actualiza la cantidad a comprar por el stock disponible
            cantidad = self.__lista_productos[posicion].stock

        #se calcula el monto de la venta considerando el precio y cantidad del producto solicitado y el monto del delibery
        monto = self.__lista_productos[posicion].precio * cantidad + self.__delivery
        self.__lista_productos[posicion].stock -= cantidad

        return True, cantidad, monto



if __name__ == "__main__":

    tienda = Supermercado("Concepción", 5000)
    ingresar_productos = True
    tienda.ingresar_producto()
    while ingresar_productos:
        print("\nDo you want a new product deposit? y/n")
        pregunta = input()
        if pregunta.lower() == "y" or pregunta.lower() == "yes":
            tienda.ingresar_producto()
        else:
            ingresar_productos = False

    print(tienda.listar_productos())

    nombre_producto = input("Ingrese el nombre del producto a comprar: ") #realizar un buscar
    cantidad_producto = int(input("Ingrese la cantidad: "))

    existe, cantidad, monto = tienda.venta(nombre_producto, cantidad_producto)

    if existe:
        print(f"El monto a pagar es ${monto} pesos por {cantidad} {nombre_producto} más delivery")
    else: 
        print(f"{monto} {cantidad}")

    #------------------------------------------------------------------------------------------------------
