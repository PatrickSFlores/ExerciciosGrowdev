#Semana 02 - Aula 01

#Exercício 01

# Celsius p/ Fahrenheit
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f'A temperatura em Fahrenheit é: {fahrenheit}°F')


# Fahrenheit p/ Celsius
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f'A temperatura em Celsius é: {celsius}°C')



#Exercício 02

num = int(input("Digite um número inteiro: "))
if num % 2 == 0:
    print("Par")
else:
    print("Ímpar")



#Exercício 03

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
opcao = int(input("Escolha a operação: (1 adição) ou (2 subtração)"))

if opcao == 1:
    resultado = num1 + num2
    print(f'{num1} + {num2} = {resultado}')
elif opcao == 2:
    resultado = num1 - num2
    print(f'{num1} - {num2} = {resultado}')
else:
    print("Opção inválida")



#Exercício 04

nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))
nota4 = float(input("Digite a nota do 4º bimestre: "))
total_aulas = int(input("Digite o número total de aulas: "))
faltas = int(input("Digite o número de faltas: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média do aluno é {media}')

per_faltas = (faltas / total_aulas) * 100
print(f'O percentual de faltas do aluno é de {per_faltas}%')

if per_faltas > 25:
    print("Reprovado por Faltas")
elif media < 7:
    print("Reprovado por Média")
else:
    print("Aprovado")



#Exercício 05

#Situação 2(recuperação)
nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))
nota4 = float(input("Digite a nota do 4º bimestre: "))
total_aulas = int(input("Digite o número total de aulas: "))
faltas = int(input("Digite o número de faltas: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média do aluno é {media}')

per_faltas = (faltas / total_aulas) * 100
print(f'O percentual de faltas do aluno é de {per_faltas}%')

if per_faltas > 25:
    print("Reprovado por Faltas")
elif 5 <= media < 7:
    print("Recuperação")
elif media < 5:
    print("Reprovado por Média")
else:
    print("Aprovado")

#Situação 3(Média e Faltas)
nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))
nota4 = float(input("Digite a nota do 4º bimestre: "))
total_aulas = int(input("Digite o número total de aulas: "))
faltas = int(input("Digite o número de faltas: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média do aluno é {media}')

per_faltas = (faltas / total_aulas) * 100
print(f'O percentual de faltas do aluno é de {per_faltas}%')

if per_faltas > 25 and media < 7:
    print("Reprovado por Média e Faltas")
elif per_faltas > 25:
    print("Reprovado por Faltas")
elif media < 7:
    print("Reprovado por Média")
else:
    print("Aprovado")



#Exercício 06

dia = int(input("Digite um dia: "))
mes = int(input("Digite um mês: "))
ano = int(input("Digite um ano: "))

valido = True

if mes < 1 or mes > 12:
    valido = False
elif mes == 2:
    if ano % 4 == 0:
        if dia < 1 or dia > 29:
            valido = False
    elif dia < 1 or dia > 28:
        valido = False
elif mes in [4, 6, 9, 11]:
    if dia < 1 or dia > 30:
        valido = False
else:
    if dia < 1 or dia > 31:
        valido = False

if valido:
    print("Data válida")
else:
    print("Data inválida")



#Exercício 07

dia = int(input("Digite um dia: "))
mes = int(input("Digite um mês: "))
ano = int(input("Digite um ano: "))


valido = True

if mes < 1 or mes > 12:
    valido = False
elif mes == 2:
    if ano % 4 == 0:
        if dia < 1 or dia > 29:
            valido = False
    elif dia < 1 or dia > 28:
        valido = False
elif mes in [4, 6, 9, 11]:
    if dia < 1 or dia > 30:
        valido = False
else:
    if dia < 1 or dia > 31:
        valido = False


if valido:
    if mes == 2:
        if ano % 4 == 0:
            if dia < 29:
                prox_dia = dia + 1
                prox_mes = mes
                prox_ano = ano
            else:
                prox_dia = 1
                prox_mes = mes + 1
                prox_ano = ano
        else:
            if dia < 28:
                prox_dia = dia + 1
                prox_mes = mes
                prox_ano = ano
            else:
                prox_dia = 1
                prox_mes = mes + 1
                prox_ano = ano
    elif mes in [4, 6, 9, 11]:
        if dia < 30:
            prox_dia = dia + 1
            prox_mes = mes
            prox_ano = ano
        else:
            prox_dia = 1
            prox_mes = mes + 1
            prox_ano = ano
    else:
        if dia < 31:
            prox_dia = dia + 1
            prox_mes = mes
            prox_ano = ano
        elif mes == 12:
            prox_dia = 1
            prox_mes = 1
            prox_ano = ano + 1
        else:
            prox_dia = 1
            prox_mes = mes + 1
            prox_ano = ano

    print(f'A próxima data é: {prox_dia}/{prox_mes}/{prox_ano}')
else:
    print("Data inválida")


#Exercício 08

nota1 = float(input("Digite a nota da primeira parcial: "))
nota2 = float(input("Digite a nota da segunda parcial: "))

media = (nota1 + nota2) / 2

if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
else:
    conceito = "E"

print(f'Nota da primeira parcial: {nota1}')
print(f'Nota da segunda parcial: {nota2}')
print(f'Média: {media}')
print(f'Conceito: {conceito}')

if conceito in ['A', 'B', 'C']:
    print("APROVADO")
else:
    print("REPROVADO")


#Exercício 09

salario_atual = float(input("Digite o salário do colaborador: "))

if salario_atual <= 280.00:
    per_aumento = 20
elif salario_atual <= 700.00:
    per_aumento = 15
elif salario_atual <= 1500.00:
    per_aumento = 10
else:
    per_aumento = 5

valor_aumento = salario_atual * (per_aumento / 100)

novo_salario = salario_atual + valor_aumento

print(f'Salário antes do reajuste: R$ {salario_atual:.2f}')
print(f'Percentual de aumento aplicado: {per_aumento}%')
print(f'Valor do aumento: R$ {valor_aumento:.2f}')
print(f'Novo salário após o aumento: R$ {novo_salario:.2f}')
