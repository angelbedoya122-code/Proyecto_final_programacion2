'''Clase Polinomio'''
class Polinomio:
  def __init__(self, L):
    self.L = L

  def __str__(self):
    cad = f'{self.L[0]} '
    for i in range(1, len(self.L)):
      cad += f' + {self.L[i]}x^{i}'
    return cad

  def __add__(self, other):
    if not isinstance(other, Polinomio):
      raise TypeError("Solo se pueden sumar objetos de la clase Polinomio")

    n1 = len(self.L)
    n2 = len(other.L)
    limite_comun = min(n1, n2)
    Lsum = [self.L[i] + other.L[i] for i in range(limite_comun)]

    if n1 > n2:
      Lsum += self.L[limite_comun:]
    else:
      Lsum += other.L[limite_comun:]

    return Polinomio(Lsum)

  def __sub__(self, other):
    if not isinstance(other, Polinomio):
      raise TypeError("Solo se pueden restar objetos de la clase Polinomio")

    polinomio_negativo = Polinomio([-i for i in other.L])

    return self + polinomio_negativo

  def __mul__(self, other):
    if not isinstance(other, Polinomio):
      raise TypeError("Solo se pueden multiplicar objetos de la clase Polinomio")

    longitud_final = len(self.L) + len(other.L) - 1

    Lmul = [0]*longitud_final

    for i in range(len(self.L)):
      for j in range(len(other.L)):
        Lmul[i+j] += self.L[i] * other.L[j]

    return Polinomio(Lmul)

  def evaluar(self, x):
    result = 0
    for i in range(len(self.L)):
      result += self.L[i]*(x**i)
    return result
  
'''Clase PolinomiosDerivables'''
class PolinomiosDerivables(Polinomio):
  def derivada(self):
    derivada = []
    exp = 1
    for i in self.L[1:]:
      derivada.append(i*exp)
      exp += 1
    return PolinomiosDerivables(derivada)

  def recta_tangente(self, x0):
    polinomio_derivado = self.derivada()
    m = polinomio_derivado.evaluar(x0)

    y0 = self.evaluar(x0)

    b = y0 - (m*x0)

    return PolinomiosDerivables([b,m])

  def grado(self):
    return f'Este polinomio es de grado {len(self.L)-1}'
  
'''ejercicio cajero'''
class Cajero:
    def __init__(self, n1, n2, n5):
        self.n1 = n1
        self.n2 = n2
        self.n5 = n5

    def retiro(self, x):
        if x <= 0 or x % 10000 != 0:
            return "El retiro debe ser positivo y múltiplo de 10000"
        copia_n1 = self.n1
        copia_n2 = self.n2
        copia_n5 = self.n5
        while x != 0:
            if x >= 50000 and copia_n5 > 0:
                x -= 50000
                copia_n5 -= 1
            elif x >= 20000 and copia_n2 > 0:
                x -= 20000
                copia_n2 -= 1
            elif x >= 10000 and copia_n1 > 0:
                x -= 10000
                copia_n1 -= 1
            else:
                return "No hay billetes suficientes para realizar el retiro"
        self.n1 = copia_n1
        self.n2 = copia_n2
        self.n5 = copia_n5
        return "Retiro realizado correctamente"

    def consignacion(self, n1, n2, n5):
        self.n1 += n1
        self.n2 += n2
        self.n5 += n5
        return "Consignación realizada"

    def verificar_estado(self):
        return f"Billetes de 10000: {self.n1} Billetes de 20000: {self.n2} Billetes de 50000: {self.n5}"  