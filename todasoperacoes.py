# Programa Calculadora com IF-ELIF-ElSE
# 10/03/2026

op = input("Digite 1-SOMA ou 2-SUBTRAÇÃO ou 3-MULTIPLICAÇÃO OU 4-DIVISÃO OU 5-POTENCIAÇÃO OU 6-RADICIACAO")
op = int(op)

a = input("Entre com o 1º número")
a = int(a)

b = input("Entre com o 2º número")
b = int(b)

if (op == 1): 
    print(a + b)
elif (op == 2):
    print(a - b)
elif (op == 3):
    print(a * b)
elif (op == 4):
    print(a ** b)
elif (op == 5):
    print(a / b)
elif (op == 6):
    print(a ** 1/2)

else: 
    print("Digite uma opção valida")
    
    
    
    
    
    
input()
    
  