import numpy as np


def linear(x, k: float = 1, b: float = 0) -> tuple:
    if k == 1:
        if b == 0:
            text = fr'$y = x$'
        else:
            text = fr'$y = x + {b}$'
    else:
        if b == 0:
            text = fr'$y = {k}x$'
        else:
            text = fr'$y = {k}x + {{{b}}}$'

    return k * x + b, text


def absolute(x, k: float = 1, b: float = 0) -> tuple:
    if k == 1:
        if b == 0:
            text = fr'$y = |x|$'
        else:
            text = fr'$y = |x| + {b}$'
    else:
        if b == 0:
            text = fr'$y = {k}|x|$'
        else:
            text = fr'$y = {k}|x| + {b}$'
    return k * abs(x) + b, text


def parabola(x, k: float = 1, b: float = 0) -> tuple:
    if k == 1:
        if b == 0:
            text = fr'$y = x^2$'
        else:
            text = fr'$y = x^2 + {b}$'
    else:
        if b == 0:
            text = fr'$y = {k}x^2$'
        else:
            text = fr'$y = {k}x^2 + {b}$'
    return k * x * x + b, text


def hyperbola(x, k: float = 1, b: float = 0) -> tuple:
    if k == 1:
        if b == 0:
            text = fr'$y = \dfrac{{1}}{{x}}$'
        else:
            text = fr'$y = \dfrac{{1}}{{x}} + {b}$'
    else:
        if b == 0:
            text = fr'$y = \dfrac{{{k}}}{{x}}$'
        else:
            text = fr'$y = \dfrac{{{k}}}{{x}} + {b}$'
    return k / x + b, text


def sinus(x, a: float = 1, b: float = 1) -> tuple:
    if a == 1:
        if b == 1:
            text = fr'$y = \sin(x)$'
        else:
            text = fr'$y = \sin({b}x)$'
    else:
        if b == 1:
            text = fr'$y = {a}\sin(x)$'
        else:
            text = fr'$y = {a}\sin({b}x)$'
    return a * np.sin(b * x), text


def cosine(x, a: float = 1, b: float = 1) -> tuple:
    if a == 1:
        if b == 1:
            text = fr'$y = \cos(x)$'
        else:
            text = fr'$y = \cos({b}x)$'
    else:
        if b == 1:
            text = fr'$y = {a}\cos(x)$'
        else:
            text = fr'$y = {a}\cos({b}x)$'
    return a * np.cos(b * x), text


def tangent(x, a: float = 1, b: float = 1, c: float = 1, d: float = 0) -> tuple:
    if a == 1:
        if b == 1:
            text = fr'$y = \tan(x)$'
        else:
            text = fr'$y = \tan({b}x)$'
    else:
        if b == 1:
            text = fr'$y = {a}\tan(x)$'
        else:
            text = fr'$y = {a}\tan({b}x)$'
    return a * np.tan(b * x - c) + d, text
