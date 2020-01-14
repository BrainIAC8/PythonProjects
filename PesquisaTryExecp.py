#Tentando Abrir  Aqrquivo
nome =  raw_input('Digite o nome do arquivo: ')
try:
 arquivo = open('c:\Arqpy/'+nome)
except:
    print 'O arquivo '+nome+'nao pode ser aberto'
    raw_input(' Pressione<ENTER> para terminar...')
    exit()
for linha in  arquivo:
    print linha.rstrip()
arquivo.close()
raw_input('\nArquivo aberto com sucesso!!!')