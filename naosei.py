import unittest
def sobrenomeNaOrdem(nome, sobrenome1, sobrenome2):
    if(len(sobrenome2) >= len(sobrenome1)):
        return nome+' '+sobrenome1+' '+sobrenome2
    else:
        return nome+' '+sobrenome2+' '+sobrenome1

class NomeTest(unittest.TestCase):

    def test_sobrenomeNaOrdem(self):
        nomeCompleto = sobrenomeNaOrdem("João", "Gomes", "Bitella")
        #self.assertNotEqual(nomeCompleto, "João Gome Bitella")

#unittest.main(argv=[''], exit=False)

class Prova():

    def __init__(self):
        self.questoes = []
        self.respostas = []
    
    def mostrarQuestoes(self):
        print(self.questoes)

    def mostrarRespostas(self):
        print(self.respostas)

    def armazenaQuestaoResposta(self, novaQuestao, novaResposta):
        self.questoes.append(novaQuestao)
        self.respostas.append(novaResposta)