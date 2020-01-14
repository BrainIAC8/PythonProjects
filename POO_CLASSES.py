#CRIANDO CLASSE
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def obterNome(self):
        return self.nome

    def obterIdade(self):
        return self.idade

#criando uma instacia para classe
pessoa = Pessoa('Pedro',49)
print pessoa.obterNome(),':', pessoa.obterIdade()

class Gelatina:
    def __init__(self, tam, cor, sabor):
        self.tam=tam
        self.cor=cor
        self.sabor=sabor
gel1 = Gelatina('pequena', 'vermelha','morango')
gel2 = Gelatina('media', 'amarela', 'abacaxy')
gel3 = Gelatina('grande', 'roxa', 'uva')

print gel1.tam, gel1.cor, gel1.sabor
print gel2.tam, gel2.cor, gel2.sabor
print gel3.tam, gel3.cor, gel3.sabor


class Produto:
    def __init__(self, cod, nome, quant):
        self.cod=cod
        self.nome=nome
        self.quant=quant
codigo = raw_input('Digite o codigo: ')
nome = raw_input('Digite o nome do produto: ')
quantidade = raw_input('Qual a quantidade? ')

produto = Produto(codigo, nome, quantidade)
print '\n'
print 'Dados de Saida:\n'
print 'Codigo:' + produto.cod
print 'Produto: ' + produto.nome
print 'Quantidade: ' + produto.quant
print type(produto.quant), type(produto.cod), type(produto.nome)
raw_input('>>>')