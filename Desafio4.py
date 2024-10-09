def proximo_elemento_a():
    return 7 + 2  
def proximo_elemento_b():
    return 64 * 2  

def proximo_elemento_c():
    return 7 ** 2  

def proximo_elemento_d():
    return 10 ** 2 

def proximo_elemento_e():
    fibonacci = [1, 1, 2, 3, 5, 8]
    return fibonacci[-1] + fibonacci[-2]  # Soma dos dois números anteriores

def proximo_elemento_f():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    numero = 20
    while not is_prime(numero):
        numero += 1
    return numero

print(f"a) Próximo elemento: {proximo_elemento_a()}")
print(f"b) Próximo elemento: {proximo_elemento_b()}")
print(f"c) Próximo elemento: {proximo_elemento_c()}")
print(f"d) Próximo elemento: {proximo_elemento_d()}")
print(f"e) Próximo elemento: {proximo_elemento_e()}")
print(f"f) Próximo elemento: {proximo_elemento_f()}")