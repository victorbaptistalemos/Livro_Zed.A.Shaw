ten_things = 'Apples Oranges Crows Telephone Light Sugar'

print('Wait, there are not 10 things in that list. Let\'s fix that.')

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee',
              'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) < 10:
    next_one = more_stuff.pop()
    print(f'Adding: {next_one}')
    stuff.append(next_one)
    print(f'There are {len(stuff)} items now.')

print(f'There go: {stuff}')

print('Let\'s do some things with stuff.')

print(stuff[1])
# Imprimiu o segundo da lista, o primeiro índice é 0

print(stuff[-1])
# Imprimiu o primeiro item de trás para frente
# Ordem inversa de uma lista pode ser acessada por índices negativos

print(stuff.pop())
# Imprimiu o último último item da lista e o removeu da lista
# Para remover um índice específico, o índice deve ser o argumento de pop()

print(' '.join(stuff))
# Imprimiu uma string criada a partir da junção de uma lista

print('#'.join(stuff[3:5]))
# Imprimiu uma string criada a partir de uma lista seccionada
# stuff[3:5] significa seccionar a lista stuff começando no quarto elemento e
# parando antes do sexto elemento (uma lista de 2 elementos)
