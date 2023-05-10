import numpy as np


class Canvas:

    def __init__(self, n):
        self.N = n


A = Canvas(10)
s = (A.N,A.N)
print(np.zeros(s))