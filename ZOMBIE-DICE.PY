
import time
from time import sleep
from random import randint, shuffle
def linha(msg):
   tam= len(msg) + 4
   print('~' * tam)
   print(f'  {msg}')
   print('~' * tam)

# começando e explicando e regra
linha('Você precisa marcar seus pontos de alguma maneira')
time.sleep(1)
linha('Dois ou mais jogadores podem jogar.')
time.sleep(1)
linha('O primeiro jogador será aquele que venceu a última partida ou a pessoa que falar “Céééééérebros” da maneira mais zumbi possível.')
time.sleep(1)
linha("O jogo e composto por tres cores de dados com o total de 13 dados")
time.sleep(1)
linha("¨6 dados verde composto por CPCTPC")
time.sleep(1)
linha("4 dado amarelo composto por TPCTPC")
time.sleep(1)
linha("3 o dado vermelho composto por TPTCPT")
time.sleep(1)
linha("Sendo q o C= cerebro o P= passos e o T= tiro")
time.sleep(1)
linha("O jogador que atingir 13 cerebros primeiro ganha o jogo")
time.sleep(1)
linha("O que levar 3 tiros perde todos os pontos do turno e passa a vez")
time.sleep(1)
linha(" Passos você retornara o dado para o copo")
time.sleep(1)


#Definindo tipo de dados
class Dados(object):
    def __init__(self, cor, lados):
        self.cor = cor
        self.lados = lados



#Definindo aleatorio os dados
    def lista(self):
        return self.lados[randint(0, 5)]


#Jogador e contador de pontos dos jogadores
class Jogador(object):
    def __init__(self, nome, ponto):
        self.nome = nome
        self.ponto = ponto


#Turno dos jogadores e definindos os dados
    def decisao_turno(self):
        print()
        print("turno do",self.nome )
        self.tempo_ponto = {'cérebros': 0, 'tiro ': 0}
        self.meu_dado = criando_dado()
        self.dados_rolados = []
        decisao_rodada = 's'
        while self.tempo_ponto['tiro '] < 3 and decisao_rodada == 's' and len(self.meu_dado) > 0:
            self.dados_rolados = self.escolhendo_dados(self.dados_rolados)
            resultados_dados = self.lancando_dados(self.dados_rolados)
            resultados_dados, self.dados_rolados = self.separando_dados(resultados_dados, self.dados_rolados)
            print(f'Ainda contem', len(self.meu_dado), 'dados no copo')
            if self.tempo_ponto['tiro '] >= 3:
                print("Você tomou muitos tiros!")
                self.tempo_ponto['cérebros'] = 0
                break
            decisao_rodada  = self.fazer_decisao()
        self.ponto += self.tempo_ponto['cérebros']


#Quais dados cairam
    def escolhendo_dados(self, dados_na_mao):
        while len(dados_na_mao) < 3:
            dados_na_mao.append(self.meu_dado.pop())
        return dados_na_mao


#Quais dados cairam e qual lado:
    def lancando_dados(self, dados_na_mao):
        resultados_lista = []
        resultados_básicos = []
        for jogada_dado in dados_na_mao:
            resultados_básicos.append(jogada_dado.lista())
            resultados_lista.append(jogada_dado.cor + ' ' + resultados_básicos[-1])
        print(resultados_lista)
        return resultados_básicos


#Retornando os dados com a lado pegadas:
    def separando_dados(self, dados_na_mao, dados_objetos):
        for i in range(2, -1, -1):
            if dados_na_mao[i] != "Pegadas":
                self.tempo_ponto[dados_na_mao[i]] += 1
                dados_na_mao.pop(i)
                dados_objetos.pop(i)
        return dados_na_mao, dados_objetos


#Desição para continuar jogando ou não:
    def fazer_decisao(self):
        decidir = ''
        print(self.tempo_ponto)
        while decidir != 's' and decidir != 'n':
            decidir = input('Quer continuar jogando (s/n)? ')
        return decidir


