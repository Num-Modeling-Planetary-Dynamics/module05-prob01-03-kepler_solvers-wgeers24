# Using Danby's method
import numpy as np
import sympy as sym

M = 5 * (np.pi) / 180
E = [M]
e = 0.100


def f(E):
    return E - e * np.sin(E) - M


def fP(E):
    return 1 - e * np.cos(E)


def fP2(E):
    return e * np.sin(E)


def fP3(E):
    return e * np.cos(E)


def D1(E):
    return -(f(E)) / (fP(E))


def D2(E):
    return -(f(E)) / (fP(E) + 0.5 * (D1(E) * fP2(E)))


def D3(E):
    return -(f(E)) / (fP(E) + 0.5 * (D2(E) * fP2(E)) + (1 / 6) * ((D2(E) ** 2) * fP3(E)))


while True:
    Enew = E[-1] + D3(E[-1])
    E.append(Enew)
    if np.abs(E[-1] - E[-2]) < 0.000001 * (np.pi / 180):
        break
with open("../data/module05-prob03-output.csv", "w") as f:
    for Eval in E:
        f.write(f"{Eval}\n")
        print(Eval)
