import sys
from antlr4 import *
from FiboLexer import FiboLexer
from FiboParser import FiboParser
from FiboListener import FiboListener

# Función para generar la secuencia completa de Fibonacci hasta n
def generar_secuencia_fibo(n):
    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(str(a))
        a, b = b, a + b
    return ", ".join(secuencia)

# Clase que reacciona a la gramática
class MyFiboListener(FiboListener):
    def exitExpr(self, ctx):
        # Extraer el número n de FIBO(n)
        n_str = ctx.INT().getText()
        n = int(n_str)
        
        # Generar e imprimir la secuencia como pide el parcial
        resultado_secuencia = generar_secuencia_fibo(n)
        print(f"\nEntrada: FIBO({n})")
        print(f"Salida: {resultado_secuencia}")

def main():
    print("--- Intérprete ANTLR para Secuencia Fibonacci ---")
    print("Escribe FIBO(n) y presiona Enter, luego Ctrl+D:")

    # Leer de la consola
    input_stream = StdinStream()
    
    # Procesamiento ANTLR
    lexer = FiboLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = FiboParser(token_stream)
    tree = parser.prog()

    # Caminar por el árbol
    walker = ParseTreeWalker()
    listener = MyFiboListener()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()