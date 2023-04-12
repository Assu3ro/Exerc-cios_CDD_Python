cont=1
soma=0

while cont<=3:
    num = int(input("Escreva uma nota: "))
    #soma=soma+num
    soma+=num
    cont=cont+1
print(soma/3)
