import Pyro4

class Server(object):
    @Pyro4.expose
    def welcomeMessage(self, name):
        certo = 0
        errado = 0
        questao = name.split(";") #separar a string em um array, tendo o corte no ;
        alternativa = questao[2] #ela pega a posição 2 onde estão as alternativas V ou F

        for x in alternativa: #percorre o array para verificar quais estão certas ou erradas
            if(x == "V"):
                certo = certo + 1
            else:
                errado = errado + 1    

        resultado = "Questao N:",questao[0], "\n N alternativas ", questao[1], " \n N certas ", certo, " \n N erradas ", errado
        return  resultado

def startServer():
    server = Server()
    daemon = Pyro4.Daemon()             
    ns = Pyro4.locateNS()
    uri = daemon.register(server)  
    ns.register("server", uri)   
    print("Ready. Object uri =", uri)
    daemon.requestLoop()                   

if __name__ == "__main__":
    startServer()