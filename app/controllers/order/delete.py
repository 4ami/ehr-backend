from sqlalchemy.orm import Session
from app.models import OrderModel

async def deleteOrder(session: Session, id:int) -> bool:
    order = session.query(OrderModel).filter(OrderModel._id == id).first()
    if order is None: return False
    session.delete(order)
    session.commit()
    return True