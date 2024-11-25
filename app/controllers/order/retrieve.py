from sqlalchemy.orm import Session
from app.models import OrderModel
from app.views import OrderResponse

async def allOrders(session: Session) -> list[OrderResponse]:
    return session.query(OrderModel).all()

async def getOrder(session: Session, id:int) -> OrderResponse:
    return session.query(OrderModel).filter(OrderModel._id == id).first()