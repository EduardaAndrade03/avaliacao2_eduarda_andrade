# Média de notas

def calcular_media(lista):
    soma=0
    med=0
    for  nota in lista:
        soma+=nota
    med=soma/4
    if med<0 or med>10:
        return(f"Tem alguma coisa errada. Média: {med}")
    elif med>=7:
        return(f"Aprovado. Média: {med}")
    elif med<7:
        return(f"Reprovado. Média: {med}")
notas=[]
for x in range(1,5):
    nota=int(input(f"Digite a {x}º nota: "))
    notas.append(nota)
print(calcular_media(notas))
