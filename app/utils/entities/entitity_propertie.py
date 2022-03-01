from multiprocessing.dummy import Array
from typing import List
from pydantic import BaseModel

#Las entidades se pueden crear en una sola clase por clase, es decir 
# Dejar en una sola clase, todas las entidades posibles. Sea de respuesta o de ingreso
class PropiertiesEntity(BaseModel):
    yearCreated: str = '2020'
    city: str = 'Bogota'
    state: str = 'Vendido'
    address: str = "Calle 98 a # 60-72"
    price: int = 23123
    description: str = "peipit"

class PropiertierFilter(BaseModel):
    dataFilter = ["column","operation","value"]
    other: str = ""

class ResponseModel(BaseModel):
    status: int
    details: List
    data: List[PropiertiesEntity] 

class FilterModel(BaseModel):
    data: List[PropiertierFilter] 