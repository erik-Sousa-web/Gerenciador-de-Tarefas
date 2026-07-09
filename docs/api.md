## Documentação da API

## Listar tarefas
Método: GET
Rota: /tarefas
O que faz: Retorna a lista de todas as tarefas cadastradas
Retorno: Lista de tarefas em formato JSON, cada uma com id, descrição e status de conclusão

## Criar tarefa
Método: POST
Rota: /tarefas
O que envia: enviar uma nova tarefa para a memoria json.
Retorno: retorna a tarefa criada (id, descrição e status) em formato JSON
## Editar tarefa
Método: PUT
Rota: /tarefas/<id>
O que envia: envia atualização de uma tarefa.
Retorno: retorna a tarefa com as novas atualizações.

## Excluir tarefa
Método: DELETE
Rota: /tarefas/<id>
O que envia: exclui uma tarefa do app
Retorno: mensagem de confirmação que a tarefa foi removida com sucesso.