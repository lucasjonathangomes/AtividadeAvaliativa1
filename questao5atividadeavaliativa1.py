#Escreva um unico algoritmo que calcule as seguintes sequencias, fornecendo como saida
# resultado de H, S e P, dadas as respectivas entradas do usuario (sem utilizar vetor):
n = 0
resulh = 1
resuls = 1
resulp = 0

while n < 50:
    n = int(input('Digite um número para calcular o H: '))

while n > 1:
    #sistema para se é par ou impar 0 = par, 1 = impar
    if n % 2 == 0:
        resulh = resulh + (n * 2 - 1 )/n # formula do H
    else:
        resulh = resulh - (n * 2 - 1)/n #formula do H
    n = n - 1

#-=-=-=--=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-

while n < 50:
    n = int(input('Digite um número para calcular o S: '))

while n > 1:
    if n % 2 == 0:
        resuls = resuls - (n/(n*n)) #formula do S
    else:
        resuls = resuls + (n / (n * n)) # formula do S
    n = n - 1

#-=-=-=--=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-

while n < 50:
    n = int(input('Digite um número para calcular o P: '))

contador = 0
potencia = 1

while True:

    while potencia <= n:
        contador = contador + 1
        multiplicador = contador
        verificador = 0 #verificando se é primo

        while multiplicador != 1:
            if contador % multiplicador == 0:

                verificador = verificador + 1 #confirmado que é primo adiciona mais UM
            multiplicador = multiplicador - 1

        if verificador == 1:
            #print('Primo : {}, potência {}'.format(contador, potencia))
            resulp = resulp + (contador/potencia ** 3)
            potencia = potencia + 2
    if potencia > n:
        break #para parar o while True

print('O valor do calculo de H: \033[36m{}\033[m'.format(resulh))
print('O valor do calculo de S: \033[36m{}\033[m'.format(resuls))
print('O valor do calculo de P: \033[36m{}\033[m'.format(resulp))


