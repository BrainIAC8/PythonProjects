# Compara Tuplas

txt = 'ciencia de dados em busca da vantagem competitiva'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)
print res
print t
raw_input('>>>>Fim')

# Recurso de atribuicao compposta

m = ['Fabio', 'Augusto', 'Andrade']
x1, x2, x3 = m
print x1
print x2
print x3
print m.count(x3)
print x1+' ' +x2+' '+x3
raw_input('>>>>>>')