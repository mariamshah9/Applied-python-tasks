


import cmath
import math

AB = int(input())
BC = int(input())

if __name__ == '__main__':
   print (str(int(round(math.degrees(cmath.phase(complex(BC,AB))))))+'°')



