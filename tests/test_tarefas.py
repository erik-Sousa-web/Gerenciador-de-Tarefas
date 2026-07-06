from src.tasks import (
    adicionar_tarefa,
    listar_tarefas,
    editar_tarefa,
    excluir_tarefa,
    tarefas
)


def setup_function():
    tarefas.clear()


def test_adicionar_tarefa():
    adicionar_tarefa("Estudar Python")

    assert len(tarefas) == 1
    assert tarefas[0]["descricao"] == "Estudar Python"


def test_listar_tarefas():
    adicionar_tarefa("Teste")

    assert len(listar_tarefas()) == 1


def test_editar_tarefa():
    adicionar_tarefa("Velha")

    editar_tarefa(1, "Nova")

    assert tarefas[0]["descricao"] == "Nova"


def test_excluir_tarefa():
    adicionar_tarefa("Excluir")

    excluir_tarefa(1)

    assert len(tarefas) == 0