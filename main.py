nome = input("Nome completo: ")
entrada = True

while entrada == True:
    try:
        ano = int(input("Ano do nascimento: "))
        if 1922 <= ano <= 2021:
            entrada = False
        else:
            print("Ano invalido. Digite um ano entre 1922 e 2021.")
    except ValueError:
        print("Digite apenas numeros validos.")

diferenca = 2022 - ano
print(f" {nome}! Você tem {diferenca} anos.")
