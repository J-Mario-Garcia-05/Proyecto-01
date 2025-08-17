class Ordenador:
    def quick_sort(lista,clave):
        if len(lista) <= 1:
            return lista

        menores = [x for x in lista[1:] if obtener_valor(x) < pivote]
        iguales = [x for x in lista if obtener_valor(x) == pivote]
        mayores = [x for x in lista [1:] if obtener_valor(x) > pivote]
        return Ordenador.quick_sort(menores, clave) + iguales + Ordenador.quick_sort(mayores, clave)

class Buscador:
    def buscar (lista,clave, valor):
        resultados = []
        for producto in lista:
            if clave == "código" and producto.codigo == valor:
                resultados.append(producto)
            elif clave == "nombre" and valor in producto.nombre:
                resultados.append(producto)
            elif clave == "categoria" and valor in producto.categoria:
                resultados.append(producto)
        return resultados

        def buscar_productos(lista,clave,valor):
            lista = list(self.productos.values())
            if not lista:
                print("No hay productos en el inventario. ")
                return

            resultado = Buscador.buscar(lista,clave,valor)
            if resultados:
                for p in resultados:
                    print(f"{p.codgio} - {p.nombre} - {p.categoria} - Q{p.precio} - {p.stock}")
            else:
                print("No se encontraron productos. ")

    #la funcion listar productos iria adentro de la clase inventario ya que es allí donde se van a mostrar los productos hice la funcion de agregar producto para ver lo de la funcion listar producto

    def agregar_producto(self,producto):
            if producto.codigo in self. productos:
                print("El código ya existe dentro del inventario. ")
            else:
                self.productos[producto.codigo] = producto

    def listar_productos(self, clave="nombre"):
        lista = list(self.productos.values())
        if not lista:
            print("No hay productos en el invenario para mostrar.")
            return
        lista_ordenada = Ordenador.quick_sort(lista, clave_orden)
        for p in lista_ordenada:
            print(f"{p.codigo} - {p.nombre} - {p.categoria} - Q{p.precio} - Stock: {p.stock}")

#MENU
def menu():
    invenario = Inventario()

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
                precio = float(input("Precio del producto: "))
                stock = int(input("Stock del producto: "))
            except ValueError:
                print("Precio o stock invalido. Intentelo de nuevo.")
                continue
            producto = Productos(codigo, nombre, categoria, precio, stock)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            print("\nOrdenar por: nombre, precio o stock")
            clave = input("Ingrese la clave para ordenar: ")
            if clave not in ["nombre", "precio", "stock"]:
                clave = "nombre"
            inventario.listar_productos(clave)

        elif opcion == "3":
            print("\nBuscar por: código, nombre, categoria")
            clave = input("Ingrese la clave de búsqueda:")
            valor = input("Ingrese el valor a buscar: ")
            inventario.buscar_producto(clave, valor)

        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion inválida. Intentelo nuevamente. ")

menu ()

