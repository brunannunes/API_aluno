from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import *
from models import *
from typing import List

app = FastAPI()

@app.post("/aluno", response_model=alunoRead)

def creat_aluno(aluno: alunoCreate, db: Session = Depends(get_db)):
    db_aluno = alunoDB(**aluno.model_dump())

    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)

    return db_aluno

@app.get("/aluno", response_model=List[alunoRead])
def get_all_alunos(db: Session = Depends(get_db)):
    alunos = db.query(alunoDB).all()
    return alunos

@app.get("/alunos/{aluno_id}", response_model=alunoRead)
def getAlunoById (aluno_id: int, db: Session = Depends(get_db)):
    alunos = db.query(alunoDB).filter(alunoDB.id == aluno_id).first()

    if alunos is None:
        raise HTTPException(status_code=404, detail="aluno nao encontrado")
    return alunos

@app.delete("/aluno/{aluno_id}")
def delete_aluno (aluno_id: int, db: Session = Depends(get_db)):
    alunos = db.query(alunoDB).filter(alunoDB.id == aluno_id).first()

    if alunos:
        db.delete(alunos)
        db.commit()

        return{'message': f'aluno com id "{aluno_id}" foi deletado', 'aluno deletado': alunos}
    else:
        raise HTTPException(status_code=404, detail="esse aluno nao foi encontrado")