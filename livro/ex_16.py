from sys import argv

script, filename = argv

print(f'We\'re going to erase {filename}.')
print('If you don\'t want that, hit Ctrl-C (^C).')
print('If you do want that, hit RETURN.')

input('?')

print('Opening thr file...')
target = open(filename, 'w')
print('Truncating the file. Goodbye!')
target.truncate()

print('Now I\'m going to ask you for three lines.')

line_1 = input('line 1: ')
line_2 = input('line 2: ')
line_3 = input('line 3: ')
line_4 = input('line 4: ')

print('I\'m going to write these to the file.')

target.write(line_1)
target.write('\n')
target.write(line_2)
target.write('\n')
target.write(line_3)
target.write('\n')
target.write(line_4)
target.write('\n')

print('And finally, we close it.')
target.close()
