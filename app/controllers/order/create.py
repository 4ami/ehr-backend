from sqlalchemy.orm import Session
from app.models import OrderModel
from app.views import Order, NewOrderResponse
async def createOrder(session:Session, order:Order) -> NewOrderResponse:
    newOrder= OrderModel(
        type= order.type.name,
        department = order.department
    )
    try:
        session.add(newOrder)
        session.flush()
        session.commit()
        return NewOrderResponse(
            id=newOrder._id,
            message='Order Created Successfully',
            status_code=202,
        )
    except Exception as e:
        session.rollback()
        print('exception: ', e)
        return None