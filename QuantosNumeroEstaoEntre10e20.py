intervalo=0
foraIntervalo=0
for i in range(4):
    num=int(input("Escreva um número: "))
    if num<=20 and num>=10:
        intervalo+=1
    else :
        foraIntervalo+=1
print("A quantidade de número entre 10 e 20 foi: ",intervalo)
print("A quantidade de número fora de 10 e 20 foi: ",intervalo)
