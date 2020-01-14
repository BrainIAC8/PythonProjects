d={'a':1000,'b':3000, 'c':100}
print 'a=1000, b=3000, c=100'
print 'Maximo = '+ max(d,key=d.get)
print 'Minimo = ' + min(d, key=d.get)
raw_input('>')

#
def troca(x,y):
    aux = x
    x = y
    y = aux
    return x,y
a = int(raw_input('Valor 1 numero: '))
b = int(raw_input('Valor 2 numero: '))
print troca(a,b)
raw_input()

print "tamanho da palavra: " + str(len('AUGUSTO'))
raw_input()

ano_nasc=raw_input('Qual o ano do seu nascimento?')
ano_atual='2020'
idade=int(ano_atual)-int(ano_nasc)
print 'Voce tem ' + str(idade) +' anos de idade'
raw_input()

import math
a=25
b=math.sqrt(a)
print 'Raiz quadrada: ' + str(b)
raw_input()