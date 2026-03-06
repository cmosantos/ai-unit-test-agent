def soma(a, b):
    """
    Returns the sum of two numbers
    """
    return a + b


def subtracao(a, b):
    """
    Returns the subtraction of two numbers
    """
    return a - b


def divisao(a, b):
    """
    Returns the division of two numbers
    Raises an error if the divisor is zero
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
