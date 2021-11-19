def sumOfn(n):
    if n<=1:
        return 1
    else:
        return n + sumOfn(n-1)
# print(sumOfn(10))
def fibo(m):
    if m<=1:
        return m
    else:
        return m+(fibo(m-2)+fibo(m-3))

# fibo(13)
print(fibo(13))