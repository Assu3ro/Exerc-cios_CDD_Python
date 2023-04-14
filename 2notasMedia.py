resposta = "s"
#resposta=input("Você deseja fazer um cálculo (s ou n?)")
while resposta == "s":

    nota1 = float(input("Digite a primeira nota: "))
    while nota1<0 or nota1>10:
        nota1 = float(input("Nota fora do intervalo, coloque um número entre 0 e 10: "))

    nota2 = float(input("Digite a segunda nota: "))
    while nota2 <0 or nota2 >10:
        nota2 = float(input("Nota fora do intervalo, coloque um número entre 0 e 10: "))

    media= (nota1+nota2)/2
    print("A media é:", media)

    resposta = input("Você deseja fazer um cálculo (s/n?)")

