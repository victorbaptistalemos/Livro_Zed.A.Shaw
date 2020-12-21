from os import name as os_name
from os import system as os_system
from random import randint
from sys import exit
from textwrap import dedent


class Morte:
    causa = {
        # Tempo esgotado
        'Tempo': dedent('''
            Seu tempo acabou! Você escuta um som de clique do
            colete. Nem adianta se desesperar, fumaça começa a
            sair do colete e você morre. Voou carne e sangue
            pela sala inteira, cena linda, hahahahahahahahaha.
        '''),
        # Erro de digitação
        'Botao escondido': dedent('''
            Enquanto você decidia o que fazer, você percebe
            que há um botão escondido no colete. Achando que
            foi uma falha da pessoa que te colocou ali,
            resolve apertar o botão. Ao apertar o botão você
            percebe o erro que fez. O contador mostra 0 e
            você morre explodindo ali mesmo.
        '''),
        # Saída inesperada (^C ou ^D)
        'Desespero': dedent(f'''
            Você se desesperou e resolveu arrancar os fios do
            mecanismo e morreu ao arrancar o {randint(1, 5)}º fio. Voou
            carne e sangue pela sala inteira. Após algum tempo
            encontraram o cativeiro e partes do seu corpo
            estavam espalhados por aí. Uma pena!
        '''),
        # Morte por não utilizar ferramenta nos perigos

        'Nenhuma ferramenta_Abelha': dedent('''
            Você tentou enfrentar as abelhas assasinas de mãos
            vazias? Aí tem coragem! Só que coragem não mata
            abelhas, você morreu! Uma pena, sua coragem serviu
            para nada.
        '''),
        'Nenhuma ferramenta_Urso': dedent('''
            Você tentou enfrentar o urso de mãos vazias? Pela
            fé! Tentasse enfrentá-lo com alguma ferramenta.
            Você não é Chuck Norris para enfrentar urso de
            mãos vazias. Você morreu! Uma pena, se ao menos
            você fosse Chuck Norris.
        '''),
        'Nenhuma ferramenta_Gelo': dedent('''
            Resolveu fazer um aquecimento socando a pilastra
            de gelo ou passou o efeito do remedinho? De toda
            sorte você conseguiu liberar a chave. Você foi na
            euforia pegar a chave, se esquecendo dos perigos
            da sala, mas, acabou escorregando e morrendo após
            bater com a cara na pilastra, quebrando o pescoço.
            Sem sorte hoje, né?
        '''),
        'Nenhuma ferramenta_Acido': dedent('''
            Isso é desespero para tentar sair desse local? Que
            loucura! Tem um caldeirão com fogo e ácido e você
            resolveu brincar de cientista? Ao tentar pegar a
            chave dentro do caldeirão de ácido quente, você
            se aproximou demais do fogo e o colete explodiu.
            Que morte idiota. Tá assistindo muito Happy Tree
            Friends.
        '''),
        'Nenhuma ferramenta_Cthulhu': dedent('''
            Você quis enfrentar Cthulhu de mãos vazias? De
            todas as loucuras essa, provavelmente, deve ser a
            pior de todas. Cthulhu te matou. Sua morte poderia
            ter sido um pouco menos inútil se você tivesse
            oferecido a sua alma. Pelo menos uma oferendazinha
            poderia ter ido junto. Que bosta!
        '''),
        # Morte por utilização errada da ferramenta Inseticida
        'Inseticida_Urso': dedent('''
            Inseticida no urso? O máximo que aconteceu foi
            fazer o urso espirrar. Você morreu na primeira
            patada que o urso te deu.
        '''),
        'Inseticida_Gelo': dedent('''
            Você jogou o frasco do repelente na pilastra de
            gelo. O frasco bateu na pilastra, ricocheteou e
            bateu na sua cara. Você conseguiu de alguma forma
            segurar o frasco, mas não antes de aplicar um
            pouco do produto na sua cara, fazendo você perder
            a visão - isso sem contar que os olhos ficaram
            bem vermelhos e ardendo. Você está sem a visão e,
            também, sem saber o que fazer. Vale ressaltar que
            não existia apenas a pilastra de gelo na sala.
            Resumindo, a sala de gelo se tornou a sala de gelo
            vermelho.
        '''),
        'Repelente_Acido': dedent('''
            Depois que você teve a brilhante ideia de espirrar
            repelente no caldeirão de ácido, uma reação em
            cadeia fez com que o ácido liberasse um gás mortal
            na sala. Você morreu asfixiado, pelo menos o gás
            desarmou o mecânismo do seu colete. Voçê está
            livre!
        '''),
        'Repelente_Cthulhu': dedent('''
            Hahahahahahahahahahahahahahahahahahahahahahahaha!
            Você usou todo o frasco de repelente no Cthulhu,
            mas não deu certo. Aconteceu absolutamente nada.
            Você tentou escapar, mas Cthulhu apareceu do nada
            na sua frente e você morreu depois que seus olhos
            derreteram ao olhar nos olhos de Cthulhu!
        '''),
        # Morte por utilização errada da ferramenta Mel
        'Mel_Abelha': dedent('''
            Você cuidadosamente colocou o pote de mel no chão.
            O mel acabou sendo espalhado no chão de qualquer
            forma. No meio do processo as abelhas começaram a
            te atacar, você morreu ali mesmo. Esqueceu que no
            pote estava escrito abelhas assassinas?
        '''),
        'Mel_Gelo': dedent('''
            Mel no gelo? Você é idiota ou o quê? Você jogou o
            pote de mel na pilastra de gelo numa tentativa de
            quebrar a pilastra. Você teve sorte, a pilastra
            quebrou e liberou a chave. Ao mesmo tempo algumas
            estalactites caíram. Você, ao desviar, deixou de
            prestar a atenção nos perigos da sala e morreu
            depois que seu corpo foi perfurado em uma das
            estalagmites.
        '''),
        'Mel_Acido': dedent('''
            Você de alguma forma conseguiu neutralizar o ácido
            no caldeirão. Parabéns, mas morreu sufocado pela,
            fumaça liberada na reação. Que pena.
        '''),
        'Mel_Cthulhu': dedent('''
            Que bonitinho! Você ofereceu o mel e sua alma para
            Cthulhu e ... morreu, parabéns!
        '''),
        # Morte por utilização errada da ferramenta Lança-chamas
        'Lança-chamas_Abelha': dedent('''
            No seu desespero por matar as abelhas assassinas
            com o lança-chamas, você matou algumas abelhas
            desavisadas, mas isso fez despertar a grande
            abelha rainha e o seu combustível acabou. Você
            morreu pelo veneno mortal da abelha rainha.
        '''),
        'Lança-chamas_Urso': dedent('''
            Seria uma boa ideia usar lança-chamas no urso se
            não fosse pelo fato de você ter pouco combustível.
            O urso te matou assim que o combustível acabou.
        '''),
        'Lança-chamas_Acido': dedent('''
            Não tente isso em casa. Você usou o lança-chamas
            no caldeirão de ácido, mas não teve efeito. Daí
            você teve a brilhante ideia de jogar o galão de
            combustível no caldeirão. Uma esplosão fez com que
            ácido fosse jogado em várias direções. Você até
            tentou escapar da sala, mas um pouco de ácido caiu
            na sua cabeça. O ácido quente derreteu sua cabeça
            por completo. Você virou uma pessoa-sem-cabeça.
            Nem precisava, mas, você morreu!
        '''),
        'Lança-chamas_Cthulhu': dedent('''
            O fogo do lança-chamas não fez nem cócegas nele.
            Você morreu pelas chamas de Cthulhu. Pelo menos
            você está crocrante.
        '''),
        # Morte por utilização errada da ferramenta Pote de solução básica
        'Pote de solução básica_Abelha': dedent('''
            Você tentou matar as abelhas assassinas jogando o
            líquido do pote? Sério isso? Francamente! A única
            coisa que você conseguiu foi atrair a fúria das
            abelhas. Você morreu.
        '''),
        'Pote de solução básica_Urso': dedent('''
            Você jogou o pote de solução básica no urso. Com
            essa ação você irritou o urso. No desespero, você
            saiu correndo. Você já estava chegando na porta de
            entrada para escapar, mas o urso foi mais rápido e
            te derrubou. Não foi dessa vez, bebê! Você morreu.
        '''),
        'Pote de solução básica_Gelo': dedent('''
            Você jogou o pote de solução básica na pilastra de
            gelo. 'Ai que burro, dá 0 pra ele'. Você morreu ao
            escorregar na solução básica que se espalhou pelo
            gelo.
        '''),
        'Pote de solução básica_Cthulhu': dedent('''
            Você jogou o pote de solução básica no Cthulhu.
            Durante o ato Cthulhu te olhou e cuspiu em você.
            O cuspe era tão ácido que a solução básica nem fez
            efeito. Você morreu pelo cuspe ácido.
        '''),
        # Morte por utilização errada da ferramenta Mirtilos
        'Mirtilos_Abelha': dedent('''
            Sua morte foi engraçada! Ao comer mirtilos no meio
            das abelhas assassinas acabou comendo algumas das
            abelhas que estava ao redor e morreu com a boca
            inchada! Sério mesmo que você teve essa brilhante
            ideia de comer mirtilos justamente no meio das
            abelhas? Parabéns!
        '''),
        'Mirtilos_Urso': dedent('''
            Você parou para comer mirtilos em frente ao urso?
            Você estava terinando de comer os Mirtilos quando
            percebeu o urso bem atrás de você. No desespero
            você tentou correr, mas o urso te derrubou, te
            matou e depois de te desossar comeu os mirtilos
            restantes. O bicho estava varado de fome.
        '''),
        'Mirtilos_Gelo': dedent('''
            'Você quer brincar na neve?' Não, pera. Isso é um
            jogo de escapar ou aquele filme da menina das mãos
            que atira gelo? Que seja, você quis misturar os
            mirtilos com um pouco de gelo raspado. Você morreu
            frio. Pelo menos a raspadinha estava deliciosa.
        '''),
        'Mirtilos_Acido': dedent('''
            Não sei qual era a fórmula química do ácido no
            caldeirão, mas assim que os mirtilos entraram em
            contato com a solução ácida uma explosão aconteceu
            e você morreu com o impacto. Foi tão violenta que
            seu corpo foi parar parar na sala inicial.
        '''),

        # Escolheu pote usado
        'Pote quebrado': dedent('''
            Você cismou que a chave estava escondida no pote
            usado, mas na sua cisma você, sem querer, cortou
            seus pulsos. O corte foi tão profundo que você
            não conseguiu estancar o sangramento. Você
            escorregou no próprio sangue e bateu a cabeça no
            chão. Não se sabe se você morreu de hemorragia ou
            pela queda.
        ''')
    }

    def __init__(self, causa):
        try:
            os_system('cls' if os_name == 'nt' else 'clear')
            # Limpa a tela
            print(self.causa.get(causa, 'Chave não encontrada'))

            input('Pressione ENTER para continuar.\n')
            exit(0)

        except KeyboardInterrupt:
            print()
            exit(0)

        except EOFError:
            print()
            exit(0)


if __name__ == '__main__':
    x = Morte('Tempo')
