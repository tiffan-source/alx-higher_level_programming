#!/usr/bin/python3
import calculator_1 as calcul

if __name__ == "__main__":
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, calcul.add(a, b)))
    print("{} - {} = {}".format(a, b, calcul.sub(a, b)))
    print("{} * {} = {}".format(a, b, calcul.mul(a, b)))
    print("{} / {} = {}".format(a, b, calcul.div(a, b)))
