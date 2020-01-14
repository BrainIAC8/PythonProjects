#Modulo RE - regular expression

import re, math

er = re.findall(r'\bf[a-z]*', 'which foot or had fell faster')
print er

er2 = re.sub(r'\bAMD',r'AuthenticAMD', 'AMD Turion(tm) 64 X2 Mobile')
print er2

er3 = re.sub(r'(\b[a-z]+) \1', r'\1', 'Hoje esta um dia dia ensolarado')
print er3

def Sin(a):
    ang = a*math.pi/180
    return math.sin(ang)

sin = Sin(60)
print  sin

sin2 = Sin(30)
print sin2

import random
ram = random.choice(['goiaba', 'laranja', 'abacate', 'pera'])
print  ram

range1 = random.randrange(100)
print  range1

from datetime import date
hoje = date.today()
nascimento = date(1979,11,28)
idade = hoje-nascimento
print idade
print 'Sua idade e %d anos' % int(idade.days/365)