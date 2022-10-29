# Declarando variáveis
paisA1 = 15000
paisA2 = 15000
paisB = 45000
paisC = 65000
paisC *= 1.025
paisC_23 = paisC*1.23
anoa = 0
anob = 0

# Quantos anos levará para o país A ultrapassar o país B

while paisB>paisA1:
    paisA1 = paisA1+(paisA1 * 0.10)
    paisB = paisB+(paisB * 0.05)
    anoa+=1
print(f'Levará {anoa} anos')

# Quantos anos levará para o país A ultrapassar o país C em 23%

while paisC_23>paisA2:
    paisA2 *= 1.10
    paisC *= 1.025
    paisC_23 = paisC*1.23
    anob+=1
print(f'Levará {anob} anos')
    