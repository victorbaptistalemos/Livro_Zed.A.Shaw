from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f'Copying from {from_file} to {to_file}')

# Poderíamos fazer esses dois como uma lista, como?
in_file = open(from_file)
indata = in_file.read()

print(f'The input file is {len(indata)} bytes long')

print(f'Does the output file exists? {exists(to_file)}')
print('Ready, hit RETURN to continue, ^C to abort.')
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print('Alright, all done.')

out_file.close()
in_file.close()
