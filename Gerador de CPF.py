import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)
num4 = random.randint(0, 9)
num5 = random.randint(0, 9)
num6 = random.randint(0, 9)
num7 = random.randint(0, 9)
num8 = random.randint(0, 9)
num9 = random.randint(0, 9)

cpf = (str(num1) + str(num2) + str(num3) + "." + str(num4) + str(num5) + str(num6) + '.' + str(num7) + str(num8) + str(num9)) 

primeiro_verificador_resto = (((num1 * 10) + (num2 * 9) + (num3 * 8) + (num4 * 7) + (num5 * 6) + (num6 * 5) + (num7 * 4) + (num8 * 3) + (num9 * 2)) % 11)

if primeiro_verificador_resto <= 1:
    primeiro_verificador_final = 0
else:
    primeiro_verificador_final = 11 - primeiro_verificador_resto

segundo_verificador_resto = (((num1 * 11) + (num2 * 10) + (num3 * 9) + (num4 * 8) + (num5 * 7) + (num6 * 6) + (num7 * 5) + (num8 * 4) + (num9 * 3)) % 11)

segundo_verificador_final = 11 - segundo_verificador_resto

if segundo_verificador_final >= 10:
    segundo_verificador_final = 0




print("Seu CPF gerado é: " + str(cpf) + "-" + str(primeiro_verificador_final) + str(segundo_verificador_final))