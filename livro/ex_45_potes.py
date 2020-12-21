from os import name as os_name
from os import system as os_system
from random import randint
from textwrap import dedent


class Potes:

    def __gerar_chave(self):

        for i in range(1, 10):
            self.__potes[str(i)] = 0

        self.__potes[str(randint(1, 9))] = 1

    def entrar_fase(self, mecanismo):

        try:

            os_system('cls' if os_name == 'nt' else 'clear')

            print(f'O colete mostra {mecanismo.tempo} de tempo.')

            if not self.__tentativas:

                self.__tentativas = True

                print(dedent(f'''
                    Você vê no final da sala uma placa pendurada na
                    parede e abaixo dessa placa há uma mesa com alguns
                    potes. Você se aproxima da mesa e verifica que há
                    9 potes na mesa e consegue ler o que está escrito
                    na placa:

                    \tDos 9 potes 1 está com a chave da saída.
                    \tBoa sorte!

                    Você tenta derrubar a mesa para poupar tempo, mas
                    não consegue porque além da mesa estar soldada no
                    chão os potes são muito pesados, parece que foram
                    feitos de chumbo ou algo parecido, ou seja, você
                    só consegue mexer em um pote por vez.

                    Você, então, precisa achar o pote com a chave da
                    saída.
                '''))

                input('Pressione ENTER para continuar.\n')

                os_system('cls' if os_name == 'nt' else 'clear')

                print(f'O colete mostra {mecanismo.tempo} de tempo.')

            print(dedent(f'''
                Qual pote você vai escolher?

                Ações:'''))

            for i in range(1, 10):

                print(f'{i}', end='. ')

                if self.__potes[str(i)] == 2:

                    print(f'Pote #{i} usado e sem chave.')

                else:

                    print(f'Escolher pote #{i}.')

            print()

            acao = input('[Pote #]> ')

            os_system('cls' if os_name == 'nt' else 'clear')

            if int(acao) in range(1, 10):

                if self.__potes[acao] == 1:

                    print(f'Você achou a chave de saída no pote #{acao}')

                    input('Pressione ENTER para continuar.\n')

                    return 'Final' if mecanismo.gastar_tempo(1) else 'Tempo'

                elif self.__potes[acao] == 2:

                    return 'Pote quebrado'

                else:

                    print(f'Você quebrou o pote {acao} e não achou a chave.')

                    input('Pressione ENTER para continuar.\n')

                    self.__potes[acao] = 2

                    return 'Potes' if mecanismo.gastar_tempo(1) else 'Tempo'

            else:

                return 'Botao escondido'

        except KeyboardInterrupt:

            return 'Desespero'

        except EOFError:

            return 'Desespero'

        except ValueError:

            return 'Desespero'

    def __init__(self):
        self.__tentativas = False
        self.__potes = {}
        self.__gerar_chave()
