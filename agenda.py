agenda = {}

def adicionar_contato():
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()
    agenda[nome] = {"telefone": telefone, "email": email}
    print(f"\nContato '{nome}' adicionado com sucesso!")

