print("\nBem vindos!")
numAlunos = int(input("Digite o numero de alunos: "))
cont=1
soma=0
if (numAlunos!=0):
    while cont<=numAlunos:
        num = float(input("Escreva uma nota: "))
        #soma=soma+num
        soma+=num
        cont=cont+1
    print("A média das notas é:",soma/numAlunos)

else:
    print("Número inválido!")