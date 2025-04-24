def verificar_email(email):
    C_MAI = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    C_MIN = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    D = ['0','1','2','3','4','5','6','7','8','9']
    S = ['.','_','-']
    
    if '@' not in email:
        return False
    
    local, dominio = email.split("@")

    if not local or not dominio:
        return False

    for char in local:
        if char not in C_MAI and char not in C_MIN and char not in D and char not in S:
            return False

    if '.' not in dominio:
        return False

    tlds = dominio.split(".")

    for tld in tlds:
        if not tld:
            return False
        
        for char in tld:
            if tld == tlds[0]:
                if char not in C_MIN and char not in D and char != '-':
                    return False
            else:
                if char not in C_MIN:
                    return False

    return True


email = input("Digite seu e-mail: ")

if verificar_email(email):
    print("E-mail válido")
else:
    print("E-mail inválido")