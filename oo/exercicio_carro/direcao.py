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
