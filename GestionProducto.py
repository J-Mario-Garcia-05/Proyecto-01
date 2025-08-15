class Producto:
    def __init__(self, nombre, categoria, precio):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
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
    def __str__(self):
        return f'{self.__nombre}, categoría: {self.__categoria}, precio: {self.__precio}'