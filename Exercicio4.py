x = int(input("Digite o número a ser testado:"))
if (x == 0):
    print ("Não se sabe")
if x == 2:
    print ("Primo")
else: 
    divisor = 2
    while divisor < x:
        if x%divisor == 0:
            print ("Não é primo")
            break 
        divisor = divisor + 1
    if divisor == x:
        print ("Primo")