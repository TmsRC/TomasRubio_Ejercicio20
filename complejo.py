import numpy as np
import cmath

class Complejo:
    def __init__(self,a,b):
        self.imaginario = b
        self.real = a
        self.norma = (a**2 + b**2)**(1/2)
    def conjugado(self):
        self.imaginario = -self.imaginario
        return self
    def calcula_norma(self):
        return self.norma
    def pow(self,p):
        z = np.power((self.real + 1j*self.imaginario),p).real
        return Complejo(z.real,z.imag)