#Dados e seus repectivos valor:
def criando_dado():
    vermelho1 = Dados('Vemelho', ['tiro ', 'tiro ', 'tiro ', 'Pegadas', 'Pegadas', 'cérebros'])
    vermelho2 = Dados('Vemelho', ['tiro ', 'tiro ', 'tiro ', 'Pegadas', 'Pegadas', 'cérebros'])
    vermelho3 = Dados('Vemelho', ['tiro ', 'tiro ', 'tiro ', 'Pegadas', 'Pegadas', 'cérebros'])
    amarelo1 = Dados('Vemelho', ['tiro ', 'tiro ', 'Pegadas', 'cérebros', 'cérebros', 'cérebros'])
    amarelo2 = Dados('Amarelo', ['tiro ', 'tiro ', 'Pegadas', 'cérebros', 'cérebros', 'cérebros'])
    amarelo3 = Dados('Amarelo', ['tiro ', 'tiro ', 'Pegadas', 'cérebros', 'cérebros', 'cérebros'])
    amarelo4 = Dados('Amarelo', ['tiro ', 'tiro ', 'Pegadas', 'cérebros', 'cérebros', 'cérebros'])
    verde1 = Dados('Verde', ['tiro ', 'Pegadas', 'Pegadas', 'cérebros', 'cérebros', 'cérebros'])
    verde2 = Dados('Verde', ['tiro ', 'Pegadas', 'Pegadas', 'cérebros', 'cérebros', 'cérebros'])
    verde3 = Dados('Verde', ['tiro ', 'Pegadas', 'Pegadas', 'cérebros', 'cérebros', 'cérebros'])
    verde4 = Dados('Verde', ['tiro ', 'Pegadas', 'Pegadas', 'cérebros', 'cérebros', 'cérebros'])
    verde5 = Dados('Verde', ['tiro ', 'Pegadas', 'Pegadas', 'cérebros', 'cérebros', 'cérebros'])
    verde6 = Dados('Verde', ['tiro ', 'Pegadas', 'Pegadas', 'cérebros', 'cérebros', 'cérebros'])
    dados_feitos = [vermelho1, vermelho2, vermelho3, amarelo1, amarelo2, amarelo3, amarelo4, verde1, verde2, verde3, verde4, verde5, verde6]
    shuffle(dados_feitos)
    return dados_feitos


#Pegando a desição de continuar ou não e continuando o jogo:
def rodada_game(turno_decisao):
    for cada_jogador in turno_decisao:
        cada_jogador.decisao_turno()
    print()
    print("Fim da rodada.")
    exibição_ponto(turno_decisao)
    return turno_decisao


#Entradas de jogador:
def fazer_jogadores():
    total_jogadores = int(input("Quantos jogadores? "))
    jogadores = []
    for i in range(1, total_jogadores + 1):
        pnome = input("Jogador %s nome: " % i)
        este_jogador = Jogador(pnome, 0)
        jogadores.append(este_jogador)
    shuffle(jogadores)
    print()
    print("O jogo escolheu de forma aleatoria a ordem dos jogadores:")
    for i in range(len(jogadores)):
        print(i + 1, ':', jogadores[i].nome)
    print()
    return jogadores


#Quantos pontos cada jogador tem no fim da rodada:
def exibição_ponto(pontos):
    print("Seus pontos São:")
    for i in range(len(pontos)):
        print(pontos[i].nome, pontos[i].ponto)
    print()


#Fim de jogo, quando um dos jogadores atigirem 13 Cerebros:
def main():
    jogadores = fazer_jogadores()
    fim_jogo = False
    while fim_jogo == False:
        rodada_game(jogadores)
        for cada_jogador in jogadores:
            if cada_jogador.ponto >= 13:
                fim_jogo = True
    print("Fim de jogo. Pontos finais:")
    for cada_jogador in jogadores:
        print(cada_jogador.nome, cada_jogador.ponto)
    return 0


if __name__ == '__main__':
    main()
