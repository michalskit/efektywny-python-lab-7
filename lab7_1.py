# Zadanie 1

# Przygotuj demo programu znajdującego miejsca zerowe metodą Newtona. Program powinien 
# obsługiwać następujące opcje:

# - ustalanie punktu startowego,
# - wielkość kroku w pochodnej,
# - ilość kroków metody,
# - dokładność,
# - pomoc.

# Program powinien zwrócić jedno miejsce zerowe fukcji w zależności od punktu startowego.
# na przykład:
# python lab7_1.py "x**2 - 3*x + 2" -x0 3 -max_iter 100 -tolerance 0.00001
# Found root: 2.0
# python lab7_1.py "x**2 - 3*x + 2" -x0 0 -max_iter 100 -tolerance 0.00001
# Found root: 1.0



import argparse
import math


def derivative(f, h=1e-6):
    """
    Zwraca pochodną funkcji w punkcie, wg. wzoru f'(x) = [f(x+h) - f(x)]/h, 
    gdzie h jest parametrem dekoratora, jeśli nie zostanie podany, należy przyjąć 1000 * epsilon maszynowy
    """
    pass


def newton_method(f, x0, h, max_iter, tolerance):
    """
    Implementacja metody Newtona do znajdowania miejsc zerowych funkcji.
    Tutaj należy umieścić implementację metody.
    Znalezione miejsce zerowe powinno być zaokrąglone do wartości tolerance.
    """
    pass


def parse_expression(expr):
    """
    Parses a mathematical expression and returns a function that evaluates
    the expression for a given x.
    """
    allowed_chars = set("0123456789+-*/(). x")
    if not set(expr).issubset(allowed_chars):
        raise ValueError("Invalid characters in expression")

    return eval("lambda x: " + expr)


def parse_arguments():
    """
    Parsowanie argumentów z linii komend. Tutaj należy umieścić kod odpowiedzialny
    za parsowanie argumentów.
    """
    pass


if __name__ == "__main__":
    args = parse_arguments()

    f_str = args.function
    h = args.step
    x0 = args.initial
    max_iter = args.iterations
    tolerance = args.tolerance

    f = parse_expression(f_str)
    df = derivative(f, h)

    try:
        pass