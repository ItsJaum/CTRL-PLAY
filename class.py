class casa():
    def __init__(self, rua, numero, bairro, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cep = cep

    def enderecoCompleto(self):
        return "Endereço completo: " +self.rua+ ", " +self.numero+ ", " +self.bairro+ " - CEP: " +self.cep
    
casa1 = casa(rua = "roblox", numero = "1574", bairro = "blebleble", cep = "8745310")

print(casa1.bairro)
print(casa1.enderecoCompleto())

casa2 = casa(rua = "terraria", numero = "210", bairro = "blablabla", cep = "0000097")
casa3 = casa(rua = "minecraft", numero = "560", bairro = "blublublu", cep = "0007900")

print(casa1.bairro)
print(casa1.enderecoCompleto())