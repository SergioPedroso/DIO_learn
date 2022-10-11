""" 
====================================================
Bootcamp Geração Tech Unimed-BH - Ciência de Dados
====================================================
3/3 - Aumento Salarial
====================================================
A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:
--------------------------------------------------
| Salário            | Percentual de Reajuste    |
--------------------------------------------------
| 0 - 600.00         | 17%                       |
--------------------------------------------------
| 600.01 - 900.00    | 13%                       |
--------------------------------------------------
| 900.01 - 1500.00   | 12%                       |
--------------------------------------------------
| 1500.01 - 2000.00  | 10%                       |
--------------------------------------------------
| Acima de 2000.00   | 5%                        |
--------------------------------------------------
Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.
A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas decimais, conforme exemplos abaixo.
Exemplo 1
-----------------------------------------------------------------------------------------
| Exemplo de Entrada |                              Saída                               |
-----------------------------------------------------------------------------------------
| 1000               | Novo salario: 1120,00 Reajuste ganho: 120,00 Em percentual: 12 % |
-----------------------------------------------------------------------------------------
Exemplo 2
-----------------------------------------------------------------------------------------
| Exemplo de Entrada |                              Saída                               |
-----------------------------------------------------------------------------------------
| 2000               | Novo salario: 2200,00 Reajuste ganho: 200,00 Em percentual: 10 % |
-----------------------------------------------------------------------------------------
SOLUÇÃO ABAIXO:
"""
salario = int(input())

if salario <= 600:
  percentual = 17
  reajuste = (salario/100) * percentual
  novo_salario = (salario/100) * percentual + salario
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {} %'.format(percentual))
elif salario <= 900:
  percentual = 13
  reajuste = (salario/100) * percentual
  novo_salario = (salario/100) * percentual + salario
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {} %'.format(percentual))
elif salario <= 1500:
  percentual = 12
  reajuste = (salario/100) * percentual
  novo_salario = (salario/100) * percentual + salario
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {} %'.format(percentual))
elif salario <= 2000:
  percentual = 10
  reajuste = (salario/100) * percentual
  novo_salario = (salario/100) * percentual + salario
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {} %'.format(percentual))
else:
  percentual = 5
  reajuste = (salario/100) * percentual
  novo_salario = (salario/100) * percentual + salario
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {} %'.format(percentual))


salario = int(input()) 

if (0 <= salario <= 600):
  perc_reajuste = 0.17
  reajuste = salario * perc_reajuste
  novo_salario = salario + reajuste
  print(f'Novo Salario: {novo_salario:.2f}'.format(novo_salario))
  print(f'Reajuste ganho: {reajuste:.2f}'.format(reajuste))
  print(f'Em percentual: {(perc_reajuste*100):.0f} %'.format(perc_reajuste))
  
elif (600 < salario <= 900):
  perc_reajuste = 0.13
  reajuste = salario * perc_reajuste
  novo_salario = salario + reajuste
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {:.0f} %'.format(perc_reajuste*100))
  
elif (900 < salario <= 1500):
  perc_reajuste = 0.12
  reajuste = salario * perc_reajuste
  novo_salario = salario + reajuste
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {:.0f} %'.format(perc_reajuste*100))
  
elif (1500 < salario <= 2000):
  perc_reajuste = 0.1
  reajuste = salario * perc_reajuste
  novo_salario = salario + reajuste
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {:.0f} %'.format(perc_reajuste*100))
  
elif (salario > 2000):
  perc_reajuste = 0.05
  reajuste = salario * perc_reajuste
  novo_salario = salario + reajuste
  print('Novo salario:',"{:.2f}".format(novo_salario))
  print('Reajuste ganho:',"{:.2f}".format(reajuste))
  print('Em percentual: {:.0f} %'.format(perc_reajuste*100))

else: 
  print('Valor de salário inválido...')
