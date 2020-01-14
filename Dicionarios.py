#Dicionario com conjunto de contadores

palavra = 'paralelepipido'
d = dict()
for c in palavra:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c]+1
print  d
raw_input('pausa...')

nomearq = raw_input('Digite o nome do arquivo: ')
try:
    arq = open('c:\Arqpy/'+nomearq)
except:
    print 'Arquivo nao pode ser aberto: ',nomearq
    exit()
counts = dict()
for line in arq:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print  counts
raw_input('pausa...')

