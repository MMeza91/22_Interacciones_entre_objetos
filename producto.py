#En un archivo producto.py, definir la clase que permita instanciar productos.
#Considera para la definición de esta clase lo señalado en la descripción de la problemática (utilice ENCAPSULAMIENTO).

class Producto:
    #● Los productos tienen un nombre, un precio y un stock. Los 3 valores se deben solicitar al momento de crear un producto nuevo, pero si no se indica stock, se asume que es 0. No se puede modificar el nombre ni el precio de un producto, solo su stock. Si se intenta modificar el stock por un valor menor a 0, se debe asignar 0 en su lugar. De cada producto se puede obtener su nombre, su precio o su stock.
    def __init__(self, nom_producto, precio, stock = 0):
        self._nom_producto = nom_producto
        self._precio = precio
        self._stock = stock

    @property
    def nombre(self):
        return self._nom_producto
    
    @property
    def precio(self):
        return self._precio
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter 
    def stock(self,stock_nuevo):
        if stock_nuevo >= 0:
            self._stock = stock_nuevo
        elif stock_nuevo < 0:
            self._stock = 0
        else:
            print("\nEl stock del producto debe ser un valor numérico\n")



if __name__ == "__main__":

    prod = Producto("casa",1000,1)

    prod.set_stock(15)

    print(f"{prod.nombre} -- {prod.precio} -- {prod.stock}")