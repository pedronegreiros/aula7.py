from calculadora import *

texto = float(input("digite um numero: "))
texto2 = float(input("digite um numero: "))
texto3 = float(input("qual operação deseja realizar? [1] soma [2] subtração [3] divisão [4] multiplicação: "))

if texto3 == 1:
    print(soma(num1=texto, num2=texto2))
elif texto3 == 2:
    print(subtração(num1=texto, num2=texto))
elif texto3 == 3:
    print(divisão(num1=texto, num2=texto2))
elif texto3 == 4:
    print(multiplicar(num1=texto, num2=texto2))




