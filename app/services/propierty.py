from app.core.core import cur
from app.utils.context.repository import get_register
from app.utils.entities.entitity_propertie import PropiertiesEntity, ResponseModel
from app.utils.operators.operators import operatorUtils

listCons = ["'pre_venta'","'en_venta'","'vendido'"]
consult = "select *\
               from habi_db.status_history as history\
               inner join property as pro on history.property_id =pro.id\
               inner join status as statu on history.status_id = statu.id\
               having history.id in (select max(status_history.id) from status_history group by status_history.property_id)\
               and statu.name in({})".format(",".join(listCons))

def get_propertie():
    register = consult
    result = get_register(register)
    data = list(map(lambda register: PropiertiesEntity(yearCreated=register['year'], city=register['city'],
    state=register["name"], address=register["address"], price=register["price"], description=register['description']), result))      
    return ResponseModel(status=200, data=data, details=[])

def get_filter_propertie(data):
    consultFilter = ' and '
    for result in data.data:
        consultFilter = consultFilter + result.dataFilter[0]+operatorUtils.getValue(result.dataFilter[1],result.dataFilter[2])\
            + (";" if result.other == "" else result.other + " ")
    consultFilter = consult + consultFilter    
    result = get_register(consultFilter)
    data = list(map(lambda register: PropiertiesEntity(yearCreated=register['year'], city=register['city'],
    state=register["name"], address=register["address"], price=register["price"], description=register['description']), result))      
    return ResponseModel(status=200, data=data, details=[]) 
