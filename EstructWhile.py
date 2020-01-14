#Loop infinitos: break e continue
while True:
    line = raw_input('Digite algo e pressione ENTER(parar p/ terminar) >')
    if line[0]=='#':
        continue #nao imprime ND
    if line == 'parar':
        break
    print line
print 'Finalizado!!!'
raw_input()



#Mostrar a soma de todos os numeros positivos
# menores que 10

cont = 1
soma = 0
while(cont < 10):
    soma = soma + cont
    cont = cont + 1
    print 'Soma =', soma

raw_input()

#Outro Exemplo
num = 5
while num > 0:
    print num,
    num = num -1
raw_input()
