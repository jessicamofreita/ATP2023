sala1=["Sala 1",60,[],"Twilight"]
sala2=["Sala 2",60,[],"Endgame"]
sala3=["Sala 3",55,[],"Barbie"]
sala4=["Sala 4",40,[],"Patrulha Pata"]

Cinema=[sala1,sala2,sala3,sala4]
import random



def listar(cinema):
    print("--------Cartaz--------")
    for sala in cinema:
        print(sala[0]+str(": ")+sala[3],flush=True)
    return


def disponivel(Cinema,filme,lugar):
    disponibilidade=False
    for sala in Cinema:
        if filme == sala[3] and lugar  not in sala[2]:            
                disponibilidade=True
                print(Cinema)
    return disponibilidade

def vendeBilhete(Cinema,filme,modo):
    if modo=="Não": ###Escolhe um número aleatório dos lugares daquela sala
        for sala in Cinema:
            if filme==sala[3]:
                res = ""
                while res != "aceite":
                    lugar = random.randrange(1,sala[1]+1) 
                    if disponivel(Cinema, filme, lugar): 
                        sala[2].append(lugar)
                        print("O lugar "+str(lugar)+" foi reservado com sucesso, bom filme!", flush = True)
                        res = "aceite"
                    else:
                        res = "recusado"
        

    if modo=="Sim":###Escolhe o lugar que o utilizador inserir
        for sala in Cinema:
            if filme==sala[3]:
                lugar = int(input("Escolha o lugar que quer"))
                if disponivel(Cinema,filme,lugar):
                    sala[2].append(lugar)
                    print("O lugar "+str(lugar)+" foi reservado com sucesso, bom filme!")
                else:
                    print("Este lugar já está ocupado, escolha outro!")
    

def listarDisponibilidades(Cinema):
    print("Estes são os filmes disponiveis no cinema:")
    for sala in Cinema:
        x= sala[1] - len(sala[2]) 
        
        print(sala[0] + ", com "+str(x)+" lugares disponiveis.")
    return    
        



def inserirSala( cinema, sala, lotação, filme ):
    sala=[sala,lotação,[],filme]
    
    
    if sala not in cinema:
        cinema.append(sala)
    print("A sala foi adicionada com sucesso!")
    print(sala[0]+": com lotação de "+str(sala[1])+" lugares. Filme em exibição: "+sala[3],flush=True)
    



menu=-1
print("""Boa noite!! Obrigado por escolher o nosso Cinema, aqui estão os próximos passos: 
      (1) Listar todos os filmes em exibição;
      (2) Verificar a disponibilidade da sala e do lugar;
      (3) Comprar bilhete, somente após verificar a disponibilidade;
      (4) Listar os lugares restantes em cada sala
      (6) Fechar o menu.""")
while menu !=6:
    menu=int(input("Escolhe a tua opção."))

    if menu==1:
        listar(Cinema)

    elif menu ==2:
        print(disponivel(Cinema,input("Escreve o nome do filme que queres ver"),int(input("Escolhe um lugar da sala"))))

    elif menu ==3:
        vendeBilhete(Cinema,input("Escreve o nome do filme que queres ver"), input("Deseja escolher o lugar?(Sim ou Não)"))

    
    elif menu ==4:
        listarDisponibilidades(Cinema)

    elif menu ==5:
        inserirSala(Cinema,input("Qual o nome da nova sala?"),int(input("Qual a lotação da sala?")),input(("Qual o filme em exibição?")))
    
print("Obrigado e Volte Sempre!")