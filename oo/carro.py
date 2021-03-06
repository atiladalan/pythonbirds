# import motor  # REALIZANDO CONCEITO DE IMPORTAÇÃO DE CLASSES
# import direcao  # REALIZANDO CONCEITO DE IMPORTAÇÃO DE CLASSES

"""
Você deve criar uma classe carro que vai possuir dos atributos composto por outras classes:

1) Motor
2) Direção

o Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade:
2) Método acelerar, que deverá incrementar a velocidade de uma unidade:
3) Método frear que deverá decrementar a velocidade em duas unidades:

Adireção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possiveis: Norte, Sul, Leste, Oeste.
2) Método girar_a_direita
3) Método girar_a_esquerda

       N
    O     L
       S

Exemplo:l
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'

"""


class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()


NORTE='Norte'
SUL='Sul'
LESTE='Leste'
OESTE='Oeste'

class Direcao:

    # def __init__(self):  #ATRIBUTO DE INSTANCIA REFERENTE AO ATRIBUTO VALOR
    #     self.valor = NORTE
    #
    # def girar_a_direita(self):
    #     if self.valor == NORTE:
    #         self.valor = LESTE
    #     elif self.valor == LESTE:
    #         self.valor = SUL
    #     elif self.valor == SUL:
    #         self.valor = OESTE
    #     elif self.valor == OESTE:
    #         self.valor = NORTE
    #
    # def girar_a_esquerda(self):
    #     if self.valor == NORTE:
    #         self.valor = OESTE
    #     elif self.valor == OESTE:
    #         self.valor = SUL
    #     elif self.valor == LESTE:
    #         self.valor = NORTE
    #     elif self.valor == SUL:
    #         self.valor = LESTE

#UTILIZANDO DICIONARIO PARA EXEMPLIFICAR O PROBLEMA ACIMA
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_a_esquerda_dct = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL
    }
    def __init__(self):  #ATRIBUTO DE INSTANCIA REFERENTE AO ATRIBUTO VALOR
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor] #UTILIZANDO O DICIONARIO PARA REALIZAR O DIRO A DIREITA
    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor] #UTILIZANDO O DICIONARIO PARA REALIZAR O DIRO A ESQUERDA


class Motor:   # CLASSE MOTOR PARA CONTROLAR A VELOCIDADE DO CARRO
    def __init__(self):
        self.velocidade = 0 #CONTROLE DE VELOCIDADE DO CARRO METODO VELOCIDADE DO CARRO

    def acelerar(self):
        self.velocidade +=1 #CONTROLE DE VELOCIDADE DO CARRO SENDO O METODO ACELERAR

    def frear(self): #
        self.velocidade -= 2 #CONTROLE DE VELOCIDADE DO CARRO SENDO O METODO FREAR
        self.velocidade = max(0, self.velocidade) #CONTROLE DE VELOCIDADE DO CARRO SENDO O METODO FREAR
