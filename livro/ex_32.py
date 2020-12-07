the_count = [1, 2, 3, 4, 5]
fruits = [ 'apples', 'oranges', 'pears', 'peaches', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quartes']

# Esse primeiro tipo de loop for percorre uma lista
for number in the_count:
    print(f'This is the count {number}')

# O segundo exemplo faz a mesma coisa que o primeiro
for fruit in fruits:
    print(f'A fruit of type: {fruit}')

# Listas mistas também podem ser percorridas
# {} indica uma variável na f'string', nesse caso um item de lista
for i in change:
    print(f'I got {i}')

# Listas podem ser modificadas, acrescentando ou removendo
elements = []

# Uma forma é acrescentar uma lista inteira de uma vez
elements.extend(the_count)

# Outra forma é acrescentar através de um loop
for i in range(6, 11):
    print(f'Adding {i} to the list.')
    # append é uma função que as listas entendem
    elements.append(i)

# Uma forma de remover um item de uma lista é através do seu índice
elements.pop(1)
# Removeu o segundo item da lista, cujo valor era 2
# Equivale a elements.remove(2)

# Outra forma de remover é através do valor armazenado
elements.remove(5)
# Removeu o item de valor 5 que é o quarto item da lista
# Equivale a elements.pop(3)

# Agora podemos imprimir o resultado das modificações
for i in elements:
    print(f'The element was: {i}')
