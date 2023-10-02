#Adivinhar o número
import random
n = random.randrange(1,101)
tentativas = 0
sup = 100
inf = 0
x = 0

print ("Escolha o jogo :)")

print("1-Adivinhar o número que o computador está a pensar;") 
print("2-O computador adivinhar o número que está a pensar")
jogo = int(input("Que jogo quer jogar?"))

if jogo == 1:
    print ("Tente adivinhar o número que o computador está a pensar")
    tentativas = 100
    for rodada in range(1, tentativas + 1):
        print(f"Tentativa número {rodada}")
        numero_str = input("Digite um número: ")
        numero = int(numero_str)
        if numero < 1 or numero > 100:
            print ("Número inválido, o número tem que ser entre 1 e 100")
            continue
        acertou = numero == n
        maior = numero > n
        menor = numero < n
        if acertou:
            print (f"Parabéns, acertou o número secreto em {rodada} tentativas :)")
            break
        else:
            if maior:
                print("Escreva um número menor")
            elif menor:
                print("Escreva um numero maior")
    print ("Fim do Jogo")
elif jogo == 2:
    print (" Vou adivinhar o número em que está a pensar")
    tentativas = 100
    for rodada in range(1, tentativas + 1):
        print(f"Tentativa número {rodada}")
        x = int((sup + inf) / 2)
        resposta_str =input (f"O seu número é {x}? (Digite sim ou não)")
        if resposta_str == "sim":
            print(f"Acertei o número em {rodada} tentativas :)")
            break
        else:
            resposta2_str = input ("É maior ou menor?")
            if resposta2_str == "maior":
                inf = x
            else:
                sup = x
    print("Fim do Jogo")