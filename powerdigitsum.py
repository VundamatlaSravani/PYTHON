pow = 2 ** 1000
sum = 0
rem = 0
while pow > 0:
      rem = pow % 10
      sum +=  rem
      pow = pow // 10
print("sum is:",sum)
