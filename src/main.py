import os

def limpar_tela ():
    print("\033c", end ="")
    
tarefas = []    
    
    
def mostrar_menu():
    while True: 
        limpar_tela()
        print("===== Gerenciamento de Tarefas =====\n")
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
    print("===== Cadastrar Tarefa =====")
    nome = input("Tarefa: ")
    observacao = input("Observação: ")
    while True:
        escolha = input("Status: \n 1 = A Fazer\n 2 = Em Progresso\n 3 = Feito\nStatus da Tarefa? ")
        
        
        if escolha == "1":
            status = "A Fazer"
            break
        elif escolha == "2":
            status = "Em progresso"
            break
        elif escolha == "3":
            status = "feito"
            break
        else:
            print ("Opção invalida")
            input ()
        return  cadastrar()       
            
            

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
    print("===== Editar Tarefa =====\n")

    if not tarefas:
        print("⚠️ Nenhuma tarefa cadastrada.")
        input("Pressione Enter para voltar...")
        return

    nome = input("Digite o nome da tarefa que deseja editar: ")

    
    tarefa = None
    for t in tarefas:
        if t['Nome'].lower() == nome.lower():
            tarefa = t
            break

    if not tarefa:
        print("⚠️ Tarefa não encontrada.")
        input("Pressione Enter para voltar...")
        return

    
    nova_obs = input(f"Observação atual: {tarefa['Observação']}\nNova observação: ")
    if nova_obs.strip():
        tarefa['Observação'] = nova_obs

    
    print("\nEscolha o novo status:")
    print("1 = A Fazer")
    print("2 = Em Progresso")
    print("3 = Feito")

    escolha = input("Status da Tarefa: ")
    if escolha == "1":
        tarefa['Status'] = "A Fazer"
    elif escolha == "2":
        tarefa['Status'] = "Em Progresso"
    elif escolha == "3":
        tarefa['Status'] = "Feito"
    else:
        print("Status inválido, mantendo o anterior.")

    print(f"\n✅ Tarefa '{tarefa['Nome']}' atualizada com sucesso!")
    input("Pressione Enter para continuar...")




mostrar_menu()