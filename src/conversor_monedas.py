def convertir_a_pesos(dolares, tasa_cambio=4000):
    if dolares < 0:
        raise ValueError("La cantidad en dólares no puede ser negativa")
    return dolares * tasa_cambio
