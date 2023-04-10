x = int(input("Digite um número da série:"))
if x < 0: 
    print ("Número inválido!")
elif x == 1:
    print (1)
elif x == 2:
    print (1)
else:
    v = 1
    va = 1
    x = x - 2
    while x > 0:
        aux = v
        v = v + va
        va = aux
        x = x - 1
    print (v)