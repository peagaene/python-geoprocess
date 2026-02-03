# SEGUNDA — Listas (append / pop / remove / sort)
# Exercício 1 — Lista vazia

# Crie uma lista vazia e:

# adicione 5 itens digitados pelo usuário
# imprima a lista completa

# Exercício 2 — Remoção por valor

# Dada uma lista de nomes:

# peça um nome ao usuário
# remova esse nome da lista (se existir)
# imprima a lista final

# Exercício 3 — Remoção por posição

# Dada uma lista com pelo menos 5 itens:

# remova o último item
# remova o item da posição 2
# imprima a lista

# Exercício 4 — Ordenação

# Crie uma lista de números digitados pelo usuário e:

# ordene em ordem crescente
# ordene em ordem decrescente
# imprima os dois resultados

# Exercício 5 — Verificação

# Peça um item ao usuário e:

# verifique se ele está na lista
# informe se encontrou ou não

# 1) Cadastro e resumo de pessoas (CRUD simples)

# Objetivo: praticar dict + lista + funções + validação.

# Regras

# Cadastre N pessoas (nome, idade, cidade).

# Idade deve ser int >= 0.

# Pare quando o usuário digitar fim no nome.

# Saídas

# Total de pessoas

# Média de idade

# Pessoa mais velha (nome e idade)

# Quantas cidades diferentes (use set)

# Obrigatório

# Funções: ler_nome(), ler_idade(), ler_cidade(), resumo(pessoas)

# Estrutura: pessoas = [ {"nome":..., "idade":..., "cidade":...}, ... ]

# 2) Caixa de supermercado (itens + subtotal + desconto)

# Regras

# Ler itens até fim: nome do item, preço, quantidade.

# Preço pode vir com vírgula ou ponto ("10,50" ou "10.50") → converter.

# Se total > 200: desconto 10%. Se > 500: desconto 15%.

# Saídas

# Total bruto, desconto, total final

# Item mais caro

# Lista dos itens com quantidade >= 3

# Obrigatório

# Usar try/except e while para validação

# Usar dict para cada item e lista para o carrinho

# 3) Validador de senha com regras configuráveis

# Regras de senha

# mínimo 8 caracteres

# pelo menos 1 número

# pelo menos 1 letra maiúscula

# pelo menos 1 caractere especial !@#$%

# Saídas

# “Senha OK” ou lista de erros encontrados

# Obrigatório

# Função validar_senha(senha) -> (bool, lista_erros)

# Use loops e condicionais

# Use set para testar especiais de forma rápida

# 4) Analisador de texto (estatísticas)

# Entrada

# Texto digitado pelo usuário (uma linha)

# Saídas

# Quantas palavras

# Quantos caracteres (com e sem espaços)

# As 5 palavras mais frequentes (use dict)

# Palavras únicas em ordem alfabética (use set + sorted)

# Obrigatório

# Normalizar: lower(), remover pontuação simples . , ; : ! ? (pode usar replace em loop)

# 5) Jogo “Adivinhe o número” com níveis

# Regras

# Usuário escolhe nível: 1 (1–10, 5 tentativas), 2 (1–50, 7 tentativas), 3 (1–100, 10 tentativas)

# A cada palpite, dizer “maior/menor”

# Se digitar algo inválido, não perde tentativa

# Obrigatório

# Função ler_inteiro(mensagem, min, max)

# Use while e try/except

# 6) Conversor de unidades (menu com funções)

# Menu

# km → m

# m → km

# °C → °F

# °F → °C

# sair

# Regras

# Não pode quebrar com input inválido

# Aceita números com vírgula/ponto

# Obrigatório

# Uma função por conversão

# Função ler_float() robusta

# Loop principal while True

# 7) Controle de estoque (dict de dict)

# Estrutura sugerida
# estoque = { "ARROZ": {"qtd": 10, "preco": 5.50}, ... }

# Menu

# adicionar produto

# atualizar quantidade

# atualizar preço

# vender (baixa qtd)

# relatório (valor total do estoque e itens em falta)

# sair

# Obrigatório

# Produto guardado em maiúsculo (type casting/string)

# Vender não pode deixar negativo (condicionais)

# Relatório usa loops + soma

# 8) Notas dos alunos com tuplas (imutabilidade)

# Regras

# Para cada aluno: nome + 3 notas

# Guarde as notas em uma tupla (ex: (7.5, 8.0, 6.0))

# Calcular média e situação:

# média >= 7: aprovado

# 5 <= média < 7: recuperação

# < 5: reprovado

# Saídas

# Lista de alunos e situação

# Melhor média e pior média

# Quantos em cada situação (use dict contador)

# 9) Deduplicador e comparador de listas (set na veia)

# Entrada

# Duas listas de números (o usuário digita números separados por espaço)

# Saídas

# Lista A sem repetidos

# Lista B sem repetidos

# Interseção (comuns)

# Diferença A - B

# Diferença B - A

# União

# Obrigatório

# Converter strings → int com validação

# Usar set e depois voltar para lista ordenada

# 10) Mini “ETL” de dados (limpar, validar, resumir)

# Entrada

# Usuário digita linhas no formato: nome,idade,salario

# Ex: Ana,30,4500,50 (pode vir com vírgula no salário ou espaços extras)

# Para quando digitar fim

# Validações

# nome não vazio

# idade int entre 0 e 120

# salário float > 0

# Saídas

# Quantos registros válidos e inválidos

# Média salarial

# Maior salário (nome e valor)

# Lista de nomes únicos (set)

# Obrigatório

# Função parse_linha(linha) -> dict ou None

# Guardar válidos em lista de dicts


def ler_nome():
    while True:
        nome = input('Digite seu nome: ').strip()

        if nome.isalpha():
            return nome
        else:
            print('Erro: digite apenas letras.')

def ler_idade():
    while True:
        try:
            idade = int(input('Digite sua idade: ').strip())
            if idade >= 0:
                return idade
            else:
                print('Erro: digite uma idade maior ou igual 0.')
        except ValueError:
            print("Erro: digite um valor inteiro.")

def ler_cidade():
    while True:
        cidade = input('Digite sua cidade: ').strip()

        if cidade.isalpha():
            return cidade
        else:
            print('Erro: digite apenas letras.')

CRUD = []

while True:
    print('\nCadastro de pessoa (digite "fim" no nome para encerrar)')
    nome = ler_nome()
    if nome.lower() == 'fim':
        break 
    idade = ler_idade()
    cidade = ler_cidade()  
    pessoa = {'nome': nome, 'idade': idade, 'cidade': cidade}
    CRUD.append(pessoa)

print(CRUD)