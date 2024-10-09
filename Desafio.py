def gerar_fibonacci(limite):
    fibonacci = [0, 1]
    while fibonacci[-1] < limite:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def pertence_a_fibonacci(numero, sequencia):
    return numero in sequencia

numero_informado = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

sequencia_fibonacci = gerar_fibonacci(numero_informado)

if pertence_a_fibonacci(numero_informado, sequencia_fibonacci):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")