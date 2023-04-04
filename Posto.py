combustivel = (input("\nDigite tipo de combustível: "
                     "\nGasolina = G e Etanol = E:  "))
litros = float(input("\nDigite a quantidade de Litros: "))

if combustivel == "G" or combustivel == "g":

    combustivel = 5.80

    total = (combustivel * litros)
    print("O valor de gasolina total deu: R$", total)

elif combustivel == "E" or combustivel == "e":

    combustivel = 4.80
    total = (combustivel * litros)
    print("O valor total de etanol deu: R$", total)

else:
    print("Operação incorreta! \n(Letra diferente ou número incorrerto)")
