let tarefas = [];

let indiceEdicao = null;

const nome = document.getElementById("nome");

const observacao = document.getElementById("observacao");

const status = document.getElementById("status");

const lista = document.getElementById("lista");

const btnSalvar = document.getElementById("btnSalvar");

const btnCancelar = document.getElementById("btnCancelar");



btnSalvar.onclick = function () {

    if (nome.value.trim() == "") {

        alert("Informe o nome.");

        return;

    }

    const tarefa = {

        nome: nome.value,

        observacao: observacao.value,

        status: status.value

    };

    if (indiceEdicao === null) {

        tarefas.push(tarefa);

    }

    else {

        tarefas[indiceEdicao] = tarefa;

        indiceEdicao = null;

        btnSalvar.innerHTML = "➕ Adicionar";

        btnCancelar.style.display = "none";

    }

    limparFormulario();

    mostrarTarefas();

}



btnCancelar.onclick = function () {

    indiceEdicao = null;

    limparFormulario();

    btnSalvar.innerHTML = "➕ Adicionar";

    btnCancelar.style.display = "none";

}



function limparFormulario() {

    nome.value = "";

    observacao.value = "";

    status.value = "A Fazer";

}



function mostrarTarefas() {

    lista.innerHTML = "";

    tarefas.forEach(function (tarefa, index) {

        let cor = "";

        if (tarefa.status === "A Fazer") {

            cor = "vermelho";

        }

        if (tarefa.status === "Em Progresso") {

            cor = "amarelo";

        }

        if (tarefa.status === "Feito") {

            cor = "verde";

        }

        lista.innerHTML += `

        <div class="card ${cor}">

            <h3>${tarefa.nome}</h3>

            <p>${tarefa.observacao}</p>

            <div class="status">${tarefa.status}</div>

            <div class="acoes">

                <button class="editar" onclick="editar(${index})">

                    ✏ Editar

                </button>

                <button class="excluir" onclick="excluir(${index})">

                    🗑 Excluir

                </button>

            </div>

        </div>

        `;

    });

}



function editar(index) {

    indiceEdicao = index;

    nome.value = tarefas[index].nome;

    observacao.value = tarefas[index].observacao;

    status.value = tarefas[index].status;

    btnSalvar.innerHTML = "💾 Salvar";

    btnCancelar.style.display = "block";

}



function excluir(index) {

    tarefas.splice(index, 1);

    mostrarTarefas();

}