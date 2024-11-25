from pydantic import BaseModel, Field
from typing import Optional, Required
import enum

class OrderType(enum.Enum):
    CONSULTATION='CONSULTATION'
    LAB='LAB'
    IMAGING='IMAGING'
    MEDICATION='MEDICATION'

class OrderStatus(enum.Enum):
    PENDING='PENDING'
    PROCESSED='PROCESSED'
    REJECTED='REJECTED'

#the base for all order responses
class OrderResponseBase(BaseModel):
    id: Optional[int] = Field(..., title='Order Identifier', description='Id to identify an order', examples=[1])
    message: Optional[str] = Field(..., title='Update order type message', description='Describe the response', examples=['Order\'s type has been updated', 'Order\'s type update failed'])
    status_code: int = Field(..., title='Response Code', description='Status code of the request', examples=[200, 400, 500])

#update specific order's type response
class UpdateOrderTypeResponse(OrderResponseBase):
    old_type: OrderType = Field(..., title='Old order type', description='The old type of order of a patient', examples=['CONSULTATION', 'LAB', 'IMAGING', 'MEDICATION'])
    new_type: OrderType = Field(..., title='Order type', description='The type of order of a patient', examples=['CONSULTATION', 'LAB', 'IMAGING', 'MEDICATION'])

#update specific order's status response
class UpdateOrderStatusResponse(OrderResponseBase):
    old_status: OrderStatus = Field(..., title='Old order status', description='old status of an order', examples=['PENDING', 'PROCESSED', 'REJECTED'])
    new_status: OrderStatus = Field(..., title='New order status', description='New status of an order', examples=['PENDING', 'PROCESSED', 'REJECTED'])

#update specific order's department response
class UpdateOrderDepartmentResponse(OrderResponseBase):
    old_dept: int =  Field(..., title='Old order department', description='The old department of an order', examples=[1])
    new_dept: int =  Field(..., title='New order department', description='The new respective department of an order', examples=[2])

class ReceptionistUpdateResponse(UpdateOrderTypeResponse, UpdateOrderDepartmentResponse):
    pass

#create new order response
class NewOrderResponse(OrderResponseBase):
    id: int = Field(..., title='Order Identifier', description='Id to identify an order', examples=[1])
    def __json__(self):
        return{
            'id': self.id,
            'message': self.message,
            'status_code': self.status_code
        }
#retrieve/delete an specific order response
class DeleteOrderResponse(OrderResponseBase):
    id: int = Field(..., title='Order Identifier', description='Id to identify an order', examples=[1])
    operation: str = Field(..., title='The applied operation', description='The operation has been performed on order', examples=['delete'])

#retrieve orders response
class OrderResponse(OrderResponseBase):
    id: int = Field(..., title='Order Identifier', description='Id to identify an order', examples=[1])
    type: OrderType = Field(..., title='Order type', description='The type of order of a patient', examples=['CONSULTATION', 'LAB', 'IMAGING', 'MEDICATION'])
    status: OrderStatus = Field(..., title='Order status', description='New status of an order', examples=['PENDING', 'PROCESSED', 'REJECTED'])
    department: int = Field(..., title='Order department', description='The respective department of an order', examples=['Emergency'])
