# Lista de convidados

print("LISTA DE CONVIDADOS")
convidados=[]
for x in range(1,6):
    convidado=str(input(f"digite o convidado nº{x}: "))
    convidados.append(convidado)
verificar=str(input("digite qual convidado você deseja verificar se está na lista: "))
if verificar in convidados:
    print("Convidado confirmado!")
else:
    print("Convidado não encontrado!")