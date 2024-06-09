#Peça ao usuário para inserir um número e use um loop for para imprimir a tabuada desse número (de 1 a 10).
i=int(input("digite um numero para saber sua tabuada:  "))
for numero in range(1,11):
    print(f'{numero} x {i} = {numero*i}')