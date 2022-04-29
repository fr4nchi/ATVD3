import Pyro4

name = input("O que você marcou na questão? ").strip()
server = Pyro4.Proxy("PYRONAME:server")
print(server.welcomeMessage(name))