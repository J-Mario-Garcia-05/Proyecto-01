class Ordenador:
    def quick_sort(lista,clave):
        if len(lista) <= 1:
            return lista

    def obtener_valor(producto):
        if clave == "nombre":
            return producto.nombre
        elif clave == "precio":
            return producto.precio
        elif clave == "stock":
            return producto.stock
        else:
            return None

        pivote = obtener_valor(lista[0])
        if pivote is None:
            print("Error: la clave del orden inválido.")
            return lista

        menores = [x for x in lista[1:] if obtener_valor(x) < pivote]
        iguales = [x for x in lista if obtener_valor(x) == pivote]
        mayores = [x for x in lista [1:] if obtener_valor(x) > pivote]
        return Ordenador.quick_sort(menores, clave) + iguales + Ordenador.quick_sort(mayores, clave)

    #la funcion listar productos iria adentro de la clase inventario ya que es allí donde se van a mostrar los productos
    def listar_productos(self, clave_orden = "nombre"):
        lista = list(self.productos.values())
        if not lista:
            print("No hay productos en el invenario para mostra.")
            return
        lista_ordenada = Ordenador.quick_sort(lista, clave_orden)
        for p in lista_ordenada:
            print(f"{p.codigo} - {p.nombre} - {p.categoria} - Q{p.precio} - Stock: {p.stock}")