num1= float (input("Digite um número: "))
num2= float (input("Digite um outro número: "))
operador= input('Qual operador você gostaria de usar? +, -, / ou * ? ')

if operador == '+':
    soma= num1 + num2
    print("A soma é: %f" %soma)
elif operador == '-':
    subtracao= num1 - num2
    print('A subtração é: %f' %subtracao)
elif operador == '/':
    divisao = num1 / num2
    print('A divisão é: %f' %divisao)
elif operador == '*':
    multi = num1 * num2
    print('A multiplicação é: %f' %multi)
else :
   print("você não digitou nada, tente novamente")
