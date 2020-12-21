from os import name as os_name
from os import system as os_system
from sys import exit
from textwrap import dedent


class Final:

    @staticmethod
    def entrar_fase(mecanismo):
        try:
            os_system('cls' if os_name == 'nt' else 'clear')
            # Limpa a tela

            print(f'O colete mostra {mecanismo.tempo} de tempo.')
            print(dedent(f'''
                Você abriu a ultima porta e saiu do cativeiro.
                Momentos depois, você escuta uma voz no colete.

                ... Parabéns você conseguiu. Você venceu o jogo.

                ... Como o sistema identificou a sua saída, seu
                colete foi desarmado.

                ... Procure por um botão no colete.

                ... Faça rápido se quiser sobreviver.

                Você ao escutar a mensagem procura por um botão no
                colete e momentos depois você consegue achá-lo.
                Você apertou o botão e o colete desarmou.
                Você retirou o colete e procurou por ajuda.
                Minutos depois chega a polícia e te resgata.
            '''))

            print('Você venceu!')

            input('\nPRESSIONE ENTER PARA TERMINAR.\n')

            exit(0)

        except KeyboardInterrupt:
            print()

            exit(0)

        except EOFError:
            print()

            exit(0)
