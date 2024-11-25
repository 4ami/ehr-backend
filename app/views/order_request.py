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

#the base for all order requests
class OrderBase(BaseModel):
    id: Optional[int] = Field(..., title='Order Identifier', description='Id to identify an order', examples=[1])

#update specific order's type request
class UpdateOrderType(OrderBase):
    id: int = Field(..., title='Order Identifier', description='Id to identify an order', examples=[1])
    type: OrderType = Field(..., title='Order type', description='The type of order of a patient', examples=['CONSULTATION', 'LAB', 'IMAGING', 'MEDICATION'])

#update specific order's status request
class UpdateOrderStatus(OrderBase):
    id: int = Field(..., title='Order Identifier', description='Id to identify an order', examples=[1])
    status: OrderStatus = Field(..., title='Order status', description='New status of an order', examples=['PENDING', 'PROCESSED', 'REJECTED'])

#update specific order's department request
class UpdateOrderDepartment(OrderBase):
    id: int = Field(..., title='Order Identifier', description='Id to identify an order', examples=[1])
    department: int = Field(..., title='Order department', description='The respective department of an order', examples=[1])

class ReceptionistUpdateOrder(UpdateOrderType, UpdateOrderDepartment):
    # id: int = Field(..., title='Order Identifier', description='Id to identify an order', examples=[1])
    # type: OrderType = Field(..., title='Order type', description='The type of order of a patient', examples=['CONSULTATION', 'LAB', 'IMAGING', 'MEDICATION'])
    # department: int = Field(..., title='Order department', description='The respective department of an order', examples=[1])
    pass
#create a new order request
class Order(OrderBase):
    type: OrderType = Field(..., title='Order type', description='The type of order of a patient', examples=['CONSULTATION', 'LAB', 'IMAGING', 'MEDICATION'])
    status: OrderStatus = Field(..., title='Order status', description='New status of an order', examples=['PENDING', 'PROCESSED', 'REJECTED'])
    department: int = Field(..., title='Order department', description='The respective department of an order', examples=[1])

#delete an specific order request
class DeleteOrder(OrderBase):
    id: int = Field(..., title='Order Identifier', description='Id to identify an order', examples=[1])