from fastapi import APIRouter, HTTPException
from app.views import (
    OrderResponse, 
    NewOrderResponse, 
    Order, 
    ReceptionistUpdateOrder,
    ReceptionistUpdateResponse
    )
from app.config import session
from app.controllers import (
    allOrders as controller_allOrders,
    getOrder as controller_getOrder,
    createOrder as controller_createOrder,
    updateTypeDept as controller_updateTypeDept,
    deleteOrder as controller_deleteOrder
)

order_router = APIRouter()

@order_router.get(
    '/orders',
    name='Get all orders',
    description='Retrieve all orders', 
    response_model=list[OrderResponse],
)
async def allOrders() -> list[OrderResponse]:
    orders = await controller_allOrders(session= session)
    if orders is None:
        raise HTTPException(status_code=404, detail= [])
    return [OrderResponse(id= row._id, message='orders found', status_code=200, type=row.type.value, status=row.status.value, department=row.department) for row in orders]


@order_router.get(
    '/orders/{id}',
    name='Get specific order',
    description='Retrieve specific order', 
    response_model=OrderResponse,
)
async def getOrder(id:int) -> OrderResponse:
    return await controller_getOrder(session= session, id=id)


@order_router.post(
    '/order',
    name='Create new order',
    description='Create new order instance',
    response_model=NewOrderResponse
)
async def createOrder(request:Order) -> NewOrderResponse:
    created = await controller_createOrder(session=session, order=request)
    if created is None:
        raise HTTPException(status_code=500, detail=NewOrderResponse(id=-1, message='Fail to create order', status_code=500).__json__())
    return created

@order_router.put(
    '/update',
    name='Update order type/department',
    description='Update Order type, respictive department or both',
    response_model=ReceptionistUpdateResponse
)
async def updateTypeDept(request: ReceptionistUpdateOrder) -> ReceptionistUpdateResponse:
    updated = await controller_updateTypeDept(session=session, request=request)

    if updated is None:
        detail = {'message': 'failed', 'status_code':404}
        raise HTTPException(status_code=404, detail= detail)
    return updated

@order_router.delete(
    '/order/{id}',
    name='Delete Order',
    description='Delete Order Using Order id',
)
async def deleteOrder(id:int):
    deleted = await controller_deleteOrder(session=session, id=id)
    if not deleted:
        raise HTTPException(status_code=400, detail={'message': 'Deletion failed', 'code': 400})
    return {'message': 'Order deleted successfully', 'code': 200}