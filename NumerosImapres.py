print("\nBem vindos! Você saberá quantos número pares tem dentro do numero que você colocará.")
num = int(input("Digite um numero: "))
cont = 0
for i in range(1,num+1):
    if i%2!=0:
        cont=cont+1
print(cont)