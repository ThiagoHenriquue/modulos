# Modulo Operacoes Matematicas 
def sum(x, y ):
    return x + y

def subtra(x, y ):
    return x - y

def mult(x, y ):
    return x * y

def div(x, y ):
    if y != 0:
        return x / y
    else:
        raise ValueError("Nao e permitido divisao por 0  ")
