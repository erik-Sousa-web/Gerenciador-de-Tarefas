import os

def limpar_tela ():
    print("\033c", end ="")
    
tarefas = []    
    
    
    
    
def listar_tarefas():
    print("====== Tarefas Cadastradas ======\n")

    if not tarefas:
        print("⚠️  Nenhuma tarefa cadastrada.\n")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa['Nome']} - {tarefa['Status']}")
            print(f"   Observação: {tarefa['Observação']}\n")
    print("=" * 33 )        
    
    
    
def escolher_status():
    while True:
        print("1 = A Fazer")
        print("2 = Em Progresso")
        print("3 = Feito")

        escolha = input("Status da Tarefa: ")

        if escolha == "1":
            return "A Fazer"
        elif escolha == "2":
            return "Em Progresso"
        elif escolha == "3":
            return "Feito"
        else:
            print("Opção inválida, tente novamente.")
            input("Pressione Enter...")    
    
    
    
    
def mostrar_menu():
    while True: 
        limpar_tela() 
        listar_tarefas()
        print("\n===== Gerenciamento de Tarefas =====\n") 
        print("1 = Cadastrar")
        print("2 = Editar")
        print("3 = Excluir")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            editar()
        elif opcao == "3":
            excluir()
        else:
            print ("Opção invalida")
            input ()
        return  mostrar_menu()
    
    

def cadastrar():
    limpar_tela()
    listar_tarefas()
    print("===== Cadastrar Tarefa =====") 
    nome = input("Tarefa: ")
    observacao = input("Observação: ")
    status = escolher_status()
        
    tarefa = {
        'Nome':nome,
        'Observação':observacao,
        'Status':status
    }

    tarefas.append(tarefa)
    print(f"✅ Tarefa '{nome}' adicionado com sucesso!")    
    input("Pressione Enter para continuar... ")
    
    



def editar():
    limpar_tela()
    listar_tarefas()
    print("===== Editar Tarefa =====\n")
    nome = input("Digite o nome da tarefa que deseja editar: ")

    tarefa = None
    for t in tarefas:
        if t["Nome"].lower() == nome.lower():
            tarefa = t
            break

    if not tarefa:
        print("⚠️ Tarefa não encontrada.")
        input("Pressione Enter para voltar...")
        return

    nova_obs = input(f"Observação atual: {tarefa['Observação']}\nNova observação: ")
    if nova_obs.strip():
        tarefa['Observação'] = nova_obs

    tarefa["Status"] = escolher_status()

    print(f"\n✅ Tarefa '{tarefa['Nome']}' atualizada com sucesso!")
    input("Pressione Enter para continuar...")
    
    
def excluir():
    limpar_tela()
    listar_tarefas()
    
    print("===== Excluir Tarefa =====\n")
    nome = input("Digite o nome da tarefa a ser Excluida:  ")
    encontrado = False
    for tarefa in tarefas:
        if tarefa["Nome"].lower() == nome.lower():
                tarefas.remove(tarefa)
                print(f"✅ Tarefa '{nome}' excluida com sucesso.")
                encontrado = True
                break
    if not encontrado:
            print(" ❌ Tarefa não Encontrada.")
    input("\nPressione Enter para continuar...")





mostrar_menu()  

