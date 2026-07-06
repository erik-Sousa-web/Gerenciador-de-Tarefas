tarefas = []


def adicionar_tarefa(descricao):
    tarefa = {
        "id": len(tarefas) + 1,
        "descricao": descricao,
        "concluida": False
    }

    tarefas.append(tarefa)

    return tarefa


def listar_tarefas():
    return tarefas


def editar_tarefa(id, descricao):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["descricao"] = descricao
            return tarefa
    return None


def excluir_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return True

    return False