import os
os.system('cls')

nota1 = nota2 = 0

while True:
 nomeAluno = input('digite o nome do aluno ou pressione x: ')
 if(nomeAluno == 'x' or nomeAluno == 'X'):
         
 
        break
 else:   
  nota1 = float(input('informe a primeira nota '))
  nota2 = float(input('informe a segunda nota '))
  mediaFinal= (nota1 + nota2)/2 


 print(f'A media do {nomeAluno} é {mediaFinal}')
print('encerrando sistema') 