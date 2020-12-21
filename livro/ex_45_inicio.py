from os import name as os_name
from os import system as os_system
from textwrap import dedent


class Inicio:

    @staticmethod
    def entrar_fase(mecanismo):
        """
        Método para entrar na sala inicial.
        É aqui onde se escolhe os objetos
        e as salas dos perigos.
        Você também pode ir direto para a
        sala das chaves, mas ir até lá
        sem as 5 chaves é perda de tempo.
        """

        try:

            os_system('cls' if os_name == 'nt' else 'clear')

            print(f'O colete mostra {mecanismo.tempo} de tempo.')

            if len(mecanismo.mesa) == 0 and mecanismo.ferramenta_nome() == 'Nenhuma ferramenta':

                print(dedent('''
                    Você está perdendo tempo aqui.
                    Vá para a sala das chaves.
                '''))

                input('Pressione ENTER para continuar.\n')

                print(dedent('''
                    Você está se dirigindo à sala das chaves. Você
                    percebe que o caminho para a sala das chaves é
                    mais longo que o normal. Você acaba gastando uma
                    rodada a mais para chegar.
                '''))

                input('Pressione ENTER para continuar.\n')

                return 'Chaves' if mecanismo.gastar_tempo(2) else 'Tempo'

            if mecanismo.ferramenta_posse == '0':

                print(dedent('''
                    Você está na sala inicial. Você só pode escolher
                    uma ferramenta por vez. O que você vai fazer?
                '''))

            else:

                print(dedent(f'''
                    Ótimo você está com a ferramenta \'{mecanismo.ferramenta_nome()}\'.
                    O que você vai fazer?
                '''))

            print(dedent('''
                Ações:
                1. Escolher ferramenta
                2. Enfrentar perigo
                3. Sala das chaves
            '''))

            acao = input('[Ação]: ')

            os_system('cls' if os_name == 'nt' else 'clear')

            if acao == '1':

                print('Você decidiu escolher uma ferramenta.')

                trocar_ferramenta = mecanismo.escolher_ferramenta()

                if trocar_ferramenta != 'Ferramenta trocada':
                    return trocar_ferramenta

                input('Pressione ENTER para continuar.\n')

                return 'Inicio' if mecanismo.gastar_tempo(1) else 'Tempo'

            elif acao == '2':

                if mecanismo.ferramenta_posse == '0':

                    print(dedent('''
                        Você perderá tempo indo a um local sem um mecanismo.
                    '''))

                else:

                    print(f'Ferramenta selecionada: \'{mecanismo.ferramenta_nome()}\'')
                    print(dedent('''
                        Observe atentamente o perigo da sala e se já
                        enfrentou o perigo naquela sala.
                    '''))

                print('Escolha uma das opções abaixo:')

                for i in range(1, 6):

                    print(f'{i}. {mecanismo.nome_fase(str(i))}')

                print()

                acao = input('[Perigo]: ')

                os_system('cls' if os_name == 'nt' else 'clear')

                if str.isnumeric(acao) and int(acao) in range(1, 6):

                    print(dedent(f'''
                        Você escolheu o cenário {mecanismo.nome_fase(acao)} para enfrentar.
                        Boa sorte.
                    '''))

                    input('Pressione ENTER para continuar.\n')

                    return mecanismo.nome_fase(acao) if mecanismo.gastar_tempo(1) else 'Tempo'

                else:
                    return 'Botao escondido'

            elif acao == '3':

                print(dedent('''
                    Você escolheu ir à sala das chaves. Você percebe
                    que o caminho para a sala das chaves é mais longo
                    que o normal. Você gastou 2 rodadas para chegar ao
                    invés de uma.
                '''))

                input('Pressione ENTER para continuar.\n')

                return 'Chaves' if mecanismo.gastar_tempo(2) else 'Tempo'

            else:
                return 'Botao escondido'

        except KeyboardInterrupt:
            return 'Desespero'

        except EOFError:
            return 'Desespero'
