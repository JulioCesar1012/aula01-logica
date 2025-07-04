usuarios = []

for i in range(2):
    nome = input("Nome: ")
    email = input("Email: ")
    
    usuario = {
        "nome": nome,
        "email": email
    }

    usuarios.append(usuario)

print("\nUsuários cadastrados:")
for user in usuarios:
    print(f"Nome: {user['nome']} | Email: {user['email']}")
