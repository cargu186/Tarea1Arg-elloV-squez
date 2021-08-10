from multiple_op import multiple_op


def test_funciones():
    import math
    import random
    n = random.randint(0, 100000)
    Negativo1 = "w"

    assert multiple_op(n) == [math.prod([n, n]), pow(2, n), math.factorial(n)]
    assert multiple_op(Negativo1) == 0xA0
