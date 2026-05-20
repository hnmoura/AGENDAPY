agenda = {}

def adicionar_contato():
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("E-mail: ").strip()
    agenda[nome] = {"telefone": telefone, "email": email}
    print(f"\nContato '{nome}' adicionado com sucesso!")

def listar_contatos():
    if not agenda:
        print("\nSua agenda está vazia.")
        return
    print("\n--- LISTA DE CONTATOS ---")
    for nome, dados in sorted(agenda.items()):
        print(f"Nome: {nome} | Telefone: {dados['telefone']} | E-mail: {dados['email']}")

def buscar_contato():
    nome = input("Digite o nome do contato que deseja buscar: ").strip()
    if nome in agenda:
        dados = agenda[nome]
        print(f"\nNome: {nome} | Telefone: {dados['telefone']} | E-mail: {dados['email']}")
    else:
        print(f"\nContato '{nome}' não encontrado.")

def excluir_contato():
    nome = input("Digite o nome do contato que deseja excluir: ").strip()
    if nome in agenda:
        del agenda[nome]
        print(f"\nContato '{nome}' removido com sucesso.")
    else:
        print(f"\nContato '{nome}' não encontrado.")

def menu():
    while True:
        print("\n=== AGENDA DE CONTATOS ===")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Buscar Contato")
        print("4. Excluir Contato")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            buscar_contato()
        elif opcao == '4':
            excluir_contato()
        elif opcao == '5':
            print("\nSaindo da agenda...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
