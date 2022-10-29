
# Entrada salário fixo e valor de vendas

sal_fixo = float(input('Salário fixo: '))
valor_vendas = float(input('valor das vendas: '))

# Calculando comissão para valor de vendas menor do que 1500 reais

if valor_vendas <= 1500.00:
    pct5= valor_vendas*0.05
    sal_total = sal_fixo + pct5
    print(f'O salário total foi {sal_total}, sendo que {pct5} de comissão e {sal_fixo} de salário fixo.')
    
    
# Calculando comissão para valor de vendas maior do que 1500 reais
else:
    valoracm = valor_vendas - 1500
    totalvendas1 = valoracm * 0.07
    totalvendas2 = 1500 * 0.05
    totalvendas = totalvendas1+totalvendas2
    sal_total = totalvendas + sal_fixo
    print(f'O salário total foi {sal_total:.2f}, sendo que {totalvendas} de comissão e {sal_fixo} de salário fixo.')