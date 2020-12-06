def break_words(stuff):
    """Esta função irá dividir palavras."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Esta função coleta uma lista e ordena seus valores."""
    return sorted(words)

def print_first_word(words):
    """Imprime o primeiro item da lista após removê-lo"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Imprime o último item da lista após removê-lo"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Recebe uma string e retorna uma lista ordenada"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Imprime o primeiro e último itens da lista"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Imprime o primeiro e último itens da lista ordenada"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

if __name__ == '__main__':
    sentence = "All good things come to those who wait."
    words = break_words(sentence)
    print(words)
    sorted_words = sort_words(words)
    print(sorted_words)
    print_first_word(words)
    print_last_word(words)
    print(words)
    print_first_word(sorted_words)
    print_last_word(sorted_words)
    print(sorted_words)
    sorted_words = sort_sentence(sentence)
    print(sorted_words)
    print_first_and_last(sentence)
    print_first_and_last_sorted(sentence)
