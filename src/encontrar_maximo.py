def encontrar_maximo(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    return max(lista)

def encontrar_minimo(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    return min(lista)

def calcular_promedio(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    return sum(lista) / len(lista)
