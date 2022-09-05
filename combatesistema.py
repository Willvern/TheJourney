def combate_inicio(enemy):
    print("Você encontra um",enemy,"e todos se juntaram a você")
    escolha= str(input("O que você e sua guilda vão reagir "))
    match escolha:
        case lutar:
            lutar("")
        case acao:
            acao("")
        case inventario:
            inventario("")
        case fugir:
            fugir("")

def lutar():
    match lutar:
        case mago:
            atk=str(input("Escolheu os poderes de mago\n1º - Bola de Fogo\nº2 - Furação do Dragão\n 3º - Portal \n 4º - Vortex de água\nescolha o poder entre 1 e 4: "))
            if atk==1:
                print("Bola de Fogo!")
                
            elif atk==2:
                print("Furação do Dragão!")
            elif atk==3:
                print("Portal!")
            elif atk==4:
                print("Vortex de água!")
            
def acao():
    match acao:
        case 1:
            ("")


def inventario():
    match inventario:
        case porcao:
            print("O",personagem,"tomou a porção de cura!")
