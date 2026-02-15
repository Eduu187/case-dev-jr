from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    id: str
    titulo: str
    descricao: str
    status: str  # Pendente | Em Andamento | Concluída
    criado_por: str
    data_criacao: str  # dd/mm/aaaa
    data_conclusao: Optional[str] = None  # dd/mm/aaaa