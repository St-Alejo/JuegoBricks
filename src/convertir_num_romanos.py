def romano_a_entero(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0

    for letra in reversed(romano):
        valor = valores[letra]
        if valor < prev:
            total -= valor
        else:
            total += valor
        prev = valor

    return total
