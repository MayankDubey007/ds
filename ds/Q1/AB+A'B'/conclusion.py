import Multiplication
import Transpose
import additionMATRiX

m1 = [[1, 2],
      [3, 4]]

m2 = [[5, 6],
      [7, 8]]
step01 = Multiplication.multiply(m1, m2)
print()
step02 = Multiplication.multiply(Transpose.trns(m1),Transpose.trns(m2))
print()

Result = additionMATRiX.ADD(step01,step02)
