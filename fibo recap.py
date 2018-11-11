def fibo(m):
    if m == 0:
        return (0)
    if m == 1:
        return (1)
    return fibo(m - 1) + fibo(m - 2)


print(fibo(7))