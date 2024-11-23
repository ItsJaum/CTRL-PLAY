# Email = gomesbitellaj@gmail.com
# print(Email)


# print("")
# print(len(Email))
# print(Email.find("@gmail.com"))
# print(Email.count("."))

email = input("Escreva seu email: ")

print(email)
print("Quantidade de caracteres no email:", len(email))

if email.find("@") != -1:
    print("confirmado")
else:
    print("recusado")