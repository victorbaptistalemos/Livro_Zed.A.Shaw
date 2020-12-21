from textwrap import dedent


class Textos:
    textos = {
        'ex_ativo':
        dedent('''
            Texto do perigo ativo.
        '''),
        'ex_inativando':
        dedent('''
            Texto do perigo sendo desativado.
        '''),
        'ex_inativo':
        dedent('''
            Texto do perigo inativo.
        '''),
        'Abelha_ativo':
        dedent('''
            Você entrou na sala das abelhas assassinas.
            O que você vai fazer?

            Ações:
            1. Voltar
            2. Usar ferramenta
        '''),
        'Abelha_inativando':
        dedent('''
            Você sente uma leve tontura por causa do cheiro do
            repelente. Você vê as abelhas assassinas caírem
            mortas no chão, mas a abelha rainha não foi
            afetada, e, por sorte sua, não despertou.
        '''),
        'Abelha_inativo':
        dedent('''
            Não há mais abelhas nesta sala.
            O que você vai fazer?

            1. Voltar
            2. Sala das chaves
        '''),
        'Urso_ativo':
        dedent('''
            Você entrou na sala do urso.
            O que você vai fazer?

            Ações:
            1. Voltar
            2. Usar ferramenta
        '''),
        'Urso_inativando':
        dedent('''
            Você colocou o pote de mel no chão e empurrou para
            o canto da sala. O barulho do pote deslisando pela
            sala chamou a atenção do urso e este foi atrás do
            pote de mel. Ainda bem que ele não te notou.
        '''),
        'Urso_inativo':
        dedent('''
            O urso está se deliciando com o pote de mel.
            O que você vai fazer?

            1. Voltar
            2. Sala das chaves
        '''),
        'Gelo_ativo':
        dedent('''
            Você conseguiu abrir um buraco na pilastra
            Você entrou na sala de gelo. Você percebe que a
            sala está repleta de gelo. No meio da sala você vê
            uma pilastra de gelo e no meio desta você vê a
            chave da sala. Você está tremendo de frio e vai
            morrer congelado se ficar muito tempo
            O que você vai fazer?

            Ações:
            1. Voltar
            2. Usar ferramenta
        '''),
        'Gelo_inativando':
        dedent('''
            Você acionou o lança chamas e apontou o fogo para
            a pilastra de gelo. Quando o combustível terminou
            você percebeu que havia um buraco na pilastra e a
            chave já não estava mais lá. Cuidadosamente você
            analisa o chão em volta e acha a chave.
        '''),
        'Gelo_inativo':
        dedent('''
            Está frio e você não tem mais nada o que fazer aqui.
            O que você vai fazer?

            1. Voltar
            2. Sala das chaves
        '''),
        'Acido_ativo':
        dedent('''
            Você entrou na sala do caldeirão de ácido.
            Ao centro está o caldeirão aceso com ácido dentro.
            O que você vai fazer?

            Ações:
            1. Voltar
            2. Usar ferramenta
        '''),
        'Acido_inativando':
        dedent('''
            Ao jogar a solução básica no caldeirão, você vê
            que uma grande quantidade de vapor subiu deixando
            o caldeirão seco. Foi tanto vapor que o fogo do
            caldeirão foi apagado. Você teve que esperar mais
            uma rodada esperando o caldeirão esfriar e achar
            a chave no meio do sal.
        '''),
        'Acido_inativo':
        dedent('''
            O local está bastante úmido e você não tem mais
            nada o que fazer aqui.
            O que você vai fazer?
    
            1. Voltar
            2. Sala das chaves
        '''),
        'Cthulhu_ativo':
        dedent('''
            Ao entrar na sala você se depara com Cthulhu te
            observando e você entra em pânico. Com o pânico
            você pode demorar a responder às ações.
            O que você vai fazer?

            Ações:
            1. Voltar
            2. Usar ferramenta
        '''),
        'Cthulhu_inativando':
        dedent('''
            Você resolveu comer os mirtilos. Cthulhu vê você
            comendo os mirtilos e, milagrosamente, desaparece
            deixando mais mirtilos onde ele estava. Você pega
            os mirtilos e repara que embaixo dos mirtilos a
            chave estava escondida.
        '''),
        'Cthulhu_inativo':
        dedent('''
            Cthulhu não reapareceu e a paz paira no ar.
            Não há mais o que fazer aqui.
            O que você vai fazer?

            1. Voltar
            2. Sala das chaves
        ''')
        }
