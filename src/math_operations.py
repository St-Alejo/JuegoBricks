# math_operations.py
def add(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

def subtract(a, b):
    """Resta dos números y devuelve el resultado."""
    return a - b

def multiply(a, b):
    """Multiplica dos números y devuelve el resultado."""
    return a * b

# src/math_operations.py
def divide(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

