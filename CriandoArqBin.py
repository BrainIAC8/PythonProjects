#Criando arquivo binario
import pickle

arquivo = open('c:\Arqpy/arquivo.dat', 'wb')
for i in range(10):
    pickle.dump(i, arquivo)
arquivo.close()
raw_input('\nAqruivo Binario criado com sucesso!!!!')

#Lendo arquivo binario

arquivo = open('c:\Arqpy/arquivo.dat', 'rb')
soma = 0
for i in range(10):
    n=pickle.load(arquivo)
    soma = soma+n
print soma
arquivo.close()
raw_input('\nArquivo binario lido com sucesso!!!')
