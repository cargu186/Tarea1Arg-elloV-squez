import math

def multiple_op(X):
    resultado = [0, 0, 0]
    ERROR_BAD_ARGUMENTS = 0xA0

    if type(X) == int and X >= 0:
        resultado[0] = X * X
        resultado[1] = 2**X
        resultado[2] = math.factorial(X)
        return resultado

    else:
        print("El dato ingresado no es valido")
        return ERROR_BAD_ARGUMENTS
