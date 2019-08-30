inicio = int(input('Digite o numero inicial: '))
fim = int(input('Digite o numero final: '))
passo = int(input('Digite o passo: '))

for c in range(inicio, fim+1, passo):
    print(c)
print('Fim')