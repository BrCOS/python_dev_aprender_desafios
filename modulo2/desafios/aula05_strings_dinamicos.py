"""
Desafio 1
Crie os seguintes strings dinâmicos
nome = "Carol"
hobby = "ouvir Música"
"Olá sou a Carol e gosto de ouvir musica"
"""

nome, hobby = 'Carol', 'ouvir musica'

print(f'Olá, sou a {nome}, e eu gosto de {hobby}')


"""
Desafio 2
Monte a seguintes palavras, usando as sílabas como base
b = "ba"
parte2 = "nica"
a = "a"
r = "ri"
parte1 = "eletrô"
t = "te"
# Resultado
"bateria eletrônica"
"""

b, parte2, a, r, parte1, t = 'ba', 'nica', 'a', 'ri', 'eletrô', 'te'
print(f'{b}{t}{r}{a} {parte1}{parte2}')