Nota1 = float(input("Digite a Nota 1:"))
Nota2 = float(input("\nDigite a Nota 2:"))
Nota3 = float(input("\nDigite a Nota 3:"))

Media = ((Nota1+Nota2+Nota3)/3)

print("\nA média foi: ", Media)

if Media >=4 and Media <7:
    print("Recuperação!")

    if Media >= 7:
        print("Aluno Aprovado!")

else:
     print("Aluno Reprovado!")
