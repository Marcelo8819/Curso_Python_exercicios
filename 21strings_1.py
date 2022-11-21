# Conhecendo métodos úteis da classe string 

curso = 'pYtHon'

print(curso.upper()) # Converte toda a string para letras maiúsculas 

print(curso.lower()) # Converte toda a string para letras minúsculas

print(curso.title()) # Converte o título do texto para maiúscula

curso = "   Python  "

print(curso + '.')

print(curso.strip() + '.') # Tira todos os espaços em branco da string

print(curso.lstrip() + '.' ) # Tira os espaços em branco da esquerda da string 

print(curso.rstrip() + '.') # Tira os espaços em branco da direita da string


curso = 'Python'

print(curso.center(10, "#")) # Centraliza os caracteres , o primeiro argumento indica o total de caracteres
#da string, e o segundo argumento é opcional, no caso como Python tem apenas 6 argumentos será 
# completado com mais 4 #, para formar os 10, caso não seja informado nenhum caracter será completado com 
# espaços em branco. 

print('-'.join(curso))

menu = 'Python'

print(menu.center(14))



print(menu.center(14, '-'))

print('-'.join(menu))