teclado = 'teclado'

#exibindo o primeiro caracter da palavra que esta na variavel teclado
print(teclado[0])
#exibindo o terceiro caracter
print(teclado[4])
#exibindo o ultimo caracter sem precisar ficar contando
print(teclado[-1])

#exibindo o index da letra 'l' dentro da variavel
print(teclado.index('l'))
#exibindo o index da letra 'a' dentro da variavel
print(teclado.index('a'))

#exibindo caracter de forma dinamica
print(teclado[teclado.index('l')])
print(teclado[teclado.index('a')])

#acessando partes de uma string
link = 'youtube.com/c/LofiGirl'
#imprimindo o primeiro e o ultimo caracter
print(link[0])
print(link[-1])

#imprimindo toda a string
print(link[0:])
#imprimindo as primeiras 7 letras
print(link[0:7])
#imprimindo as ultimas letras
print(link[14:])
#outra maneira de imprimir as ultimas letras
print(link[-8:])

#exibindo a ultima ocorrecia de um caracter, nao necessariamente um caracter repetido
frase = 'Clean Code'
print(frase.rindex('C'))
print(frase.rindex('a'))
