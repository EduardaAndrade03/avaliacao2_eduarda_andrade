# Média de notas

def calcular_media(lista):
    soma=0
    med=0
    for  nota in lista:
        soma+=nota
    med=soma/4
    return med
notas=[]
for x in range(1,5):
    nota=int(input(f"Digite a {x}º nota: "))
    notas.append(nota)

media= calcular_media(notas)

if media>=7:
    print(f"Aprovado. Média: {media}")
elif media<7:
    print(f"Reprovado. Média: {media}")
