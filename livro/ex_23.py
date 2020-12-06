import sys
script, encoding, error, input_file = sys.argv

# https://learnpythonthehardway.org/python3/languages.txt
# O arquivo languages.txt foi renomeado para ex_23_sample.txt

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, '<===>', cooked_string)


languages = open(input_file)
# Lendo a partir da raiz da aplicação

main(languages, encoding, error)
