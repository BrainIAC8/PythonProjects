#Funcao que retorna o valor conforme a condicao
def maior_que_zero(x):
    return x > 0
def menor_que_zero(y):
    return y < 0

valores = [10, 4, -1, 3, -9, -11]

print filter(maior_que_zero, valores)
print filter(menor_que_zero, valores)
raw_input('Fim do programa!!!...  ...tecle ENTER para sair')
