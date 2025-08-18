class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__stock = stock

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, value):
        if value != '':
            self.__codigo = value
        else:
            raise ValueError('Codigo no valido')

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        if value != '':
            self.__nombre = value
        else:
            raise ValueError("El nombre no puede estar vacío")

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, value):
        if value != '':
            self.__categoria = value
        else:
            raise ValueError("La categoría no puede estar vacío")

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
            raise ValueError("El stock no puede ser negativo")

    def __str__(self):
        return f"{self.__codigo} - {self.__nombre}, categoría: {self.__categoria}, precio: Q.{self.__precio:.2f}, stock: {self.__stock}"

class Inventario:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, producto: Producto):
        if producto.codigo in self.inventario:
            raise ValueError('Ya existe un producto con el mismo código')
        self.inventario[producto.codigo] = producto

    def listar_productos(self, clave="nombre"):
        lista = list(self.inventario.values())
        return Ordenador.quick_sort(lista, clave) if lista else []

    def actualizar_precio(self, codigo, nuevo_precio):
        if codigo in self.inventario:
            self.inventario[codigo].precio = nuevo_precio
        else:
            raise ValueError("Producto no encontrado")

    def actualizar_stock(self, codigo, nuevo_stock):
        if codigo in self.inventario:
            self.inventario[codigo].stock = nuevo_stock
        else:
            raise ValueError("Producto no encontrado")

    def eliminar_producto(self, codigo):
        if codigo in self.inventario:
            del self.inventario[codigo]
        else:
            raise ValueError("Producto no encontrado")
