from pydantic import BaseModel, validator
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class alunoCreate(BaseModel):
    nome: str
    idade:int
    ano: str

    @validator('idade')
    def validar_idade(cls,value):
        if value < 0:
            return ValueError("A idade inserida é inválida")
        return value
    
class alunoRead(BaseModel):
    id: int
    nome: str
    idade: int
    ano: str

class alunoDB(Base):
    __tablename__ = 'alunos'

    id = Column(Integer, primary_key = True, index = True)
    nome = Column(String, index = True)
    idade = Column(Integer, index = True)
    ano = Column(String, index = True)

