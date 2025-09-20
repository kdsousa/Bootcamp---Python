# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.
nome = input('Digite seu nome: ')
salario = float(input('Digite o valor do seu salario mensal: '))
bonus = float(input('Digite o valor do seu bonus: '))
valor_bonus = 1000 + salario * bonus

print(f'Olá {nome}!')
print(f'O valor do seu bonus é de R${valor_bonus}')