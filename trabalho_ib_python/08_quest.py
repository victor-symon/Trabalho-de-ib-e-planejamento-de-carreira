numero1=int(input("digite o primeiro numero:  "))
numero2=int(input("digite o segundo numero:  "))
operaçao=input(" bem vindo a calculadora python, para realizar uma multiplicação digite mult,para realizar uma soma digite som,para realizar uma subtração digite sub,para realizar uma divisão digite  div.")
sub=numero1 - numero2
mult=numero1*numero2
som=numero1+numero2
div=numero1/numero1
if operaçao=="sub":
    print(f'o resultado da operação foi    {sub}' )
elif operaçao=="mult":
     print(f'o resultado da operação foi  {mult}' )
elif operaçao=="som":
    print(f'o resultado da operação foi   {som}' )
elif operaçao=="div":  
    print(f'o resultado da operação foi   {div}' )









