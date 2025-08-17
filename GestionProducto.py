class Producto:
    def __init__(self, nombre, categoria, precio, stock):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        if value is not None:
            self.__nombre = value
        else:
            raise ValueError("No puedo ingreasar campos vacíos")

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, value):
        if value is not None:
            self.__categoria = value
        else:
            raise ValueError("No puedo ingreasar campos vacíos")

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, value):
        if value > 0:
            self.__precio = value
        else:
            raise ValueError("El precio debe ser mayor a 0")

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("El número de stock debe ser mayor a 0")

    def __str__(self):
        return f'{self.__nombre}, categoría: {self.__categoria}, precio: Q.{self.__precio:.2f}, cantidad en stock: {self.__stock}'


class Inventario:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self):
        while True:
            try:
                codigo = input("Ingrese el codigo del producto: ")
                if codigo in self.inventario:
                    raise ValueError("Ya existe un producto con mismo código")
                nombre = input("\tNombre del producto: ")
                categoria = input("\tCategoria del producto: ")
                precio = float(input("\tPrecio del producto: "))
                stock = int(input("\tStock disponible: "))
                producto = Producto(nombre, categoria, precio, stock)
                self.inventario[codigo] = {'producto': producto}
                print("Producto agregado correctamente")
            except ValueError as e:
                print(f"Ha ocurrido un error: {e}")
            break

    def actualizar_precio(self, producto):
        try:
            precio = float(input("\tIngrese el nuevo precio: "))
            self.inventario[producto].precio = precio
        except ValueError as e:
            print("Ha ocurrido un error: ", e)

    def actualizar_stock(self, producto):
        try:
            stock = int(input("\tIngrese el nuevo stock: "))
            self.inventario[producto].stock = stock
        except ValueError as e:
            print("Ha ocurrido un error: ", e)

    def eliminar_producto(self, producto):
        del self.inventario[producto]

    def mostrar(self, productos):
        if not self.inventario:
            print("No hay productos en el inventario")
        else:
            for clave, producto in productos.items():
                print("Clave del pproducto: ", clave)
                print(producto)
