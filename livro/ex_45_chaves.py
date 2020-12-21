from os import name as os_name
from os import system as os_system
from textwrap import dedent


class Chaves:
    def entrar_fase(self, mecanismo):
        """
        Método para entrar na sala do cthulhu.
        Tente descobrir como afastar o grande mal.
        """

        try:

            os_system('cls' if os_name == 'nt' else 'clear')

            print(f'O colete mostra {mecanismo.tempo} de tempo.')

            if self.__fechaduras:

                print(dedent('''
                    No final da sala há uma porta enorme com 5 locais
                    de fechaduras. Para abri-la, obviamente, voce deve
                    ter as 5 chaves. O que você vai fazer?

                    Ações:
                    1. Voltar à sala inicial
                    2. Usar chaves
                '''))

                acao = input('[Ação]: ')

                os_system('cls' if os_name == 'nt' else 'clear')

                if acao == '1':

                    print(dedent('''
                        Você escolheu voltar à sala inicial. Você percebe
                        que o caminho de volta é mais longo que o normal e
                        leva o dobro de tempo para voltar.
                    '''))

                    input('Pressione ENTER para continuar.\n')

                    return 'Inicio' if mecanismo.gastar_tempo(2) else 'Tempo'

                elif acao == '2' and not mecanismo.contar_chaves() == 5:

                    print(dedent('''
                        Você percebe que não tem todas as 5 chaves e
                        resolve voltar à sala inicial. Você percebe que o
                        caminho de volta é mais longo que o normal e leva
                        o dobro de tempo para voltar.
                    '''))

                    input('Pressione ENTER para continuar.\n')

                    return 'Inicio' if mecanismo.gastar_tempo(2) else 'Tempo'

                elif acao == '2' and mecanismo.contar_chaves() == 5:

                    print(dedent('''
                        Você tem todas as chaves e começou a encaixar as
                        chaves em seus respectivos lugares. Não há erro,
                        cada fechadura tem um formato específico ficando
                        fácil identificar qual chave usar. A cada chave
                        encaixada um som de clique soa sinalizando que
                        uma tranca foi destravada. Ao terminar a tarefa
                        a porta sinaliza que está pronta para ser aberta.
                    '''))

                    self.__fechaduras = False

                    input('Pressione ENTER para continuar.\n')

                    return 'Chaves' if mecanismo.gastar_tempo(1) else 'Tempo'

                else:

                    return 'Botao escondido'

            else:

                print(dedent('''
                    Ao abrir a porta você entrou automaticamente e nem
                    percebeu. Todo o caminho para trás ficou perdido
                    assim que a porta fechou e se trancou.
                '''))

                input('Pressione ENTER para continuar.\n')

                return 'Potes' if mecanismo.gastar_tempo(1) else 'Tempo'

        except KeyboardInterrupt:

            return 'Desespero'

        except EOFError:

            return 'Desespero'

    def __init__(self):
        self.__fechaduras = True
