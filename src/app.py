import os



from src.tasks import adicionar_tarefa, listar_tarefas, editar_tarefa, excluir_tarefa
from src.tasks import adicionar_tarefa, listar_tarefas, editar_tarefa, excluir_tarefa
from flask import Flask, render_template, request, jsonify
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "..", "templates"),
    static_folder=os.path.join(BASE_DIR, "..", "static")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tarefas", methods=["GET"])
def listar():
    return jsonify(listar_tarefas())

@app.route("/tarefas", methods=["POST"])
def post():
    descricao = request.json["descricao"] 
    tarefa =  adicionar_tarefa(descricao)           
    return jsonify(tarefa)

@app.route("/tarefas/ <int:id>", methods = ["PUT"])
def editar(id):
    descricao = request.json["descricao"]
    tarefa = editar_tarefa(id, descricao) 
    return jsonify(tarefa)   
    

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def excluir(id):
    excluir_tarefa(id)
    return jsonify({"sucesso": True})


if __name__ == "__main__":
    app.run(debug=True)