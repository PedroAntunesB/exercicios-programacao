def validar_nome(nome):
    return nome.strip() != ""


def validar_idade(idade):
    return 14 <= idade <= 120


def validar_email(email):
    return "@" in email and "." in email


def validar_senha(senha):
    return len(senha) >= 8


while True:
    nome = input("Nome: ")
    
    if not validar_nome(nome):
        print("Nome inválido.")
        continue

    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Idade inválida.")
        continue

    if not validar_idade(idade):
        print("A idade deve estar entre 14 e 120 anos.")
        continue

    email = input("E-mail: ")

    if not validar_email(email):
        print("E-mail inválido.")
        continue

    senha = input("Senha: ")

    if not validar_senha(senha):
        print("A senha deve possuir pelo menos 8 caracteres.")
        continue

    print("\nCadastro realizado com sucesso!")
    print("Nome:", nome)
    print("Idade:", idade)
    print("E-mail:", email)
    break