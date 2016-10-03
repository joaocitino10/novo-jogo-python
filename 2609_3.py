import random

continuar = "sim"
while continuar =="sim":
    tentativas = 0
    numero = random.randint(1, 100)
    resposta = 0
    print "tente acertar o numeroque o computador escolheu !!"
    while numero != resposta:
        tentativas = tentativas + 1
        resposta = raw_input("digite um numero aleatorio entre 1 e 100: ")
        resposta = int (resposta) 
        if resposta > numero:
            print "o numero certo e menor que " + str(resposta)
        if resposta < numero:
            print "o numero certo e maior que" + str(resposta)
    print " oba ! woohoooo !! voce acertou ! (y)"
    print " voce acertou depois de "  + str ( tentativas) + " tentativas. "
    continuar = raw_input ("digite 'sim' para jogar de novo: ")  
    
 

           

           

