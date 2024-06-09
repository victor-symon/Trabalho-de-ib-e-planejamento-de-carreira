print("vamos fazer o seu cadastro")
nome=input("qual é o seu nome:  ")
idade=input("qual a sua idade:  ")
if idade < "15":
    print(f'sr.{nome} pode tirar o seu titolo eleitoral,pois esta na idade apta')
else :
    print(f'sr. {nome}  não  pode tirar o seu titolo eleitoral,pois não está na idade apta')
