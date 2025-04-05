class Animal():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.energia = 100
    
    def Dormir(self, horas):
        energiaGanha = horas * 10
        # self.energia = self.energia + energiaGanha
        self.energia += energiaGanha
        if self.energia > 100:
            self.energia = 100
        print(f"{self.nome} dormiu por {horas} e ganhou {energiaGanha} de energia. Energia atual: {self.energia}")

    def brincar(self, horas):
        energiaPerdida = horas * 10
        self.energia -= energiaPerdida
        if self.energia >= 100:
            self.energia = 100
            print(f"{self.nome} brincou por {tempo} minutos e gastou {energiaPerdida} de energia. Energia atual: {self.energia}")
        else:
            print(f"{self.nome} esta cansado demais para brincar!")
Animal1 = Animal("mavie", 8)

Animal1.brincar(10)
Animal1.Dormir(4)
        

    
