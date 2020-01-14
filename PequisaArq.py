#Abertura de arquivo e gravacao
arq = open('c:\Arqpy/arquivoN.txt', 'w')
texto = []
for i in range(1,11):
    t = str(i)
    texto.append(t +'\n')
arq.writelines(texto)
arq.close()
raw_input('Arquivo criado com sucesso!!!')

# Pesquisando em arquivos
arquivo = open('c:\Arqpy/arquivoN.txt', 'r')
for linha in arquivo:
    if int(linha)%2 != 0:
        print linha.rstrip() #imprime sem linhas em branco
arquivo.close()
raw_input('\nPesquisa realizada!!!')
