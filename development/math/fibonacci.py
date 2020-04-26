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


def fib1(n):
    if n <= 1: return n
    return fib1(n - 1) + fib1(n - 2)


def fib2(n, cache=None):
    if cache is None:
        cache = [-1] * (n + 1)
        cache[0], cache[1] = 0, 1

    if cache[n] != -1:
        return cache[n]

    cache[n] = fib2(n - 1, cache) + fib2(n - 2, cache)

    return cache[n]


def fib3(n):
    if n <= 1: return n

    a, b = 0, 1

    for _ in range(n - 1):
        a, b = b, a + b

    return b
