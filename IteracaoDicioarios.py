#iteracao com direcionarios

counts = {'Juan':20,'Alfredo':45, 'Giullia':25}
for chave in counts:
    print chave, counts[chave]
raw_input('>>>>>>>>-')

lista = counts.keys()
print  lista
lista.sort()
for chave in lista:
    print chave, counts[chave]
raw_input('....>>>>')