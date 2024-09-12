import os
os.system('cls')

nome = None

while True:

    nome = input('informe seu nome ou pressione x para sair ')

    if(nome == 'x' or nome == 'X'):
        break
    else:
        print(f'seja bem vindo {nome}')
print('até logo')
