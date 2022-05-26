import time

n1 = int (input('Digite um numero: '))
n2 = int (input('Digite outro numero: '))
s = n1 - n2

print('Espere 5 segundos')

time.sleep(5)

print('A subtracao entre {} e {} da o resultado {}!'.format(n1, n2, s))

print('em 10 segundos o app fechara')

time.sleep(10)