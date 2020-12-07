def dashes():
    print('-' * 8 ** 2)

# Criando dois mapeamentos de estados
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

estados = {
    'Espírito Santo': 'ES',
    'Rio de Janeiro': 'RJ',
    'Amazonas': 'AM',
    'Pará': 'PA',
    'Ceará': 'CE',
    'Piauí': 'PI',
    'Santa Catarina': 'SC',
    'Paraná': 'PR',
    'Tocantins': 'TO',
    'Mato Grosso': 'MT'
}

# Crie conjuntos básicos de estados e algumas cidades
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroid',
    'FL': 'Jacksonville'
}

cidades = {
    'ES': 'Serra',
    'RJ': 'Cabo Frio',
    'AM': 'Parintins',
    'PA': 'Santarém',
    'CE': 'Camocim'
}

# Adicione mais algumas cidades
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
cidades['PI'] = 'Parnaíba'
cidades['SC'] = 'São José'
cidades['PR'] = 'Pato Branco'
cidades['TO'] = 'Almas'
cidades['MT'] = 'Sorriso'

# Imprima algumas cidades
dashes()
print(f'NY State has: {cities["NY"]}')
print(f'FL State has: {cities["FL"]}')
print(f'OR State has: {cities["OR"]}')
dashes()
print(f'O Estado de UF ES tem: {cidades["ES"]}')
print(f'O Estado de UF AM tem: {cidades["AM"]}')
print(f'O Estado de UF SC tem: {cidades["SC"]}')

# imprima alguns estados
dashes()
print(f'Michigan\'s abbreviation is: {states["Michigan"]}')
print(f'Florida\'s abbreviation is: {states["Florida"]}')
dashes()
print(f'A UF de Ceará é: {estados["Ceará"]}')
print(f'A UF do Amazonas é: {estados["Amazonas"]}')

# Agora a parte interessante
# Imprima um dicionário dentro do outro
dashes()
print(f'California has: {cities[states["California"]]}')
print(f'Oregon has: {cities[states["Oregon"]]}')
dashes()
print(f'Paraná tem: {cidades[estados["Paraná"]]}')
print(f'Tocantins tem: {cidades[estados["Tocantins"]]}')
print(f'Pará tem: {cidades[estados["Pará"]]}')
print(f'Rio de Janeiro tem: {cidades[estados["Rio de Janeiro"]]}')

# Imprima todas as siglas dos estados
dashes()
for state, abbrev in list(states.items()):
    print(f'{state} is abbreviated {abbrev}')

dashes()
for cidade, uf in list(estados.items()):
    print(f'A UF de {cidade} é: {uf}')

# Imprima cada cidade no estado
dashes()
for abbrev, city in list(cities.items()):
    print(f'{abbrev} has the city {city}')

dashes()
for uf, cidade in list(cidades.items()):
    print(f'A UF {uf} tem a cidade de {cidade}')

# Agora faça ambos ao mesmo tempo
dashes()
for state, abbrev in list(states.items()):
    print(f'{state} state is abbreviated {abbrev}', end=' ')
    print(f'and has city {cities[abbrev]}')

dashes()
for estado, uf in list(estados.items()):
    print(f'A UF de {estado} é {uf}', end=' ')
    print(f'e tem a cidade de {cidades[uf]}')

# Por segurança vamos acessar um estado que não está nos dicionários
state = states.get('Texas')
estado = estados.get('Minas Gerais')

if not state:
    dashes()
    print('Sorry, no Texas')

if not estado:
    dashes()
    print('Desculpa, sem Minas Gerais')

# Obtenha uma cidade com um valor padrão
city = cities.get('TX', 'Does not exist')
dashes()
print(f'The city for the state \'TX\' is: {city}')

cidade = cidades.get('MG', 'Não existe')
dashes()
print(f'A cidade para o Estado de UF \'MG\' é: {cidade}')

city = cities.get('CA', 'Does not exist')
dashes()
print(f'The city for the state \'CA\' is: {city}')
cidade = cidades.get('CE', 'Não existe')
dashes()
print(f'A cidade para o Estado de UF \'CE\' é: {cidade}')
