import random

quantidaden = 150
num_antec = random.randint(1,9)
print(num_antec)
tamanho = 1
maior_qtdade = 1
soma = num_antec
count = 0
maior_soma = 0

while count <= quantidaden:
    num_atual = random.randint(1,9)
    print(num_atual)
    
    if num_atual == num_antec + 1:
        print('É uma sequência')
        tamanho += 1
        soma += num_atual
        print(f'O tamanho da sequência é {tamanho} e a soma é {soma}')
        
    else:
        print('Sequência quebrada')
        
        if tamanho >= maior_qtdade:
            maior_qtdade = tamanho
            if soma > maior_soma:
                maior_soma = soma
        tamanho = 1
        soma = num_atual
    
    count = count+1
    num_antec = num_atual
    
if tamanho >= maior_qtdade:
    maior_qtdade = tamanho
    maior_soma = soma
    
print(f'A maior sequência contém: {maior_qtdade} números')
print(f' A maior soma foi de: {maior_soma}')