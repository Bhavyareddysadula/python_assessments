""" Question-5:

from pkg.poly import Poly 
a = Poly(1,2,3)  #an, ...., a0 
b = Poly(1,0,1,1,2,3)
c = a+b 
print(c) #Poly ( 1,0,1, 2,4,6)"""

class Poly:
    def __init__(self, *coeffs):
        self.coeffs = list(coeffs)
        
    def __add__(self, b_poly):
        res = b_poly.coeffs[:]
        for e in range(1, len(self.coeffs)+1):
            res[-e] += self.coeffs[-e]    
        return Poly(*res)
    
    def __str__(self):
        for e in range(len(self.coeffs)):
                print(self.coeffs[e], end = "")
                if e != len(self.coeffs)-1:
                    print(",", end = "")
        return ""
        
a = Poly(1,2,3)  
b = Poly(1,0,1,1,2,3)
c = a+b 
print(c)     