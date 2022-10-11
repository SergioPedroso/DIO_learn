""" 
====================================================
Bootcamp Geração Tech Unimed-BH - Ciência de Dados
====================================================
1/3 - Alfabeto
====================================================
Dada a letra N do alfabeto, nos diga qual a sua posição.
Entrada
Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).
Saída
Um único inteiro, que representa a posição da letra no alfabeto.
--------------------------------------------
| Exemplo de Entrada | Exemplo de Saída    |
--------------------------------------------
| C                  | 3                   |
--------------------------------------------
| J                  | 10                  |
--------------------------------------------
| Z                  | 26                  |
--------------------------------------------
| A                  | 1                   |
--------------------------------------------
SOLUÇÃO ABAIXO:
"""
# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;
letra = input() 


# TODO: De acordo com a entrada, imprima a posição dessa letra no Alfabeto;

for let in letra:
  # Subtração de 64 devido à posição dos caracteres do alfabeto de acordo com a função ord()
    pos = ord(letra) - 64
    print(pos)
    break
