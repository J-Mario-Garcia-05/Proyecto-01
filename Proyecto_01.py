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
        if value >= 0:
            self.__stock = value
        else:
            raise ValueError("El stock debe ser mayor o igual a 0")

    def __str__(self):
        return f"{self.__codigo} - {self.__nombre}, categoría: {self.__categoria}, precio: Q.{self.__precio:.2f}, stock: {self.__stock}"


class Ordenador:
    @staticmethod  # se usa el método estatico para no usar constructor
    def obtener_valor(producto, clave):
        if clave == "codigo":
            return producto.codigo
        elif clave == "nombre":
            return producto.nombre
        elif clave == "categoria":
            return producto.categoria
        elif clave == "precio":
            return producto.precio
        elif clave == "stock":
            return producto.stock
        return producto.nombre  # pro defecto se va a ordenar por nombre

    @staticmethod
    def quick_sort(lista, clave):
        if len(lista) <= 1:
            return lista
        pivote = Ordenador.obtener_valor(lista[0], clave)
        menores = [x for x in lista[1:] if Ordenador.obtener_valor(x, clave) < pivote]
        iguales = [x for x in lista if Ordenador.obtener_valor(x, clave) == pivote]
        mayores = [x for x in lista[1:] if Ordenador.obtener_valor(x, clave) > pivote]
        return Ordenador.quick_sort(menores, clave) + iguales + Ordenador.quick_sort(mayores, clave)


class Buscador:
    @staticmethod
    def buscar(lista, clave, valor):
        resultados = []
        for producto in lista:
            if clave == "codigo" and producto.codigo == valor:
                resultados.append(producto)
            elif clave == "nombre" and valor.lower() in producto.nombre.lower():
                resultados.append(producto)
            elif clave == "categoria" and valor.lower() in producto.categoria.lower():
                resultados.append(producto)
        return resultados


class Inventario:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, producto: Producto):
        if producto.codigo in self.inventario:
            raise ValueError('Ya existe un producto con el mismo código')
        self.inventario[producto.codigo] = producto

    def listar_productos(self, clave):
        lista = list(self.inventario.values())
        return Ordenador.quick_sort(lista, clave) if lista else []

    def buscar_producto(self, clave, valor):
        lista = list(self.inventario.values())
        return Buscador.buscar(lista, clave, valor)

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


# MENU
def menu():
    inventario = Inventario()

    while True:
        print("\n---MENÚ DE INVENTARIO---")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Salir")
        opcion = input("Seleccione una opción:")

        if opcion == "1":
            codigo = input("Código del producto: ")
            nombre = input("Nombre del producto: ")
            categoria = input("Categoria del producto: ")
            try:
                precio = float(input("Precio del producto: Q."))
                stock = int(input("Stock del producto: "))
                producto = Producto(codigo, nombre, categoria, precio, stock)
                inventario.agregar_producto(producto)
                print("Producto agregado correctamente")
            except ValueError as e:
                print(f"Ha ocurrido un error: {e}")

        elif opcion == "2":
            clave = input("Ordenar por (nombre, precio, stock): ").lower()
            if clave not in ["nombre", "precio", "stock"]:
                print("Orden no valido, se ordenará por nombre")
                clave = "nombre"
            productos = inventario.listar_productos(clave)
            if productos:
                for p in productos:
                    print(p)
            else:
                print("No hay productos en el inventario")

        elif opcion == "3":
            clave = input("Buscar por (codigo, nombre, categoria): ").lower()
            valor = input(f"Ingrese el/la {clave} del producto: ")
            resultados = inventario.buscar_producto(clave, valor)
            if resultados:
                for p in resultados:
                    print(p)

                print("\n1.Editar precio \t2.Editar Stock \n3.Eliminar producto \t4.Volver al menú principal")
                submenu = input("\nSeleccione una opción: ")
                if submenu == "1":
                    codigo = input("\nIngrese el código del producto a editar precio: ")
                    try:
                        if not any(p.codigo == codigo for p in resultados):
                            raise ValueError("Producto no encontrado")
                        nuevo_precio = float(input("Nuevo precio: Q."))
                        inventario.actualizar_precio(codigo, nuevo_precio)
                        print("Producto actualizado correctamente")
                    except ValueError as e:
                        print("Ha ocurrido un error: ", e)
                elif submenu == "2":
                    codigo = input("\nIngrese el código del producto a editar stock: ")
                    try:
                        if not any(p.codigo == codigo for p in resultados):
                            raise ValueError("Producto no encontrado")
                        nuevo_stock = int(input("Nuevo stock: "))
                        inventario.actualizar_stock(codigo, nuevo_stock)
                        print("Stock actualizado correctamente")
                    except ValueError as e:
                        print("Ha ocurrido un error: ", e)
                elif submenu == "3":
                    codigo = input("\nIngrese el código del producto a eliminar: ")
                    try:
                        if not any(p.codigo == codigo for p in resultados):
                            raise ValueError("Producto no encontrado")
                        inventario.eliminar_producto(codigo)
                        print("Producto eliminado correctamente")
                    except ValueError as e:
                        print("Ha ocurrido un error: ", e)
                elif submenu != "4":
                    print("Opción no válida")
                print("Regresando al menú")
            else:
                print("No se encontraron productos")

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion inválida. Intentelo nuevamente. ")


menu()
