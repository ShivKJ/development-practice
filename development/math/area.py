"""
author: Shiv
email: shivkj001@gmail.com
date: 4/26/20

MIT License

Copyright (c) [2018]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
from math import radians, sin, sqrt


def area_sides(a, b, c):
    """
    finds area of triangle with sides a, b and c using Heron's Formula
    https://en.wikipedia.org/wiki/Heron%27s_formula#Formulation
    :param a:
    :param b:
    :param c:
    :return: area
    """
    s = (a + b + c) / 2

    return sqrt(s * (s - a) * (s - b) * (s - c))


def area_ab_angle(a, b, theta, in_degree=True):
    """
    finds area of triangle with sides a and b and theta as angle between them
    :param a:
    :param b:
    :param theta:
    :param in_degree:
    :return:
    """
    if in_degree:
        theta = radians(theta)

    return a * b * sin(theta) / 2
