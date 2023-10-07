import random


lista_numeros = []

def criar_lista():
    global lista_numeros
    lista_numeros = [random.randint(1, 100) for _ in range(10)]
    print("Lista criada com sucesso.")
    print(f"A sua lista é {lista_numeros}")

def ler_lista():
    global lista_numeros
    lista_numeros = []
    print("Escreva os números que deseja colocar na lista:")
    while True:
        try:
            n = int(input("Digite um número (0 para terminar): "))
            if n == 0:
                break
            lista_numeros.append(n)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    
    print("Lista lida com sucesso.")
    print(f"A sua lista é: {lista_numeros}")

def soma():
    global lista_numeros
    result = sum(lista_numeros)
    print(f"Soma dos elementos da lista: {result}")

def media():
    global lista_numeros    
    result = sum(lista_numeros) / len(lista_numeros)
    print(f"Média dos elementos da lista: {result}")

def maior():
    global lista_numeros
    if not lista_numeros:
        print("A lista está vazia.")
        return
    
    result = max(lista_numeros)
    print(f"Maior elemento da lista: {result}")

def menor():
    global lista_numeros
    if not lista_numeros:
        print("A lista está vazia.")
        return
    
    result = min(lista_numeros)
    print(f"Menor elemento da lista: {result}")

def esta_ordenada_crescente():
    global lista_numeros
    if not lista_numeros:
        print("A lista está vazia.")
        return
    if lista_numeros == sorted(lista_numeros):
        print("A lista está ordenada por ordem crescente?: Sim")
    else:
        print("A lista está ordenada por ordem crescente?: Não")
    lista_crescente = sorted (lista_numeros)
    print (f" A sua lista ordenada de forma crescente é {lista_crescente}")

def esta_ordenada_decrescente():
    global lista_numeros
    if not lista_numeros:
        print("A lista está vazia.")
        return
    if lista_numeros == sorted(lista_numeros, reverse=True):
        print("A lista está ordenada por ordem decrescente?: Sim")
    else:
        print("A lista está ordenada por ordem decrescente?: Não")
    lista_decrescente = sorted (lista_numeros, reverse = True)
    print (f" A sua lista ordenada de forma decrescente é {lista_decrescente}")
    

def procura_elemento():
    global lista_numeros
    if not lista_numeros:
        print("A lista está vazia.")
        return
    
    try:
        elemento = int(input("Digite o elemento que deseja procurar: "))
        if elemento in lista_numeros:
            index = lista_numeros.index(elemento)
            print(f"O elemento {elemento} está na posição {index}.")
        else:
            print(f"O elemento {elemento} não está na lista.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

def mostrar_lista():
    global lista_numeros
    print("Lista atual:", lista_numeros)

cor_cinza = "\033[90m"
cor_reset = "\033[0m"


while True:
    print(cor_cinza + "### TPC4: Aplicação para manipulação de listas de inteiros ###" )
    print(cor_cinza + "(1) Criar Lista" )
    print(cor_cinza + "(2) Ler Lista" )
    print(cor_cinza + "(3) Soma" )
    print(cor_cinza + "(4) Média" )
    print(cor_cinza + "(5) Maior")
    print(cor_cinza + "(6) Menor" )
    print(cor_cinza + "(7) Esta Ordenada por ordem crescente")
    print(cor_cinza + "(8) Esta Ordenada por ordem decrescente" )
    print(cor_cinza + "(9) Procura um elemento" )
    print(cor_cinza + "(0) Sair" + cor_reset)
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        criar_lista()
    elif opcao == '2':
        ler_lista()
    elif opcao == '3':
        soma()
    elif opcao == '4':
        media()
    elif opcao == '5':
        maior()
    elif opcao == '6':
        menor()
    elif opcao == '7':
        esta_ordenada_crescente()
    elif opcao == '8':
        esta_ordenada_decrescente()
    elif opcao == '9':
        procura_elemento()
    elif opcao == '0':
        mostrar_lista()
        print("Aplicação encerrada.")
        break
    else:
        print("Opção inválida. Tente novamente.")
