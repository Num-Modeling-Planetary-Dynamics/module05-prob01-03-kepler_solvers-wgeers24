#Using Danby's method
import numpy as np
import sympy as sym

M = 5 * (np.pi) / 180
E = [M]
e = 0.100


def f(E):
    return E - e * np.sin(E) - M


def fP(E):
    return 1 - e * np.cos(E)


while True:
    Enew = E[-1] - ((f(E)[-1]) / (fP(E)[-1]))
    E.append(Enew)
    if np.abs(E[-1] - E[-2]) < 0.000001 * (np.pi / 180):
        break
with open("../data/module05-prob03-output.csv", "w") as f:
    for Eval in E:
        f.write(f"{Eval}\n")
        print(Eval)