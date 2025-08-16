class Ordenador:
    def quick_sort(lista,campo):
        if len(lista) <= 1:
            return lista

        pivote = lista[0]
        valor_pivote = obtener_valor(pivote, campo)

        menores = [x for x in lista[1:] if obtener_valor(x, campo) < valor_pivote]
        oguales = [x for x in lista if obtener_valor(x, campo) == valor_pivote]