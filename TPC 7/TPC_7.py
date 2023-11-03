



Memoria={"Polinómio "+str(pol):None for pol in range(1,100) }

#Função para passar os polinómios de listas para uma versão mais amigável
def imprimirPolinomio(polinomio):
    def obterPotencia(grau):#Sempre que pedido, esta função substitui um número pelo seu equivalente em expoente, de modo a que os polinómios aparentem melhor ao imprimi-los

        potencias = {
            '0': '⁰',
            '1': '¹',
            '2': '²',
            '3': '³',
            '4': '⁴',
            '5': '⁵',
            '6': '⁶',
            '7': '⁷',
            '8': '⁸',
            '9': '⁹'}
        return ''.join(potencias[numero] for numero in str(grau))
    
    pol_res=str("")
    MaiorGrau_termo=0

    for termo in polinomio:
            res=str("")
            
            
            coef,grau=termo
            if grau>MaiorGrau_termo:
                    MaiorGrau_termo=grau
                    
                    
                    
            if coef!=0:
                if coef!=1:
                    if grau==0:
                        res+=str(coef)
                    else:
                        res+=str(coef)+"x"+ obterPotencia(grau)
                if coef==1:
                    if grau==0:
                        res+=str(coef)
                            
                    else:
                        res+="x"+ obterPotencia(grau)
                if coef>0:
                    res="+"+ res
            pol_res+=res

    if pol_res[0]=="+":
        pol_res=pol_res[1:]
    
    return pol_res,MaiorGrau_termo


#1
def criaPol():
    resPol = []
    grau = int(input("Qual o grau do seu polinómio?"))
    n = 1
    
    while grau >= 0:
        coef = float(input(f"Qual o coeficiente do {n}º termo?"))
        if coef != 0:
            resPol.append((coef, grau))
        
        grau -= 1
        n += 1
    return resPol

def adicionaPolinomio():
    pol=criaPol()
    for key in Memoria:
        if Memoria[key] is None:
            Memoria[key] = pol
            break
    return pol




#2
def LerPolinomios(fnome):
    
    file=open(fnome,"r")
    
    

    for line in file:
        termos=line.split(";")
        polinomio=[]
        for termo in termos:
            t=termo.split("/")
            if len(t)>1:
                coef=float(t[0])
                grau=int(t[1])
                polinomio.append((coef,grau))
        for key in Memoria:
            if Memoria[key] is None:
                Memoria[key]=polinomio
                break

    file.close()
    return 

#3
def ListarPolinomios():
  
    
    for ordem,polinomio in Memoria.items():
        if polinomio is not None:
            
            pol_res,grau=imprimirPolinomio(polinomio)

        
            print(ordem,"        ",pol_res,flush=True)

#4
def calcPolinomio(n,x):

    
    res = 0
    for termo in Memoria[f"Polinómio {n}"]:
        res=res+(termo[0]*x**termo[1])
        


    print(f"A soma do polinómio número {n} para x={x} é {res}",flush=True)

#5
def ListarPolinomios_Grau():
    
    
    for ordem,polinomio in Memoria.items():
        if polinomio is not None:

            pol_res,MaiorGrau=imprimirPolinomio(polinomio)
            
            print(ordem,"       ",pol_res,f"(grau {MaiorGrau})",flush=True)

#6
def MaiorGrauPol():
    MaiorGrau = -1
    Pol_MaiorGrau= None
    MaiorPol_ordem = None
    
    for ordem, polinomio in Memoria.items():
        if polinomio is not None:
            pol_res, MaiorGrau_termo= imprimirPolinomio(polinomio)
            
            if MaiorGrau_termo > MaiorGrau:
                MaiorGrau = MaiorGrau_termo
                Pol_MaiorGrau = pol_res
                MaiorPol_ordem = ordem

    print(f"O polinómio de maior grau é o {MaiorPol_ordem}, igual a {Pol_MaiorGrau}",flush=True)

#7
def derivarPolinomios():

    for ordem, polinomio in Memoria.items():
        dp=[]
        if polinomio is not None:
            for termo in polinomio:
                coef,grau=termo
                
        
                if grau>0:
                    dtermo=()
                    dcoef=int()
                    dgrau=int()
                    dcoef=coef*grau
                    dgrau=grau-1
                    dtermo=dcoef,dgrau
                    dp.append(dtermo)

            dpol_res, dMaiorGrau_termo= imprimirPolinomio(dp)
            pol_res,MaiorGrau_termo=imprimirPolinomio(polinomio)

            
            print(f"{pol_res:<35}{dpol_res}")
            
    
