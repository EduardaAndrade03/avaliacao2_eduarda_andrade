# Soma de pares e ímpares

impares=0
pares=0
numeros=[]
for x in range(1,11):
    inteiro=int(input(f"Digite o numero {x}: "))
    numeros.append(inteiro)
print(numeros)
for x in numeros:
    if x%2==0:
        pares+=x
    else:
        impares+=x
print(f"soma de todos os números pares: {pares}")
print(f"soma de todos os números ímpares: {impares}")