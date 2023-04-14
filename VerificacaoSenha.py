senha1 = input("Cadastre uma senha: ")
cont=1
senha2 = input("Digite sua senha: ")
if (senha2 != senha1):
    while cont<=3:
        num = input("Tente novamente: ")
        cont=cont+1
    print("Acesso bloqueado!")
else:
    print("\nBem vindos!")
