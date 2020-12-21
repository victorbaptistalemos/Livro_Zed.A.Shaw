from os import name as os_name
from os import system as os_system
from textwrap import dedent

from ex_45_jogo import Jogo
from ex_45_mapa import Mapa
from ex_45_mecanismo import Mecanismo
from ex_45_morte import Morte


class Main:
    def __init__(self):
        try:
            os_system('cls' if os_name == 'nt' else 'clear')

            print(dedent('''
                Você acorda e se depara com as mãos amarradas em
                uma sala e vê uma mesa com alguns objetos.
                Pendurado na borda da mesa há uma placa dizendo.

                \t Vamos jogar um jogo?
                \t Você tem 30 rodadas para escapar. Boa sorte

                Você se desespera e consegue se desamarrar, mas ao
                se desamarrar um apito soa e você percebe que está
                com um colete munido com dinamites.
            '''))

            input('Pressione ENTER para continuar.\n')
            self.__mecanismo = Mecanismo()
            self.__mapa = Mapa()
            jogo = Jogo(self.__mapa, self.__mecanismo)
            jogo.jogar()

        except KeyboardInterrupt:
            Morte('Desespero')

        except EOFError:
            Morte('Desespero')


if __name__ == '__main__':
    x = Main()
