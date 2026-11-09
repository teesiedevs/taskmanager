# 📋 Task Management CLI

Um gerenciador de tarefas desenvolvido em **Python**, que permite organizar atividades diretamente pelo terminal de forma simples, prática e eficiente.

O projeto oferece funcionalidades para cadastrar, listar, atualizar e remover tarefas, além de permitir a definição de prioridades e o acompanhamento do status de cada atividade.

## 🚀 Funcionalidades

- **Adicionar tarefas:** Cadastra novas tarefas com título, status e prioridade.
- **Atualizar status:** Permite modificar o status de uma tarefa entre `pending` e `completed`.
- **Listar tarefas:** Exibe todas as tarefas cadastradas, incluindo seus respectivos status e níveis de prioridade.
- **Remover tarefas:** Permite excluir tarefas específicas utilizando seu título como referência.
- **Gerenciamento por prioridade:** Classifica as tarefas em três níveis: baixa, média e alta.

## 🛠️ Tecnologias utilizadas

- **Python 3.10+**
- Estruturas de dados nativas do Python (listas e dicionários).
- Interface de interação via terminal (CLI).

## 📦 Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.10 ou superior.
- Um terminal ou editor de código de sua preferência.

Para verificar a versão do Python:

```bash
python --version
```

## ⚙️ Como executar

**1. Clone o repositório**

```bash
git clone https://github.com/seu-usuario/task-management-cli.git
```

**2. Acesse a pasta do projeto**

```bash
cd task-management-cli
```

**3. Execute o programa**

```bash
python main.py
```

**4. Utilize o menu e siga as instruções apresentadas no terminal para gerenciar suas tarefas.**

## 📊 Níveis de prioridade

O sistema utiliza opções numéricas para definir a prioridade de cada tarefa:

| Opção | Prioridade |
|:---:|:---|
| `1` | Baixa |
| `2` | Média |
| `3` | Alta |

## 📌 Estrutura dos dados

As tarefas são armazenadas em memória utilizando uma lista de dicionários.

Cada tarefa possui os seguintes atributos:

```python
{
    "title": "Estudar Python",
    "situation": "pending",
    "priority": "alta"
}
```

| Atributo | Descrição |
|---|---|
| `title` | Nome ou descrição da tarefa. |
| `situation` | Status atual da tarefa (`pending` ou `completed`). |
| `priority` | Nível de prioridade (`baixa`, `média` ou `alta`). |

## 📁 Estrutura do projeto

```text
task-management-cli/
│
├── main.py
└── README.md
```

## ⚠️ Pontos de atenção

Alguns ajustes podem ser necessários para melhorar a estabilidade e a experiência de utilização do sistema:

- **Remoção de tarefas:** Verificar a referência ao atributo `self.new_tasks` no método `delete_tasks`, pois o atributo utilizado pela classe é `self.tasks`.
- **Validação da busca:** A mensagem de tarefa não encontrada deve ser exibida somente após verificar todos os elementos da lista.
- **Validação de prioridade:** Implementar tratamento para entradas diferentes de `1`, `2` ou `3`, evitando erros durante a execução.

## 🔮 Melhorias futuras

Algumas funcionalidades podem ser implementadas para expandir o projeto:

- [ ] Criar um menu principal interativo.
- [ ] Implementar validação de entradas do usuário.
- [ ] Permitir a edição do título de uma tarefa.
- [ ] Adicionar filtros por prioridade e status.
- [ ] Implementar persistência de dados utilizando arquivos JSON.
- [ ] Adicionar testes automatizados.

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais da programação em Python, como:

- Programação Orientada a Objetos (POO).
- Manipulação de listas e dicionários.
- Estruturas condicionais e de repetição.
- Criação e utilização de métodos.
- Tratamento de entradas do usuário.
- Organização e estruturação de código.

## 👩‍💻 Autoria

Desenvolvido como projeto de prática e aprimoramento de habilidades em Python.

---

**Task Management CLI** — Organização e produtividade diretamente pelo terminal. 🐍

