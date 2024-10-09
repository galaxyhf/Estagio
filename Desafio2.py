texto = input("Digite uma string para verificar a quantidade de letras 'a' presentes: ")

texto_minusculo = texto.lower()

quantidade_a = texto_minusculo.count('a')

if quantidade_a > 0:
    print(f"A letra 'a' (maiúscula ou minúscula) aparece {quantidade_a} vez(es) na string informada.")
else:
    print("A letra 'a' (maiúscula ou minúscula) não aparece na string informada.")