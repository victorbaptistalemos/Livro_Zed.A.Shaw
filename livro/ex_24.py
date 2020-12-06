print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes with \\ that do:')
print('"\\n"\nnew lines and "\\t"\ttabs')

poem = '''
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
'''

print('-' * 15)
print(poem)
print('-' * 15)

five = 10 - 2 + 3 - 6
print(f'This should be five: {five}')

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans // 1000
    crates = jars // 100
    return jelly_beans, jars, crates

start_point = 10_000
beans, jars, crates = secret_formula(start_point)

print(f'With a start point of: {start_point}')
print(f'We\'d have {beans} beans, {jars} jars, and {crates} crates')

start_point //= 10

print('We can also do this way:')
formula = secret_formula(start_point)
# Essa é uma maneira fácil de aplicar uma tupla a uma string de formatação
print(f'We\'d have {} beans, {} jars, and {} crates'.format(*formula))
