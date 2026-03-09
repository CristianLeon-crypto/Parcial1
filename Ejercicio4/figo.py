import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    n = 40
    print(f"Calculando Fibonacci de {n} en Python...")
    inicio = time.time()
    resultado = fibonacci(n)
    fin = time.time()
    print(f"Resultado: {resultado}")
    print(f"Tiempo medido internamente: {fin - inicio:.4f} segundos")