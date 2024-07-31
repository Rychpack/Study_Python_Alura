# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

number = int(input('Digite um número para a multiplicação: '))
for operator in range(1,11):
    mult = number * operator
    print(f'{number} x {operator} = {mult}')    