import numpy as np


def spiral(t, k: float = 1) -> tuple:
    if k == 1:
        text = rf'$ \rho = \varphi$'
    else:
        text = rf'$ \rho = {k}\varphi$'
    return t * k, text


def rose(t, a: float = 1, n: float = 1, d: float = 1) -> tuple:
    if a == 1:
        if n == d:
            text = fr'$\rho = sin(\varphi)$'
        else:
            text = fr'$\rho = sin\left(\dfrac{{{n}}}{{{d}}}\varphi\right)$'
    else:
        if n == d:
            text = fr'$\rho = {a} sin(\varphi)$'
        else:
            text = fr'$\rho = {a} sin\left(\dfrac{{{n}}}{{{d}}}\varphi\right)$'
    return a * np.sin((n / d) * t), text


def cardioid(t, a: float = 1) -> tuple:
    a *= 2
    if a == 1:
        text = rf'$ \rho = {a} (1 - cos(\varphi))$'
    else:
        text = rf'$ \rho = {a}(1 - cos(\varphi))$'
    return 2 * a * (1 - np.cos(t)), text
