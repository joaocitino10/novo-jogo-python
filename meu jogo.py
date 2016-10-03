import random

print "pense em um numero entre 1 e 100, que eu vou acertar"
tempo = raw_input("pressione 'enter' quando tiver pensado no numero")
minimo = 1
maximo = 100
numero = random.randint(minimo, maximo)
print " o seu numero pensado foi esse: " + str(numero) + " ?"
resposta1 = raw_input("digite 's' se eu acertei ou 'n' se eu errei: ")
while resposta1 != 's' :
    resposta2 = raw_input("digite '>' se eu chutei baixo ou '<' se eu chutei alto: ")
    if resposta2 == '>' :
         minimo = numero + 1
    else:
        maximo = numero -1
    numero = random.randint(minimo, maximo)
    print " o seu numero pensado foi esse: " + str(numero) + " ?"
    resposta1 = raw_input("digite 's' se eu acertei: ")
            
print "hahahaha! Eu sou d+!"   
    
