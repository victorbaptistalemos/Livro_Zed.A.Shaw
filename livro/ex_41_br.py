import random
from urllib.request import urlopen
import sys

PALAVRAS_URL = 'https://learncodethehardway.org/words.txt'

palavras = []

frases = {
    'class %%%(%%%):':
    'Cria uma classe chamada %%% que é um(a) %%%.',

    'class %%%(object):\n\tdef __init__(self, ***):':
    'classe %%% tem-um __init__ que recebes self and *** parâmetros.',

    'class %%%(object):\n\tdef __init__(self, @@@):':
    'classe %%% tem-um __init__ que recebe self and @@@ parâmetros.',

    '*** = %%%()':
    'Atrubui *** a uma instancia da classe %%%.',

    '***.***(@@@)':
    '*** utiliza a função *** e a chama com os parâmetros self e @@@.',

    '***.*** = \'***\'':
    '*** utiliza o atrubito *** e altera o seu valor para \'***\'.'
}

# Quer treinar primeiro as frases ou os nomes?
if len(sys.argv) == 2 and sys.argv[1] == 'portuguese':
    primeira_frase = True
else:
    primeira_frase = False

# Carregue palavras do website
for palavra in urlopen(PALAVRAS_URL).readlines():
    palavras.append(str(palavra.strip(), encoding='utf-8'))


def converter(trecho, frases):
    nomes_classes = [w.capitalize() for w in
                     random.sample(palavras, trecho.count('%%%'))]
    outros_nomes = random.sample(palavras, trecho.count('***'))
    resultados = []
    nomes_parametros = []

    for i in range(0, trecho.count('@@@')):
        contagem_parametro = random.randint(1, 3)
        nomes_parametros.append(
            ', '.join(random.sample(palavras, contagem_parametro))
        )

    for sentenca in trecho, frases:
        resultado = sentenca [:]

        # Nomes de classes falsos
        for palavra in nomes_classes:
            resultado = resultado.replace('%%%', palavra, 1)

        # Outros nomes falsos
        for palavra in outros_nomes:
            resultado = resultado.replace('***', palavra, 1)

        # Lista de parâmetros falsas
        for palavra in nomes_parametros:
            resultado = resultado.replace('@@@', palavra, 1)

        resultados.append(resultado)

    return resultados

# Continue tentando até que seja digitado ^D (^C no Windows)
try:
    while True:
        trechos = list(frases.keys())
        random.shuffle(trechos)

        for trecho in trechos:
            frase = frases[trecho]
            pergunta, resposta = converter(trecho, frase)
            if primeira_frase:
                pergunta, resposta = resposta, pergunta

            print(pergunta)

            input('> ')

            print(f'RESPOSTA: {resposta}\n\n')

except EOFError:
    print('\nTchau')
