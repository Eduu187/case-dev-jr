# Case Prático – API Serverless (AWS Lambda)

## 🎯 Objetivo do teste
* Lógica de programação
* Estruturação de funções Lambda
* Conceitos de API serverless
* Boas práticas em ambiente stateless
* Noções de AWS
* Organização, clareza e documentação

---

## 📝 Parte 1 – Desenvolvimento de lambda

### Contexto do problema
Você deve desenvolver uma API serverless de gerenciamento de tarefas (To-Do) que será utilizada por um front-end para que os advogados possam gerenciar suas tarefas do dia a dia como visitas ao Fórum, revisão de defesas, etc.

A API deverá rodar em **AWS Lambda**, exposta via **API Gateway**, e armazenar os dados em um banco gerenciado.

### Modelo de dados: Tarefa
* **id**: (UUID)
* **titulo**: (string)
* **descricao**: (string)
* **status**: (Pendente | Em Andamento | Concluída)
* **criado_por**: (string)
* **data_criacao**: (formato dd/mm/aaaa)
* **data_conclusao**: (formato dd/mm/aaaa)

### Requisitos funcionais
A API deve permitir:
1. Criar uma tarefa
2. Listar todas as tarefas
3. Buscar tarefa por ID
4. Atualizar uma tarefa
5. Excluir uma tarefa

### Stack obrigatória
* **Linguagem:** Python 3.10+ ou C# (Framework .NET 6 ou superior)
* **Execução:** AWS Lambda
* **API:** API Gateway (REST ou HTTP API)
* **Banco de dados:** Livre escolha
* **Infraestrutura:** Stackspot, Terraform, SAM ou Serverless Framework (Livre escolha)

---

## 🏗️ Parte 2 – Desenho de solução
Elabore o desenho da solução, explicando os componentes utilizados e o fluxo da aplicação.

---

## 🎤 Parte 3 – Apresentação da solução
Você terá **30 minutos** para apresentar a solução, sendo necessário:
* Apresentar o desenho de solução, explicando os componentes e sua utilização.
* Apresentar a estrutura de banco de dados criada.
* Apresentar o código elaborado.

> **Nota:** O formato da apresentação é livre.

---

## 📦 Entrega
Repositório Git ou arquivo ZIP contendo:
* Código-fonte completo.
* Arquivo de infraestrutura (SAM / Terraform / Serverless).
* **README** com instruções de deploy e execução local.

*Obs: Não é necessário publicar na AWS.*