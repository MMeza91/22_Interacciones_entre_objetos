


#● Al listar los productos existentes, se debe ocultar el stock de los productos en el caso de las tiendas de tipo Restaurante y Farmacia. Las tiendas de tipo Supermercado deben añadir el mensaje “Pocos productos disponibles” junto a la cantidad de stock del producto, en caso de que el stock del producto sea inferior a 10. Las tiendas de tipo Farmacia deben añadir el mensaje “Envío gratis al solicitar este producto” junto al precio de los productos con un valor superior a $15.000.

#NOTA: Considera que el método para listar los productos será llamado dentro de print, por lo que debe retornar un string.

#● Para realizar una venta, se debe solicitar el nombre del producto que se desea vender y la cantidad requerida. Las tiendas de tipo Farmacia y Supermercado deben tener stock existente del producto indicado (si no poseen stock, o no existe el producto solicitado, no se realiza ninguna acción). Sin embargo, los productos de las tiendas de tipo Restaurante siempre tienen stock 0, por lo que no es necesario hacer esta validación ni modificar el stock (Tip: puede usar pass). Además, en el caso específico de las tiendas de tipo Farmacia, no se puede solicitar una cantidad superior a 3 por producto en cada venta (si se solicita una cantidad mayor a 3, no se realiza ninguna acción). En el caso de las tiendas de tipo Farmacia o Supermercado, si la cantidad requerida es superior a la existente, solo se venderá la cantidad disponible (quedando entonces el stock del producto en 0). 



import abc

#El equipo te ha solicitado diseñar e implementar la arquitectura de clases que involucra a la entidad principal “Tienda”. Estas son las consideraciones que se deben tener en cuenta respecto de las tiendas:

#● Existen por el momento 3 tipos de tienda (en el futuro podría haber más), los cuales son: “Restaurante”, “Supermercado” y “Farmacia”.
    
#● Todas las tiendas deben poder ingresar un producto, listar los productos existentes, y realizar ventas.
    
#● Cada tienda creada, independiente de su tipo, posee un nombre, un listado de productos y un costo de delivery. Al momento de crear una nueva tienda, se debe solicitar el nombre y el costo de delivery (todas las tiendas se crean inicialmente sin productos). En una tienda ya existente, no se puede modificar el nombre ni el costo de delivery, pero sí se puede modificar los productos (mediante el ingreso de un producto,o mediante la realización de ventas).

class Tienda(abc):
    # 2. En un archivo tienda.py, definir la o las clases necesarias para instanciar los distintos tipos de tienda (utilice ABSTRACCIÓN y ENCAPSULAMIENTO). Cada clase que permita instanciar una tienda debe tener (considerar para cada punto la información entregada en la descripción de la problemática):

    # a. Un método constructor
    def __init__(self, nombre, delibery):
        self._nombre = nombre
        self._delibery = delibery
    

    #b. Un método para ingresar un producto (utilice COMPOSICIÓN, y opcionalmente COLABORACIÓN) 
    def ingresar_producto(self,producto):
        pass

    #c. Un método para listar productos
    def listar_productos(self):
        pass

    # d. Un método para realizar ventas (utilice COLABORACIÓN)
    def venta(self):
        pass

    #Nota 1: Una clase Compuesta puede tener una lista de Componentes del mismo tipo, almacenados en un atributo de tipo lista.

    #Nota 2: Si utilizas un método sobrecargado, también se considera colaboración. 

    # NOTA: Se asume que cada producto es específico de una tienda. Es decir, un producto no existe por sí mismo, sino que como parte de una tienda. Respecto del comportamiento de cada tipo de tienda, considere lo siguiente:

#● Para ingresar un producto a una tienda, se debe solicitar los datos requeridos del producto. Una vez creado el producto, éste se añade a la lista de productos a la tienda. Si el producto ya existe en la tienda (dado por su nombre), se debe modificar su stock, sumando al valor existente el stock del nuevo ingreso. Se conserva el precio del primer ingreso de un mismo producto. Tip: Pruebe sobrecargar los operadores __add__, __sub__ y __eq__.