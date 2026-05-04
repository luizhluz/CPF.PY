def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica tamanho e sequência inválida
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Cálculo do 1º dígito
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = 11 - (soma % 11)
    if dig1 >= 10:
        dig1 = 0

    # Cálculo do 2º dígito
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = 11 - (soma % 11)
    if dig2 >= 10:
        dig2 = 0

    # Verifica os dígitos
    return dig1 == int(cpf[9]) and dig2 == int(cpf[10])


# Programa principal
cpf = input("Digite o CPF: ")

if validar_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")