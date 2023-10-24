def factorial(n):
    # Caso base
    if n == 0:
        return 1
    # Caso recursivo
    else:
        return n * factorial(n-1)
    
print(factorial(5))