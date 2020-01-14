#Escrevendo Arquivos
arquivo = open('c:\Arqpy/arquivonum.txt', 'w')
val = 0
for num in range(10):
    val = val + 1
    arquivo.write(str(val)+'\n')
arquivo.close()
raw_input('\nGravacao realizada com sucesso!!!!')
