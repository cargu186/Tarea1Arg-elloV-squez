import math
import random
from funciones import multiple_op, verify_array_op


def test_multiple_op():
    n = random.randint(0, 100000)

    assert multiple_op(n) == [math.prod([n, n]), pow(2, n), math.factorial(n)]


def test_verify_array_op():
    arrayPrueba = [0, 0, 0, 0, 0]
    arrayAssert = [0, 0, 0, 0, 0]
    for i in range(0, 5):
        n = random.randint(0, 100000)
        arrayPrueba[i] = n
        arrayAssert[i] = [math.prod([n, n]), pow(2, n), math.factorial(n)]

    assert verify_array_op(arrayPrueba) == arrayAssert


def test_multiple_op_neg_case():

    assert multiple_op("a") == 0xA0


def test_verify_array_op_neg_case():

    assert verify_array_op(["a", "b", "c", "d"]) == 0xA0
