voted = {}

def verifica_eleitor(nome):
    if voted.get(nome):
        print("Mande embora!")
    else:
        voted[nome] = True
        print("Deixe votar!")


verifica_eleitor("Tom")
verifica_eleitor("Juan")
verifica_eleitor("Juan")