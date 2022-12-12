multi= 5 * 0.6
multi2= 9.81*0.6**2

from fractions import Fraction
result= multi - Fraction (1,2) * multi2

print("O resultado da operação 5 x 0,6 - 1/2 x 9,81 x 0,6^2 é = ",result)

#segundo jeito 

print ("O resultado da operação é", 5*0.6-1/2*9.81*0.6**2)