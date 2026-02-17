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
- `GET /tasks?status=Pendente`: Filtrar tarefas por status.
- `GET /tasks/{id}`: Buscar tarefa por ID.
- `PUT /tasks/{id}`: Atualizar status ou descrição.
- `DELETE /tasks/{id}`: Remover tarefa.

## 📋 Estrutura da Task no DynamoDB

### Modelo de Dados
A entidade `Task` é composta pelos seguintes atributos:

| Atributo | Tipo | Descrição | Exemplo |
|----------|------|-----------|---------|
| `id` | String | Identificador único (UUID) | `550e8400-e29b-41d4-a716-446655440000` |
| `titulo` | String | Título da tarefa (3-100 caracteres) | `Revisar processo nº 123/2025` |
| `descricao` | String | Descrição detalhada (máx 500 caracteres) | `Análise de jurisprudência para defesa` |
| `status` | String | Status atual da tarefa | `Pendente`, `Em Andamento`, `Concluída` |
| `criado_por` | String | Nome do advogado criador | `João Silva` |
| `data_criacao` | String | Data de criação (formato dd/mm/aaaa) | `17/02/2026` |
| `data_conclusao` | String (Opcional) | Data de conclusão (formato dd/mm/aaaa) | `20/02/2026` ou `null` |

### Exemplo de Documento no DynamoDB
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "titulo": "Revisar processo nº 123/2025",
  "descricao": "Análise de jurisprudência para defesa em primeira instância",
  "status": "Em Andamento",
  "criado_por": "João Silva",
  "data_criacao": "17/02/2026",
  "data_conclusao": null
}
```

### Regras de Validação
- **Status permitidos:** `Pendente`, `Em Andamento`, `Concluída`
- **Transição de status:** Quando status muda para `Concluída`, `data_conclusao` é preenchida automaticamente
- **Campos obrigatórios:** `titulo`, `descricao`, `status`, `criado_por`
- **Campo `id`:** Gerado automaticamente na criação (UUID v4)