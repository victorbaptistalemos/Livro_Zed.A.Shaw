from os import name as os_name
from os import system as os_system
from random import shuffle
from textwrap import dedent


class Mecanismo:
    """
    Classe que contém todos os mecanismos do jogo. Considerada o coração do jogo.
    """

    # A partir daqui todas as funções de inicialização são chamadas.
    def __gerar_perigos(self):
        """
        Método para gerar aleatoriamente as salas dos perigos.
        """

        perigos = ['Abelha', 'Urso', 'Gelo', 'Acido', 'Cthulhu']
        # Listas das fases com perigos.
        shuffle(perigos)
        # Embaralha a lista.

        for i in range(5):
            # Aciciona ao dicionário self.__salas o valor do índice da lista.
            self.__salas[str(i + 1)] = perigos[i]

        for i in perigos:
            self.__chaves[i] = False

    def __gerar_ferramentas(self):
        """
        Método para gerar aleatoriamente as ferramentas do jogo.
        """

        objetos = ['Inseticida', 'Mel', 'Lança-chamas', 'Pote de solução básica', 'Mirtilos']
        # Lista com as ferramentas do jogo.
        shuffle(objetos)
        # Embaralha a lista.
        for i in range(1, 6):
            # Aciciona ao dicionário self.ferramentas[i] o valor do índice da lista.
            self.__ferramenta_dic[str(i)] = objetos[i - 1]
    # Até aqui todas as funções de inicialização são chamadas.

    # A partir daqui as funções de ferramenta podem ser chamadas.
    def ferramenta_nome(self):
        """
        Método que retorna o nome da ferramenta equipada.
        """

        return self.__ferramenta_dic[self.__ferramenta_posse]

    def __trocar_ferramenta(self, valor):
        """
        Método que executa a troca de ferramenta.
        """

        self.__mesa.remove(valor)
        # Remove da mesa a ferramenta selecionada.
        self.__ferramenta_posse = valor
        # Equipa a ferramenta selecionada.

        if '0' in self.__mesa:
            # É acionada toda vez que o valor 0 estiver em self.__mesa.
            self.__mesa.remove('0')

    def escolher_ferramenta(self):
        """
        Método inicia o processo de troca de ferramenta.
        """

        try:
            self.__mesa.append(self.__ferramenta_posse)
            # Aciciona a ferramenta atual na mesa.
            if self.__ferramenta_posse != '0':
                # Se o valor de self.__ferramenta_posse for diferente de 0
                print()
                print('Você colocou a ferramenta', end=' \'')
                print(self.ferramenta_nome(), end='\' ')
                print('na mesa.')

            if '0' not in self.__mesa:
                # Adiciona o 0 somente se não estiver na mesa.
                self.__mesa.append('0')

            self.__mesa.sort()
            # Ordena as ferramentas na mesa.

            print()
            print('Escolha uma das opções abaixo:')

            for i in self.__mesa:
                # Exibe todas as ferramentas na mesa.
                print(f'{i}: {self.__ferramenta_dic[i]}')

            print()

            valor = input('[Nova ferramenta]: ')
            # Aguarda você escolher um valor numérico da lista impressa

            os_system('cls' if os_name == 'nt' else 'clear')
            # Limpa a tela do terminal.

            if valor in self.__mesa:
                # Você digitou um valor que está na mesa.
                self.__trocar_ferramenta(valor)
                # Executa a troca de ferramentas.
                print(dedent(f'''
                    A ferramenta escolhida foi: \'{self.ferramenta_nome()}\'.
                '''))
                return 'Ferramenta trocada'

            else:
                return 'Botao escondido'

        except KeyboardInterrupt:
            return 'Desespero'

        except EOFError:
            return 'Desespero'

    def usar_ferramenta(self):
        """
        Método que usa a ferramenta equipada.
        """

        print(f'A ferramenta \'{self.ferramenta_nome()}\' foi utilizada!')

        self.__ferramenta_posse = '0'

    # Até aqui toda as funções de utilização de ferramentas podem ser chamadas.

    # A partir daqui as funções de manipulação de tempo podem ser chamadas.
    def gastar_tempo(self, tempo):
        """
        Método que consome o tempo do jogo.
        param: tempo = Tempo a ser consumido.
        """

        self.__tempo -= tempo
        # Consome a quantidade de tempo informado pelo parâmetro recebido.
        return self.__tempo > 0

    # Até aqui todas as funções de manipulação de tempo podem ser chamadas.

    # A partir daqui todas as funções de manipulação de chaves podem ser chamadas.
    def coletar_chave(self, perigo):
        """
        Método que coleta a chave da fase atual.
        param: chave = Índice para manipulação de chave.
        """

        self.__chaves[perigo] = True

    def contar_chaves(self):
        """
        Método que retorna a quantidade de chaves coletadas.
        """

        return list(self.__chaves.values()).count(True)
    # Até aqui todas as funções de manipulação de chaves podem ser chamadas.

    # A partir daqui todas as funções de informação das fases podem ser chamadas.
    def nome_fase(self, sala):
        """
        Método que retorna o nome da sala a partir do parâmetro recebido.
        """

        return self.__salas[sala]

    def escolher_fase(self, nome):
        """
        Método que retorna o número do índice da fase.
        """

        return list(self.__salas.values()).index(nome)
    # Até aqui todas as funções de informação das fases podem ser chamadas.

    def __init__(self):
        """
        Método executado na instanciação de mecanismo.Mecanismo.
        """
        self.__salas = {}
        self.__chaves = {}
        self.__gerar_perigos()
        self.__mesa = [str(_) for _ in range(1, 6)]
        self.__ferramenta_dic = {'0': 'Nenhuma ferramenta'}
        self.__gerar_ferramentas()
        self.__ferramenta_posse = '0'
        self.__tempo = 30

    @property
    def ferramenta_dic(self):
        return self.__ferramenta_dic

    @property
    def ferramenta_posse(self):
        return self.__ferramenta_posse

    @property
    def tempo(self):
        return self.__tempo

    @property
    def mesa(self):
        return self.__mesa
