from typing import List, Optional
from sqlalchemy.orm import Session
import models, schemas

def get_supplier(db: Session, supplier_id: int) -> Optional[models.Supplier]:
    return db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()

def get_suppliers(db: Session, skip: int = 0, limit: int = 100) -> List[models.Supplier]:
    return db.query(models.Supplier).offset(skip).limit(limit).all()

def create_supplier(db: Session, supplier_in: schemas.SupplierCreate) -> models.Supplier:
    db_obj = models.Supplier(**supplier_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_supplier(
    db: Session, db_obj: models.Supplier, supplier_in: schemas.SupplierUpdate
) -> models.Supplier:
    data = supplier_in.dict(exclude_unset=True)
    for field, value in data.items():
        setattr(db_obj, field, value)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_supplier(db: Session, db_obj: models.Supplier) -> None:
    db.delete(db_obj)
    db.commit()

def get_product(db: Session, product_id: int) -> Optional[models.Product]:
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100) -> List[models.Product]:
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_product(db: Session, product_in: schemas.ProductCreate) -> models.Product:
    db_obj = models.Product(**product_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_product(
    db: Session, db_obj: models.Product, product_in: schemas.ProductUpdate
) -> models.Product:
    data = product_in.dict(exclude_unset=True)
    for field, value in data.items():
        setattr(db_obj, field, value)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_product(db: Session, db_obj: models.Product) -> None:
    db.delete(db_obj)
    db.commit()
