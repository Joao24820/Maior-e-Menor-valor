n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor : '))
n3 = float(input('Digite o terceiro valor : '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n1 == n2 or n1 == n3 or n2 == n3 or n2 == n1 or n3 == n1 or n3 == n2:
    print('Os Numeros escolhidos são iguais !!')
else:
    print('O menor valor digitado foi {}'.format(menor))
    print('O maior valor digitado foi {} '.format(maior))
