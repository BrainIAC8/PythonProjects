#Funcao retorna pi
import  math
a = math.pi
print " The value of pi is..." + str(a)
raw_input('>')

x = float(raw_input('Digite um numero para saber o seno, coseno e tangente: '))

a = math.sin(x)
b = math.cos(x)
c = math.tan(x)
print 'Seno de  ' + str(x) + ' = ' + str(a)
print 'Coseno de ' + str(x) + ' = ' + str(b)
print 'Tangente de ' + str(x) + ' = ' + str(c)
raw_input('FIM...')
