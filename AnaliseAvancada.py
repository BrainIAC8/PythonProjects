#Analise avancada de textos

import string

fname = raw_input('Digite o nome do arquivo: ')
try:
    fhand = open('c:\Arqpy/'+fname)
except:
    print 'Arquivo nao aberto....'
    exit()
counts = dict()
for line in fhand:
    line = line.translate(None, string.punctuation)
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print  counts
raw_input('>>>>>>.....')