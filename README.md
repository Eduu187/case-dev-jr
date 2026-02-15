# Case Técnico: API To-Do Serverless para Advogados ⚖️

Esta API foi desenvolvida para permitir que advogados gerenciem suas tarefas diárias (visitas a fóruns, revisões de defesas, etc.) de forma eficiente e escalável.

## 🏗️ Arquitetura da Solução
A solução utiliza uma arquitetura **Serverless** na AWS para garantir baixo custo e alta disponibilidade:

- **Entrada:** API Gateway (REST) como porta de entrada.
- **Processamento:** AWS Lambda (Python 3.10) seguindo princípios de **Clean Architecture**.
- **Persistência:** DynamoDB (NoSQL) para armazenamento stateless e escalável.
- **Infraestrutura:** Provisionada via **Terraform** (IaC).
- **Observabilidade:** Logs estruturados e métricas via CloudWatch e tracing com X-Ray.

## 📁 Estrutura do Projeto
- `src/domain`: Entidades puras e regras de negócio.
- `src/application`: Casos de uso e lógica de orquestração.
- `src/infrastructure`: Implementação de repositórios (DynamoDB) e schemas de validação.
- `src/handlers`: Pontos de entrada das funções Lambda.
- `terraform/`: Arquivos de configuração da infraestrutura.

## 🚀 Como Executar Localmente
```bash
    pip install -r requirements.txt
```

# Como as Lambdas dependem do contexto AWS, a execução local foca na validação dos modelos Pydantic e lógica de domínio.
python -m pytest

### 🛠️ Deploy (Terraform)
1. Vá para a pasta terraform:
cd terraform

2. Inicialize o Terraform:
terraform init

3. Aplique a configuração:
terraform apply

## 📡 Endpoints da API
- `POST /tasks`: Criar nova tarefa.
- `GET /tasks`: Listar todas as tarefas.
- `GET /tasks/{id}`: Buscar tarefa por ID.
- `PUT /tasks/{id}`: Atualizar status ou descrição.
- `DELETE /tasks/{id}`: Remover tarefa.