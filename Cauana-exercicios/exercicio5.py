n = 0
resultado_h = 1
resultado_s = 1
resultado_p = 0

#Exercício 5 - tópico 1
while n < 50:
    n = int(input('Digite um número para calcular o H: '))

while n > 1:
    if n % 2 == 0:
        resultado_h = resultado_h + (n * 2 - 1 )/n
    else:
        resultado_h = resultado_h - (n * 2 - 1)/n
    n = n - 1

#Exercício 5 - tópico 2

while n < 50:
    n = int(input('Digite um número para calcular o S: '))
resultato_s = 1
while n > 1:
    if n % 2 == 0:
        resultado_s = resultado_s - (n/(n*n)) 
    else:
        resultado_s = resultado_s + (n / (n * n))
    n = n - 1

#Exercício 5 - tópico 3
while n < 50:
    n = int(input('Digite um número para calcular o P: '))

contador = 0
potencia = 1

while True:

    while potencia <= n:
        contador = contador + 1
        multiplicador = contador
        verificador = 0 

        while multiplicador != 1:
            if contador % multiplicador == 0:

                verificador = verificador + 1 
            multiplicador = multiplicador - 1

        if verificador == 1:
            resultado_p = resultado_p + (contador/potencia ** 3)
            potencia = potencia + 2
    if potencia > n:
        break

print(f'O valor do calculo de H: {resultado_h}')
print(f'O valor do calculo de S: {resultado_s}')
print(f'O valor do calculo de P: {resultado_p}')