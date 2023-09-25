def facto(n):
    if n<2:
        return 1
    else:
        return n*facto(n-1)
n=int(input("Ingrese n: "))
print(facto(n))