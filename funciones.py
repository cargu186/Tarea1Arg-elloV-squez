import math
ERROR_BAD_ARGUMENTS = 0xA0


def multiple_op(X):
    resultado = [0, 0, 0]
    
    if type(X) == int and X >= 0:
        resultado[0] = X * X
        resultado[1] = 2**X
        resultado[2] = math.factorial(X)
        return resultado

    else:
        print("El dato ingresado no es valido")
        return ERROR_BAD_ARGUMENTS


def verify_array_op(arrayN):
    resultado = []

    if isinstance(arrayN, list):
        for n in arrayN:
            if type(n) == int and n >= 0:
                resultado.append(multiple_op(n))

            else:
                print("El array ingresado no es valido")
                resultado = ERROR_BAD_ARGUMENTS
                break
    else:
        print("No se ha ingresado un array")
        resultado = ERROR_BAD_ARGUMENTS
    
    return resultado
