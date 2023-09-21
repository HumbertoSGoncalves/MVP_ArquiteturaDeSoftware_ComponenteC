from pydantic import BaseModel


# como uma nota é adicionada a um vinho
class NotaSchema(BaseModel):
    vinho_id: int = 1
    texto: str = "Notas a serem adicionadas."
