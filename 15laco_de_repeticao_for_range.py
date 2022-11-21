''' Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros
 a partir de um início (inclusico) para um fim (exclusivo). Se usarmos range(i,j) será produzido:
 
 i, i+1, i+2, i+3, ..., j-1.

 Ela recebe 3 argumentos : stop (obrigatório), start (opcional) e step opcional.
 '''

# range (stop) -> range object
# range (start, stop[,step]) -> range object

# for i in range(10):
#     print(i+1, end=" ")

################################################################


# for j in range(-10,0,2):
#     print(j)

################################################################

# for i in range(0,18,3):
#     print(i)

################################################################

for numero in range(0, 11):
    print(numero, end=" ")

################################################################

# Exemplo utilizando o iterável

# for letra in texto:
#     if letra.upper() in vogais:
#         print(letra, end="")
# else:
#     print() 

# # Exemplo utilizando a função built- in range 

# for numero in range(0, 51, 5):
#     print(numero, end=" ")



