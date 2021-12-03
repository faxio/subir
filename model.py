from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime, time, timedelta


class Usuarios(BaseModel):
    nombre: str
    correo: str
    password: str
    rango: str


class NoticiasAnalisadas(BaseModel):
    author: str
    content: str
    title: str
    analisis: Optional[str]
    analista: Optional[str]
    description: str
    url: str
    fecha: str
    numVistas: Optional[int]
    category: Optional[list]

    class Config:
        orm_mode = True


class Categorias(BaseModel):
    categoria: str


'''
m = NoticiasAnalisadas(
    author="fabio",
    content="deded",
    title="mor",
    analisis="ffsfff",
    analista="faxio",
    description="mir",
    url="sd2",
    fecha="2021-11-30",
    numVistas=5,
    #category=["depoter","comida"]
)
print(m.dict())
'''
