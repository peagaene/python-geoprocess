#-----------------------------------------
#Exercício 1 — Conversão simples

# Peça ao usuário:

# um número digitado como texto

# Converta esse valor para:

# inteiro
# imprima o triplo desse número

# 📌 Atenção: pense no que acontece se o usuário digitar algo inválido.

# while True:
#     numero = input("Difite um número inteiro: ")

#     try:
#         numero = int(numero)
#         break
#     except ValueError:
#         print("Erro: digite apenas números.")

# numero_int = int(numero)
# numero_triplo = numero_int*3

# print(f'O triplo do numero digita é {numero_triplo}')

#------------------------------------------

# Exercício 2 — Idade válida

# Crie um programa que:

# peça a idade do usuário

# não avance enquanto a entrada não for:

# um número inteiro

# maior ou igual a 0

# ao final, imprima:

# Idade cadastrada: X anos

# while True:
#     try:
#         idade = int(input('Digite sua idade: '))
#         if idade > 0:
#             break
#         else:
#             print('O numero deve ser maior que zero.')
#     except ValueError:
#         print("Erro: digite um numero valido.")

# print(f'Idade cadastrada: {idade} anos')

#------------------------------------------

# Exercício 2 — Cálculo com decimais

# Peça ao usuário:

# um valor em metros (texto)

# Converta para:

# número decimal (float)

# calcule e imprima o valor em centímetros

# 📌 Resultado esperado em decimal, não inteiro.

#-------------------------------------------

# Exercício 2 — Nota válida

# Crie um programa que:

# peça uma nota

# repita a pergunta enquanto:

# a entrada não for numérica

# ou o valor estiver fora do intervalo 0 a 10

# ao final, imprima:

# Nota registrada: X

# while True:
#     try:
#         nota = float(input('Qual foi sua nota? '))
#         if nota >= 0 and nota <= 10:
#             break
#         else:
#             if nota < 0:
#                 print('Digite um valor maior que zero.')
#             elif nota > 10:
#                 print('Digite um valor menor que 10. ')
#     except ValueError:
#         print("Erro: digite um numero valido.")

# print(f'Nota registrada: {nota}')

#-----------------------------------------------