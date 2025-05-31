import random

def saudacoes(nome):
    frases = ["Bom dia! como vai você" + nome + "o que você fez hoje?", "olá!", "eai, como você tá?"]
    print(frases[random.randint(0,2)])

def recebe_texto():
    texto = "Cliente: " + input("Cliente: ")
    palavra_proibida = ["bocó", "paspalho", "fubango", "ordinario"]
    for i in palavra_proibida:
        if i in texto:
            print("Não vem não! não se perdeu")
            return recebe_texto()
    return texto

def busca_resposta(nome, texto):
    with open("BaseDeConhecimento.txt", "a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if texto.replace("Cliente: ", "") == "tchau":
                    print(nome+ ": Volte sempre!")
                    return "fim"
                elif viu.strip() == texto.strip():
                    proxima_linha = conhecimento.readline()
                    if "Chatbot: " in proxima_linha:
                        return proxima_linha
            else:
                print("Me desculpe! nao sei o que falar")
                conhecimento.write("\n" + texto)
                resposta_user = input("o que esperava?\n")
                conhecimento.write("\n" +"Chatbot: "+resposta_user)
                return "Hum..."

# saudacoes(input())
# recebe_texto()

busca_resposta("eu não gosto de mortal kombat não, seu bocó")

