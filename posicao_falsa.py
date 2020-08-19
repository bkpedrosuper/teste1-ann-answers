# posição pode ser mais lento que o método da bisseção
import math
# uma função qualquer
def f(x):
    return x**3+x**2 + 0.001

n = 10
chosen = 0
a, b = [1, 2]
print("O número de iterações é", n)
print("O intervalo escolhido foi [", a, ",", b, "]")
for i in range(n):
    xn = (a * f(b) - b * f(a)) / (f(b) - f(a))
    if f(xn) == 0:
        print('A raiz é:', xn)
    elif f(a) * f(xn) < 0:
        b = xn
    else:
        a = xn
    chosen = xn
    print(i, xn)

print("a raiz mais próxima encontrada foi", chosen)
