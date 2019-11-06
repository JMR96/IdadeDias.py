# -*- coding: latin1 -*-

diasVida = int(input('Insira o Numero de dias de Vida: '))

ano = int(diasVida / 365)

print ('%d ano(s)' % ano)

meses = int((diasVida / 30)) - (ano * 12)

print ('%d mes(es)' % meses)

if diasVida == 365:
    dia = 0
else:
    dia = diasVida - ((diasVida / 30) * 30)

print ('%d dia(s)' % dia)
