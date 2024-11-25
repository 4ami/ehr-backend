from sqlalchemy.orm import Session
from app.models import OrderModel
from app.views import ReceptionistUpdateResponse, ReceptionistUpdateOrder

async def updateTypeDept(session:Session, request:ReceptionistUpdateOrder) -> ReceptionistUpdateResponse:
    order = session.query(OrderModel).filter(OrderModel._id == request.id).first()

    if order is None: return None
    
    update = {}
    update['department'] = order.department
    update['type'] = order.type

    order.type = request.type.name if request.type is not None else order.type
    order.department = request.department if request.department is not None else order.department
    session.commit()
    return ReceptionistUpdateResponse(
        message='Update Success',
        status_code=200,
        id=order._id,
        old_type=update['type'].name,
        new_type=order.type.name,
        old_dept=update['department'],
        new_dept=order.department
    )