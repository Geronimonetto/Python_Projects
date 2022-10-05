login = 'usuario@hotmail.com'
senha = 123452

while True: 
    login_digitado = input("LOGIN: ")

    if login_digitado == login:
        print("Digite sua senha de acesso!")
        senha_digitada = int(input("SENHA: "))
        if senha_digitada == senha:
            print(f"Bem-vindo {login}!! ")
        else:
            print("Login e Senha NÃO ENCONTRADOS.")
    else:
        print("Login NÃO ENCONTRADO.")