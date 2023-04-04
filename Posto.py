combustivel = (input("\nDigite tipo de combustível: "
                     "\nGasolina = G e Etanol = E:  "))
litros = float(input("\nDigite a quantidade de Litros: "))

if combustivel == "G" or combustivel == "g":

    combustivel = 5.80

    total = (combustivel * litros)
    print(combustivel,"*",5.8)
    print("O valor de gasolina total deu: R$", total)

elif combustivel in "Ee":

    combustivel = 4.80
    total = (combustivel * litros)
    print(combustivel,"*",litros, "=", total)
    print("\nO valor total de etanol deu: R$", total)

else:
    print("\nOperação incorreta! \n(Letra diferente ou número incorrerto)")
