from ex_45_morte import Morte


class Jogo:
    def jogar(self):
        """
        Entra em um looping até uma das 2 condições sejam cumpridas:
        1. final.Final.entrar_fase() seja chamada.
        2. self.__fase_atual.entrar_fase(self.__mecanismo) retorne uma instância de UserWarning.
        2.1 Acontece por tempo excedido.
        2.2 Acontece por uso de dispositivo errado
        2.3 Saída manual: EOFError -> Ctrl + D (^D)
        2.4 Saída manual: KeyboardInterrupt -> Ctrl + C (^C)
        """
        while True:
            self.__fase = self.__fase_atual.entrar_fase(self.__mecanismo)
            # Carrega a fase aberta e retorna um valor.

            if self.__fase not in self.__mapa.lista_cenarios():
                # Se o valor retornado não estiver na lista de cenários.
                break

            self.__fase_atual = self.__mapa.abrir_fase(self.__fase)
            # Retorna a instância da proxima fase a ser carregada a partir do valor retornado.

        Morte(self.__fase)

    def __init__(self, mapa, mecanismo):
        """
        Ao istanciar jogo.Jogo os objetos
        mapa.Mapa e mecanismo.Mecanismo
        são atrelados às variáveis do objeto
        jogo.Jogo.

        param: mapa = Instância de mapa.Mapa
        param: mecanismo = Instância de mecanismo.Mecanismo
        """

        self.__fase = None
        self.__mapa = mapa
        self.__mecanismo = mecanismo
        self.__fase_atual = self.__mapa.abrir_fase('Inicio')
        # A fase 'Inicio' é sempre a primeira a ser iniciada.
