from app.utils.context.repository import get_register

listCons = ["'pre_venta'","'en_venta'","'vendido'"]
consult = "select *\
               from habi_db.status_history as history\
               inner join property as pro on history.property_id =pro.id\
               inner join status as statu on history.status_id = statu.id\
               having history.id in (select max(status_history.id) from status_history group by status_history.property_id)\
               and statu.name in({})".format(",".join(listCons))

def test_get_register():
    response = get_register(consult)
    assert len(response)==55