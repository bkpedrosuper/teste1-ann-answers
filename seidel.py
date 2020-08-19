E = [[3,1,1,1], [1,-4,2,3], [1,-3,5,-1]] # matrix estendida do sistema
# 4x+y+z=6 --> x = (6 - y - z) / 4
# 2x+5y+2z=3 --> y = (3 - 2x - 2z) / 5
# x+2y+4z=11 --> z = (11 - x - 2y) / 4
row = 3
col = 4
def test(matrix, vec):
    err = []
    for row in matrix:
        prod = abs(sum([col * vec for col, vec in zip(row[:-1], vec)]) - row[-1])
        err.append(prod)
    return err

n  = 10
itr = {}
chute = [0,0,0]
print ("{")
for i in range(row):
    for j in range(col):
        if(j==row):
            print(" = ", E[i][j])
        else:
            print (E[i][j], " ", end="")
print("}")
print("Chute inicial", *chute)
print("Número de iterações usado:",n)
for i in range(n):
    xn = []
    for j, row in enumerate(E):
        chute = xn + chute[len(xn):] # this line updates chute
        subs = sum([el * chute[k] for k, el in enumerate(row[:-1]) if k != j])
        subs = (row[-1] - subs) / row[j]
        xn.append(subs)
    print(i, xn, test(E, xn))
    chute = xn
print("Solução:",chute)

