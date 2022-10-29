# Sabendo que a população do pais A de ordem 15000 habitantes com uma
# taxa de crescimento de 10%, que a população do pais B é de 45000
# habitantes
# com uma taxa de crescimento de 5%, e que a população do país C é de
# 65000 habitantes com uma taxa de crescimento de 2,5%, escreva um
# programa que calcule e imprima:

#Em quantos anos a população A igualará ou ultrapassará a população B; e
#Em quantos anos a população A ultrapassará a população C em 23%.

paisa = 15000 #pais de ordem A
paisa2 = 15000 #segunda variavel de pais de ordem A, para evitar conflito na resolução de 23%
paisb = 45000 #pais de ordem B
paisc = 65000 #pais de ordem C
paisc = paisc * 1.025  #percentual de crescimento de pais C
p23 = paisc * 1.23 #percentual de 23% para comparar com pais A
anoab = 0 #contador pra mostrar em quantos anos vai levar pra A igualar ou ultrapassar B
anoac = 0 #contador que vai mostra em quantos anos vai passar A de C em 23%

while paisb > paisa: #enquanto o pais "b" for maior pais "a" a função ira fazer:
    paisa = paisa + (paisa * 10)/100 #verificação de porcentagem de crescimento de ordem A
    paisb = paisb + (paisb * 5)/100 #verificação de porcentagem de ordem B
    anoab = anoab + 1 #contador dos anos de igualar A e B
print('Em \033[36m{}\033[m anos a população de ordem A igualará ou ultrapassará a população de ordem B'.format(anoab))

while p23 > paisa2: #enquanto a porcentagem de C que é 23%... for maior que de A:
    paisa2 = paisa2 * 1.10 #percentual do pais A (10% como é crescimento se coloca o 1 na frente)
    paisc = paisc * 1.025 #percentual de cresc. do pais C (é entao... coloca o 1 na frente)
    p23 = paisc * 1.23 #parametro de 23%
    anoac = anoac + 1 #contador de anos da ordem A ate ultrapassar ordem B
print('Em \033[36m{}\033[m anos a população de ordem A ultrapassará a população de ordem C em 23%'.format(anoac))
