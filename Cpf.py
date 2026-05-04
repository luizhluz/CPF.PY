cpf = input("Digite o CPF: ")


cpf = cpf.replace(".", "")
cpf = cpf.replace("-", "")

if len(cpf) != 11:
    print("CPF inválido!")
else:
    if cpf == cpf[0] * 11:
        print("CPF inválido!")
    else:
     
        soma = 0
        for i in range(9):
            soma = soma + int(cpf[i]) * (10 - i)

        resto = soma % 11
        dig1 = 11 - resto
        if dig1 >= 10:
            dig1 = 0

       
        soma = 0
        for i in range(10):
            soma = soma + int(cpf[i]) * (11 - i)

        resto = soma % 11
        dig2 = 11 - resto
        if dig2 >= 10:
            dig2 = 0

      
        if dig1 == int(cpf[9]) and dig2 == int(cpf[10]):
            print("CPF válido!")
        else:
            print("CPF inválido!")
