#Estrutura de controle com tratamento de excecoes Try/Except/Finally

def filhos():
    try:
        val = int(raw_input('Quantos filhos voce tem?'))
    except StandardError, e:
        print 'Erro - ', e
        return 'Errado!'
    finally:
        print 'Registrado!!'
    print val
    return val
filhos()
filhos() #Segunda vez
filhos() #Terceira vez
raw_input()