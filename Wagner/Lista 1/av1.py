# QUESTÃO 1
#num = int(input("Digite um número: "))
#if (num % 2 == 0):
#    print("É par")
#else:
#    print("É Ímpar")

# QUESTÃO 2
# num1 = int(input("Digite o número 1: "))
# num2 = int(input("Digite o número 2: "))
# if (num1 > num2):
#     print(f"O número {num1} é maior que o número {num2}")
# elif (num2 > num1):
#     print(f"O número {num2} é maior que o número {num1}")
# else:
#     print("Os dois números são iguais")

# QUESTÃO 3
# letra = input("Digite uma letra: ")
# if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
#     print("É vogal")
# else:
#     print("É consoante")

# QUESTÃO 4
# nota1 = float(input("Digite nota 1: "))
# nota2 = float(input("Digite nota 2: "))
# media = (nota1 + nota2) / 2
# if (media == 10):
#     print("Aprovado com Distinção")
# elif (media >= 7):
#     print("Aprovado")
# elif (media < 7):
#     print("Reprovado")

# QUESTÃO 5
# num1 = float(input("Digite o num1: "))
# num2 = float(input("Digite o num2: "))
# num3 = float(input("Digite o num3: "))
# if (num1 > num2 and num1 > num3):
#     print(f"{num1} é o maior")
# elif (num2 > num1 and num2 > num3):
#     print(f"{num2} é o maior")
# elif (num3 > num1 and num3 > num2):
#     print(f"{num3} é o maior")
# elif (num1 == num2 == num3):
#     print(f"Todos iguais")

# QUESTÃO 6
# turno = input("Digite o turno que vc estuda\nM - Matutino\nV - Vespertino\nN - Noturno\nResposta: ").upper()
# match (turno):
#     case 'M':
#         print("Bom dia")
#     case 'V':
#         print("Boa tarde")
#     case 'N':
#         print("Boa noite")
#     case _:
#         print("Valor inválido")

# QUESTÃO 7
# print("Responda com\n's' para SIM\n'n' para NÃO\n")
# resposta = 0
# tele = input("Telefonou para a vítima?: ")
# if (tele == 's'):
#     resposta = resposta + 1
# local = input("Esteve no local?: ")
# if (local == 's'):
#     resposta = resposta + 1
# mora = input("Mora perto da vítima?: ")
# if (mora == 's'):
#     resposta = resposta + 1
# devia = input("Devia para a vítima?: ")
# if (devia == 's'):
#     resposta = resposta + 1
# trabalho = input("Já trabalhou com a vítima?: ")
# if (trabalho == 's'):
#     resposta = resposta + 1

# if (resposta < 1):
#     print("Inocente")
# elif (resposta <= 2):
#     print("Suspeito")
# elif (resposta == 3 or resposta == 4):
#     print("Cúmplice")
# elif (resposta == 5):
#     print("Assasino")