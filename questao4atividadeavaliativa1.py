# Elabore um algoritmo que leia 150 numeros inteiros e imprima:

# =-=-=Qual o tamanho da maior sequencia consecutiva de numeros em
# ordem crescente, assumindo como criterio de desempate a
# soma dos números:

# =-=-=Qual o tamanho da maior sequencia consecutiva de numeros
# constantes, assumindo como critério de desempate o valor do
# número envolvido na sequência:

qtdnum = 150 #quantidade de numeros que deseja ler, no caso é 150 pedido no enunciado
numante = int(input('Número inicial para fazer o loop: ')) #numero fora do loop para criar parametro dentro do while
tamanho = 1 #tamanho da sequencia
maiortamanho = 1
soma = numante #acumulador do numero que eu digitei
msoma = 0 #maior soma
numig = 0 #variavel para numero igual
somamaxig = 1
nuig = 1 #contador numero igual
numaxig = 1#contador numero igual maximo
i = 2 # contador que é usado ate atingir o qtdnum inseridos
        # (já começa em 2, pq o primeiro/1, já foi pedido na primeira vez que rodou o programa)

while i <= qtdnum: #enquanto "i" for menor que "qtdnum":
    natual = int(input('Digite o número ')) #numero atual

    if natual == numante + 1: #se numero atual for o numero anterior mais um, ele está na sequencia
                                #exemplo numero anterior era 5 e numero digitado agora é 6,
                                # entao temos uma sequencia pois 6 = (5 +1) !!!:
        #print('Estou numa sequência') #mensagem se estiver na sequencia
        tamanho = tamanho + 1 #se estiver na sequencia vai aumentar o tamanho(contador de tamanho)
        soma = soma + natual #soma que estava lá mais o numero atual
        if tamanho == maiortamanho and soma > msoma:
            maiortamanho = tamanho
            msoma = soma
        if tamanho > maiortamanho:  # essa ultima sequencia é maior que a maior sequencia?
            maiortamanho = tamanho
            msoma = soma
        #print('Tamanho: {}, Soma {}'.format(tamanho, soma)) #seguindo o exemplo acima: Tamanho: 2 Soma 11
                                                            # pois 5, 6 são sequencia e somados são igual a 11

    else: #se for comparado e não estiver na sequencia exibir:
        #print('Sequência quebrada') #mensagem caso quebre a sequencia
        #quando é quebrada a sequencia deve resetar o tamanho e sequencia ou seja está iniciando uma sequencia nova
        tamanho = 1 #nova sequencia e começa com um numero só
        soma = natual #soma é o numero atual dessa nova sequencia


    if natual == numante: #numero atual é igual ao numero anterior
        nuig = nuig + 1 #contador para numeros iguais

        if nuig == numaxig and natual > numig:# verificando se o numero igual esta com numeros
            numaxig = nuig # numero maximo igual recebe numero igual
            numig = natual #numero igua recebe numero atual

        if nuig > numaxig: #se numero igual for maior que numero maximo igual :
            numaxig = nuig
            numig = natual
    else:
        nuig = 1
    i = i + 1 #contador numeros inseridos
    numante = natual #esse numero que acabei de ler vai ser considerado o numero anterior
                    #na proxima interação(qdo entrar novamente no while)

if maiortamanho > 1:
    print('A maior sequência crescente: ', maiortamanho) #mostra o maior tamanho da sequencia
else:
    print('A maior sequencia crescente foi: ZERO')
#print('A maior soma: ',msoma) #mostrar a soma dos numeros inseridos e que fazem parte da maior sequencia
if numaxig > 1:
    print('A maior sequência de números iguais: ', numaxig)#mensagem final informando a sequencia/qtidade
    # de numeros iguais
else:
    print('A maior sequência de números iguais: ZERO')
#print('Número mais repetido: ', numig) #numero mais repetido