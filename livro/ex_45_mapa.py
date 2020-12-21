from ex_45_chaves import Chaves
from ex_45_final import Final
from ex_45_inicio import Inicio
from ex_45_perigo import *
from ex_45_potes import Potes


class Mapa:
    def __gerar_cenarios(self):
        """
        Método que instancia todas as fases.
        """

        self.__cenarios['Inicio'] = self.__inicio
        self.__cenarios['Chaves'] = self.__chaves
        self.__cenarios['Potes'] = self.__potes
        self.__cenarios['Final'] = self.__final

        cenarios = {
            'Abelha': self.__abelha,
            'Acido': self.__acido,
            'Cthulhu': self.__cthulhu,
            'Gelo': self.__gelo,
            'Urso': self.__urso
        }

        for x, y in cenarios.items():
            self.__cenarios[x] = y

    def abrir_fase(self, fase):
        """
        Método que "inicializa" a fase.
        Retorna a variável correspondente à instância da fase.
        """

        return self.__cenarios.get(fase)

    def lista_cenarios(self):
        return list(self.__cenarios.keys())

    def __init__(self):
        """
        Inicia o objeto da classe mapa.Mapa.
        """
        self.__cenarios = {}
        self.__inicio = Inicio()
        self.__abelha = Abelha()
        self.__urso = Urso()
        self.__gelo = Gelo()
        self.__acido = Acido()
        self.__cthulhu = Cthulhu()
        self.__chaves = Chaves()
        self.__potes = Potes()
        self.__final = Final()
        self.__gerar_cenarios()
