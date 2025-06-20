#En un archivo producto.py, definir la clase que permita instanciar productos.
#Considera para la definición de esta clase lo señalado en la descripción de la problemática (utilice ENCAPSULAMIENTO).

class Producto:
    #● Los productos tienen un nombre, un precio y un stock. Los 3 valores se deben solicitar al momento de crear un producto nuevo, pero si no se indica stock, se asume que es 0. No se puede modificar el nombre ni el precio de un producto, solo su stock. Si se intenta modificar el stock por un valor menor a 0, se debe asignar 0 en su lugar. De cada producto se puede obtener su nombre, su precio o su stock.
    def __init__(self, nom_producto, precio,stock):
        pass