'''
Punto 1.1
'''
def G1():
    a,b,c = 1,1,1
    while True:
        yield a
        a,b,c = b,c,a+b+c

'''
Punto 1.2
'''
def tresfibonacci(n):
    cont = 0
    a,b,c = 1,1,1
    while cont<n:
        yield a
        a,b,c = b,c,a+b+c

'''
Punto 2
'''
def f2(func):
    cont = [0]
    def wrapper(*args, **kwargs):
        while cont[0] < 3:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                cont[0] += 1
                print(f'Ha cometido {cont[0]} error(es): {type(e).__name__}')
                return None
        print("Leer la documentación")
    return wrapper

'''
Punto 3.1
'''
def f3i(n):
    digito=0
    while n//10 != 0:
        n = n//10
    digito += n
    return digito

'''
Punto 3.2
'''
def f3r(n):
    if n//10 == 0:
        return n
    return 0 + f3r(n//10)