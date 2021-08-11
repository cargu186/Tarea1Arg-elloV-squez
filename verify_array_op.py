from multiple_op import multiple_op


def verify_array_op(arrayN):
    resultado = []
    ERROR_BAD_ARGUMENTS = 0xA0

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
