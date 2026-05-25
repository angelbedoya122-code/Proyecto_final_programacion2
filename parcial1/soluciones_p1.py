def f1(f, a, b):
    L1 = []
    for i in range(a, b+1):
        L1.append(f(i)*i)
    return sum(L1)

def f2(L):
    def evaluar(n):
        L2 = []
        for i in range(len(L)):
            L2.append(n**i)
        L3 = [x[0]*x[1] for x in list(zip(L, L2))]
        return sum(L3)
    return evaluar

def f3(x0, y0):
    def recta(x):
        return 2 * (x - x0) + y0  
    def paralela(x):
        return 2 * (x - 1) + 1 
    return recta, paralela

def f4(L):
    L = [x for x in L if x > 10 and (int(str(x)[0]) + int(str(x)[-1])) % 2 == 0]
    return sum(L)