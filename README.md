 Validador de CPF em Python

Este projeto contém um script simples em Python para validar números de CPF (Cadastro de Pessoas Físicas) de acordo com as regras oficiais da Receita Federal.

 Funcionalidades

Remove automaticamente caracteres não numéricos
Verifica se o CPF possui 11 dígitos
Identifica CPFs inválidos com todos os números iguais (ex: 11111111111)
Calcula e valida os dois dígitos verificadores
Retorna se o CPF é válido ou inválido

 Como funciona

O algoritmo segue os seguintes passos:

Remove qualquer caractere que não seja número
Verifica se o CPF tem exatamente 11 dígitos
Calcula o primeiro dígito verificador com base nos 9 primeiros números
Calcula o segundo dígito verificador com base nos 10 primeiros números
Compara os dígitos calculados com os informados

 Como usar

Clone este repositório ou copie o código
Execute o script com Python:
