quant_neg=0
for i in range(10):
    num=int(input("Escreva um número: "))
    if num < 0:
        quant_neg+=1
print("A quantidade de número negativo foi: ",quant_neg)