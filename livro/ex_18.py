# Essa aqui é como seus scripts com argv
def print_two(*args):
    arg_1, arg_2 = args
    print(f'arg1: {arg_1}, arg2: {arg_2}')

# No modelo acima, o * é desnecessário, podemos simplesmente fazer isso
def print_two_again(arg_1, arg_2):
    print(f'arg1: {arg_1}, arg2: {arg_2}')

# Essa recebe apenas um argumento
def print_one(arg_1):
    print(f'arg1: {arg_1}')

# Essa não recebe argumento nenhum
def print_none():
    print('I have nothing if I don\'t have you')

print_two('Zed', 'Shaw')
print_two_again('Zed', 'Shaw')
print_one('First')
print_none()
