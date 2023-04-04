time1 = (input("\nDigite o time 1:"))
gol1 = int(input("\nNúmero de gols marcados:"))
time2 = (input("\nDigite o time 2:"))
gol2 = int(input("\nNúmero de gols marcados:"))


if gol1 != gol2:

    if gol1>gol2:
        print("O time ", time1, "ganhou")

    else:
        print("O time ", time2, "ganhou")

else:
    print("Mesma quantidade de gol em ambos os times")

