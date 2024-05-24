import os
import shutil

# diretorio 

# with open('aula1', 'w') as arqui:
#      os.mkdir('novo')


#ler um arquivo
# with open('text.txt', 'r') as arquivo:
#           conteudo  =  arquivo.read()
#           print(conteudo)


# os.rename('text.txt', 'novo_nome')


# with os.scandir('C:/Users/aluno/Downloads/aula1/') as arquivos:
#      for nomes in arquivos:
#          with open('C:/Users/aluno/Downloads/aula1/aula1', 'r') as arquivo:
#               conteudo  =  arquivo.read()
#               print(conteudo.file()) 
              
# print(f'Arquivo {arquivo}', 'r') 


# shutil.rmtree('C:/Users/aluno/Downloads/aula1/pasta_teste')


shutil.copytree('C:/Users/aluno/Downloads/aula1/teste', 'pasta_teste2')