#8
def somaPolinomios(n1, n2):
    pol1 = Memoria[f"Polinómio {n1}"]
    pol2 = Memoria[f"Polinómio {n2}"]
    
    pol_res = []
    
   
    maior_grau = max(max(coef[1] for coef in pol1), max(coef[1] for coef in pol2))
    
    
    for grau in range(maior_grau, -1, -1):
        soma_coef = 0
        for coef, g in pol1:
            if g == grau:
                soma_coef += coef
        for coef, g in pol2:
            if g == grau:
                soma_coef += coef
        
        if soma_coef != 0:
            pol_res.append((soma_coef, grau))
    
    soma, MaiorGrau = imprimirPolinomio(pol_res)
    
    print(f"A soma do Polinómio {n1} com o Polinómio {n2} é {soma}   ")
    
    
#9
import matplotlib.pyplot as plt

def traçarFunção(n):
    pol=[]
    for termo in Memoria[f"Polinómio {n}"]:
        pol.append(termo)
        
    xValores =[]
    inicio = -10.0
    fim = 10.0
    passo = 0.1

    x = inicio
    while x <= fim:
        xValores.append(x)
        x += passo


    yValores = [sum(coef * (x ** grau) for coef,grau in pol) for x in xValores]

    plt.plot(xValores, yValores)

    plt.xlabel('abcissas')
    plt.ylabel('ordenadas')

    plt.show()
    return 

    
#10
def guardarPolinomios( fnome):
    file=open(fnome,"a")
    for ordem,polinomio in Memoria.items():
        if polinomio is not None:
            for termo in polinomio:
                file.write(f"{termo[0]}/{termo[1]};")
            file.write("\n")
    file.close()

    return



menu=-1
print("Olá! Aqui estão as suas opções:",flush=True)
print("""1. Criar um polinómio interativamente;
         2. Ler uma lista de polinómios de um ficheiro;
         3. Listar polinómios em memória;
         4. Calcular o valor de um polinómio num ponto;
         5. Listar polinómios e o seu grau;
         6. Listar o polinómio de maior grau;
         7. Listar os polinómios em memória e as suas respetivas derivadas;
         8. Somar dois polinómios;
         9. Traçar o gráfico de um polinómio;
         10. Gravar num ficheiro os polinómios em memória;
         0. Sair da aplicação""",flush=True)
while menu!=0:
    menu=int(input("Escolha uma opção: "))
    if menu==1:
        
        pol,maiorgrau=imprimirPolinomio(adicionaPolinomio())
        print(f"Feito! Adicionaste {pol} à memória de polinómios! Usa a opção 3 ou 5 para ver os polinómios carregados!",flush=True)
        
        
    if menu==2:
        fnome=input("Insere o nome do ficheiro de polinómio que queres adicionar à memória.(limite de 99 polinómios)")
        try:
            with open(fnome, "r"):
                print(f"O arquivo '{fnome}' existe.")
        except FileNotFoundError:
            print(f"O arquivo '{fnome}' não existe.")
        
        LerPolinomios(fnome)
        print(f"Feito! Adicionaste os polinómios de {fnome} à memória da aplicação!",flush=True)
        
    if menu==3:
        print("**********Lista de Polinomios***********",flush=True)
        print("***********Ordem-|-Polinomio************",flush=True)
        ListarPolinomios()
    if menu ==4:
        
        calcPolinomio(int(input("Qual dos polinomios em memória escolhes?")),float(input("Em que ponto é que queres calcular o valor do polinómio?")))
    elif menu ==5:
        print("****************Lista de Polinomios***********",flush=True)
        print("***********Ordem-|-Polinomio(Grau)************",flush=True)
        ListarPolinomios_Grau()
    elif menu==6:
        MaiorGrauPol()
    elif menu==7:
        print("**********Lista de Polinomios e respetiva Derivada***********",flush=True)
        print("*******************Polinómio****|****Derivada****************",flush=True)
        derivarPolinomios()
    elif menu==8:
        
        print("**********Lista de Polinomios***********",flush=True)
        print("***********Ordem*|*Polinomio************",flush=True)
        ListarPolinomios()
        print("Estes são os polinómios disponiveis, escolha dois para somar")
        somaPolinomios(int(input("Escolha um polinómio para somar")),int(input("Agora o segundo polinómio")))
    elif menu==9:
        print("**********Lista de Polinomios***********")
        print("***********Ordem*|*Polinomio************")
        ListarPolinomios()
        print("Estes são os polinómios disponiveis, escolha um para traçar num gráfico.")
        traçarFunção(int(input("Qual dos polinomios em memória quer escolher?")))
    elif menu==10:
        fnome2=input("Que nome quer dar ao seu ficheiro?")
        guardarPolinomios(fnome2)
        print(f"Feito! Guardou os polinómios em memória no ficheiro {fnome2}")

    elif menu==0:
        print("Saiu da app")
        


