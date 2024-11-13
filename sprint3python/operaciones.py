"""Así se comenta en python, con 3 comillas dobles."""

def suma(a, b):
    return a + b
"""Esto realiza la suma de dos números"""

def resta(a, b):
    return a - b
"""Esto realiza la resta de dos números"""

def multiplicacion(a, b):
    return a * b
"""Esto realiza la multiplicación de dos números"""

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    else:
        return a / b
"""Esto realiza la división de dos números, controlando la división entre 0"""
