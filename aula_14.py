import unittest
from naosei import Prova

class ProvaTest(unittest.TestCase):

    def test_armazenaQuestao(self):
        questao = "quanto é 2+1?"
        p = Prova()
        p.armazenaQuestaoResposta(questao,"")
        self.assertIn("quanto é 2+1?", p.questoes)

    def test_armazenaResposta(self):
        resposta = 3
        p = Prova()
        p.armazenaQuestaoResposta("", resposta)
        self.assertIn(3, p.resposta)

unittest.main(argv=[''], exit=False) 