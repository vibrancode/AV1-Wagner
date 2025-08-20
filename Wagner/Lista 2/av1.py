# QUESTÃO 1
# fibonacci_serie = [0, 1]
# while fibonacci_serie[-1] <= 500:
#     a = fibonacci_serie[-2]
#     b = fibonacci_serie[-1]
#     proximo_numero = a + b
#     fibonacci_serie.append(proximo_numero)
# print(fibonacci_serie)

# QUESTÃO 2
# num = int(input("Digite quantos números: "))
# numeros = []
# for i in range(num):
#     num = float(input(f"Digite o {i+1} número: "))
#     numeros.append(num)
# numeros.sort()
# print(numeros)
# print(f"O menor número é {numeros[0]}")
# print(f"O maior número é {numeros [-1]}")
# print(f"A soma dos valores é {numeros[0] + numeros[-1]}")

# QUESTÃO 3
# num = int(input("Digite quantos números: "))
# while (num <= 0) or (num > 1000):
#     num = int(input("Digite quantos números: "))
#     continue
# numeros = []
# for i in range(num):
#     num = float(input(f"Digite o {i+1} número: "))
#     numeros.append(num)
# numeros.sort()
# print(f"O menor número é {numeros[0]}")
# print(f"O maior número é {numeros [-1]}")
# if (numeros[0] == numeros[-1]):
#     print("Os dois números são iguais")
# else:
#     print(f"A soma dos valores é {numeros[0] + numeros[-1]}")

# QUESTÃO 4
# nome = input("Digite seu nome: ")
# while len(nome) <= 3:
#     print("Nome inválido! O nome deve ter mais de 3 caracteres.")
#     nome = input("Digite seu nome novamente: ")
# idade = int(input("Idade: "))
# while (idade <= 0) or (idade > 150):
#     print("Idade inválida, digita idade deve ser entre 0 e 150")
#     idade = input("Digite sua idade: ")
# salario = float(input("Salário: "))
# while (salario <= 0):
#     print("Inválido")
#     salario = input("Digite seu salário: ")
# sexo = input("Sexo: ").lower()
# while sexo not in ('m', 'f'): 
#     print("Inválido: Digite 'm' ou 'f'")
#     sexo = input("Sexo: ")
# estado_civil = input("Estado civil: ['S', 'C', 'V', 'D']: ").upper()
# while estado_civil not in ('S', 'C', 'V', 'D'):
#     print("Inválido: Digite 'S', 'C', 'V' ou 'D'")
#     estado_civil = input("Estado civil: ")
# print(f"nome: {nome}\nIdade: {idade}\nSalário: {salario}\nSexo: {sexo}\nEstado Civil: {estado_civil}")

# QUESTÃO 5 
# numero = int(input("Digite um número inteiro: "))
# if numero <= 1:
#     print(f"{numero} não é um número primo.")
# elif numero == 2:
#     print(f"{numero} é um número primo.")
# else:
#     eh_primo = True
#     for i in range(2, numero):
#         if numero % i == 0:
#             eh_primo = False
#             break           
#     if eh_primo:
#         print(f"{numero} é um número primo.")
#     else:
#         print(f"{numero} não é um número primo.")