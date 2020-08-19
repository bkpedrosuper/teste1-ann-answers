# uma função qualquer
import math

def f(x):
    return x**3+x**2 + 0.001
    
    # return math.log(x)+x**2

# método da bisseção
m=0
a, b = [-2, 4]
n = 10 # número de iterações
print("O número de iterações é", n)
for i in range(n):
    m = (a + b) / 2
    if f(m) == 0:
        print('A raiz é:', m)
    elif f(a) * f(m) < 0: # teorema de Bolzano
        b = m
    else:
        a = m
    print(i, m, f(m))
print("a raiz mais próxima encontrada foi", m)
