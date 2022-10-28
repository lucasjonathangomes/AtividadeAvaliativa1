# Escreva um algoritmo que receba o valor do salario fixo e o
# valor das vendas efetuadas pelo vendedor de uma empresa,
# ambos informados pelo usuario. Sabendo-se que a empresa paga %5
# sobre um total de até R$1500, MAIS 7% o valor que ultrapassar esse
# montante (diferença), o programa deve calcular e imprimir o
# salario total final do vendedor.

salfix = float(input('Qual o salário fixo?'))
valvend = float(input('Qual o valor da venda?'))

if valvend <= 1500: # Se for igual ou até 1500 no valor da venda, calcular a porcentagem em 5%


    pctg5 = valvend * 0.05
    salfinal = salfix + pctg5 # Salário final vai ser a soma da porcentagem vezes o valor
                            # da venda (variavel pctg5) mais o salario fixo
    print('O salário final do vendedor é \033[32mR${:.2f} \033[m, as vendas foram de \033[32mR${:.2F} \033[m, '
          'comissão foi de \033[32m R${:.2F}. \033[m'.format(salfinal, valvend, pctg5))
# Se for ACIMA de 1500 usar o 7%
else:
# Saber qual o valor que foi excedido/acima nas vendas:
    valacima = valvend - 1500
# valor de venda vai ser igual a 7%:
    comi1 = valacima * 0.07
# O vendedor sempre vai receber a comissão de 5% por ser acima:
    comi2 = 1500 * 0.05
# O valor dos bonus vai ser valvend + comi que seria soma dos valores de 5% e 7%:
#     float(bonus)
    bonus = comi1 + comi2
# Salario final vai ser de:
    saltotal = salfix + bonus
    print('O salário final do vendedor é \033[36mR${:.2f} \033[m, as vendas foram de \033[36mR${:.2F} \033[m, '
          'comissão foi de \033[36m R${:.2F}. \033[m'.format(saltotal, valvend, bonus))
