import random
from urllib.request import urlopen
import sys

WORD_URL = 'https://learncodethehardway.org/words.txt'

words = []

phrases = {
    'class %%%(%%%):':
    'Make a class named %%% that is a %%%.',

    'class %%%(object):\n\tdef __init__(self, ***):':
    'class %%% has-a __init__ that takes self and *** params.',

    'class %%%(object):\n\tdef __init__(self, @@@):':
    'class %%% has-a __init__ that takes self and @@@ params.',

    '*** = %%%()':
    'Set *** to an instance of class %%%.',

    '***.***(@@@)':
    'From *** get the *** function, call it with params self and @@@.',

    '***.*** = \'***\'':
    'From *** get the *** attribute and set it to \'***\'.'
}

# Quer treinar primeiro as frases ou os nomes?
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    phrase_first = True
else:
    phrase_first = False

# Carregue palavras do website
for word in urlopen(WORD_URL).readlines():
    words.append(str(word.strip(), encoding='utf-8'))


def convert(snippet, phrases):
    class_names = [w.capitalize() for w in
                   random.sample(words, snippet.count('%%%'))]
    other_names = random.sample(words, snippet.count('***'))
    results = []
    param_names = []

    for i in range(0, snippet.count('@@@')):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(words, param_count)))

    for sentence in snippet, phrases:
        result = sentence [:]

        # Nomes de classes falsos
        for word in class_names:
            result = result.replace('%%%', word, 1)

        # Outros nomes falsos
        for word in other_names:
            result = result.replace('***', word, 1)

        # Lista de parâmetros falsas
        for word in param_names:
            result = result.replace('@@@', word, 1)

        results.append(result)

    return results

# Continue tentando até que seja digitado ^D (^C no Windows)
try:
    while True:
        snippets = list(phrases.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = phrases[snippet]
            question, answer = convert(snippet, phrase)
            if phrase_first:
                question, answer = answer, question

            print(question)

            input('> ')

            print(f'ANSWER: {answer}\n\n')

except EOFError:
    print('\nYou\'ve pressed ^D\nBye')

except KeyboardInterrupt:
    print('\nYou\'ve pressed ^C\nBye')
