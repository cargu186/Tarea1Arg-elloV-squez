def multiple_op(X):
    import math
    resultado = [0, 0, 0]
    try:
        str(X).isnumeric()
        resultado[0] = X * X
        resultado[1] = 2**X
        resultado[2] = math.factorial(X)
        return resultado

    except:
        print("El dato ingresado no es valido")
        return -1
