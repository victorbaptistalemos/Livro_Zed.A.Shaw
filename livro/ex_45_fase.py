from os import name as os_name
from os import system as os_system
from random import randint
from textwrap import dedent

from ex_45_textos import Textos


class Fase:
    def __ponto_fraco(self):
        ponto_fraco = {
            'Abelha': 'Inseticida',
            'Urso': 'Mel',
            'Gelo': 'Lança-chamas',
            'Acido': 'Pote de solução básica',
            'Cthulhu': 'Mirtilos'
        }
        return ponto_fraco.get(self.__nome, 'Nenhuma ferramenta')

    def entrar_fase(self, mecanismo):
        """
        Método para entrar nas fases de perigo.
        São 5 fases iguais, portanto há um padrão de execução.
        """

        try:

            os_system('cls' if os_name == 'nt' else 'clear')

            print(f'O colete mostra {mecanismo.tempo} de tempo.')

            if self.__perigo_ativo:

                print(Textos.textos[f'{self.__nome}_ativo'])

                acao = input('[Ação]: ')

                os_system('cls' if os_name == 'nt' else 'clear')

                if acao == '1':

                    print(dedent('''
                        Você escolheu voltar à sala inicial.
                    '''))

                    input('Pressione ENTER para continuar.\n')

                    if self.__nome == 'cthulhu':

                        return 'Inicio' if mecanismo.gastar_tempo(randint(2, 3)) else 'Tempo'

                    else:

                        return 'Inicio' if mecanismo.gastar_tempo(1) else 'Tempo'

                elif acao == '2' and mecanismo.ferramenta_nome() == self.__ponto_fraco:

                    print(Textos.textos[f'{self.__nome}_inativando'])

                    self.__perigo_ativo = False

                    mecanismo.usar_ferramenta()

                    mecanismo.coletar_chave(self.__nome)

                    print(dedent(f'''
                        Você coletou a chave desta sala.

                        Total de chaves coletadas: {mecanismo.contar_chaves()}.
                    '''))

                    input('Pressione ENTER para continuar.\n')

                    if self.__nome == 'Cthulhu':

                        return 'Cthulhu' if mecanismo.gastar_tempo(randint(2, 3)) else 'Tempo'

                    elif self.__nome == 'Acido':

                        return 'Acido' if mecanismo.gastar_tempo(2) else 'Tempo'

                    else:

                        return self.__nome if mecanismo.gastar_tempo(1) else 'Tempo'

                elif acao == '2':

                    return f'{mecanismo.ferramenta_nome()}_{self.__nome}'

                else:

                    return 'Botão escondido'

            else:

                print(Textos.textos[f'{self.__nome}_inativo'])

                acao = input('[Ação]: ')

                os_system('cls' if os_name == 'nt' else 'clear')

                if acao == '1':

                    print(dedent('''
                        Você escolheu voltar à sala inicial.
                    '''))

                    input('Pressione ENTER para continuar.\n')

                    return 'Inicio' if mecanismo.gastar_tempo(1) else 'Tempo'

                elif acao == '2':
                    print(dedent('''
                        Você escolheu seguir para a sala das chaves.
                    '''))

                    input('Pressione ENTER para continuar.\n')

                    return 'Chaves' if mecanismo.gastar_tempo(1) else 'Tempo'

                else:

                    return 'Botão escondido'

        except KeyboardInterrupt:

            return 'Desespero'

        except EOFError:

            return 'Desespero'

    def __init__(self):

        self.__nome = self.__class__.__name__
        self.__ponto_fraco = self.__ponto_fraco()
        self.__perigo_ativo = True
