def add(a, b):
    print(f'ADDING {a} + {b}')
    return int(a) + int(b)

def subtract(a, b):
    print(f'SUBTRACTING {a} - {b}')
    return int(a) - int(b)

def multiply(a, b):
    print(f'MULTIPLYING {a} * {b}')
    return int(a) * int(b)

def divide(a, b):
    print(f'DIVIDING {a} / {b}')
    return int(a) / int(b)

print('Let\'s do some math with just functions!')

age = add(30, 5)
heigth = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f'Age: {age}, Height: {heigth}, Weight: {weight}, IQ: {iq}')


# Uma charada para ponto extra (lol). Digite isso.
print('Here\'s a puzzle.')
print('what = add(age, subtract(heigth, multiply(weight, divide(iq, 2))))')

what = add(age, subtract(heigth, multiply(weight, divide(iq, 2))))

print(f'That becomes {what}. Can you do it by hand?')
