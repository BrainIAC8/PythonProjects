#Abrtura de arquivo e gravacao
arq = open('c:\Arqpy/arquivoN.txt', 'w')
texto = []
for i in 10:
    texto.append(i,'\n')
arq.writelines(texto)
arq.close()
raw_input('Arquivo criado com sucesso!!!')

arq = open('c:\Arqpy/arquivoN.txt', 'a')
texto = []
texto.append('\nNOME 5\n')
texto.append('NOME 6\n')
texto.append('NOME 7')
arq.writelines(texto)
arq.close()
raw_input('Novos amigos acrescentados com sucesso!!!')

#Leitura de arquivos
arq = open('c:\Arqpy/arquivo.txt', 'r')
texto = arq.readlines()
for linha in  texto:
    print(linha)
arq.close
raw_input('\nleitura realizada!!!')

#Leitura de arquivos2
arquivo = open('c:\Arqpy/arquivo.txt', 'r')
s = arquivo.read()
print s
arquivo.close()
raw_input('\nLeitura realizada!!!')