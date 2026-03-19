from datetime import datetime
from decimal import Decimal
from typing import Optional, List
from pydantic import BaseModel, EmailStr

class SupplierBase(BaseModel):
    name: str
    cnpj: str
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None

class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate(BaseModel):
    name: Optional[str] = None
    cnpj: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None

class SupplierInDBBase(SupplierBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

class Supplier(SupplierInDBBase):
    pass

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    supplier_id: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    supplier_id: Optional[int] = None

class ProductInDBBase(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Product(ProductInDBBase):
    pass

class SupplierWithProducts(Supplier):
    products: List[Product] = []  # opcional, se quiser retornar com relação