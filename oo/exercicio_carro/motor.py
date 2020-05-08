class Motor:   # CLASSE MOTOR PARA CONTROLAR A VELOCIDADE DO CARRO
    def __init__(self):
        self.velocidade = 0 #CONTROLE DE VELOCIDADE DO CARRO METODO VELOCIDADE DO CARRO

    def acelerar(self):
        self.velocidade +=1 #CONTROLE DE VELOCIDADE DO CARRO SENDO O METODO ACELERAR

    def frear(self): #
        self.velocidade -= 2 #CONTROLE DE VELOCIDADE DO CARRO SENDO O METODO FREAR
        self.velocidade = max(0, self.velocidade) #CONTROLE DE VELOCIDADE DO CARRO SENDO O METODO FREAR
