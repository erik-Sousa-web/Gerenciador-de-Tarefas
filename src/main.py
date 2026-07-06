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




mostrar_menu()