def verificar_email(email):
    if "@" in email and "." in email:
        arroba = email.index("@")
        ponto = email.rfind(".")
        if arroba < ponto and arroba > 0 and ponto < len(email) - 1:
            return True
    return False

email = input("Digite seu e-mail: ")


if verificar_email(email):
    print("E-mail válido")
else:
    print("E-mail inválido")
