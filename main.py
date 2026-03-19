from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import schemas, crud
from deps import get_db
from database import init_db

app = FastAPI(title="API Products e Suppliers")


@app.on_event("startup")
def on_startup():
    init_db()


# ---------------- Suppliers ----------------

@app.get("/suppliers", response_model=List[schemas.Supplier])
def list_suppliers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_suppliers(db, skip=skip, limit=limit)


@app.get("/suppliers/{supplier_id}", response_model=schemas.Supplier)
def get_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier = crud.get_supplier(db, supplier_id)
    if not supplier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supplier not found")
    return supplier


@app.post("/suppliers", response_model=schemas.Supplier, status_code=status.HTTP_201_CREATED)
def create_supplier(supplier_in: schemas.SupplierCreate, db: Session = Depends(get_db)):
    return crud.create_supplier(db, supplier_in)


@app.put("/suppliers/{supplier_id}", response_model=schemas.Supplier)
def update_supplier(
    supplier_id: int, supplier_in: schemas.SupplierUpdate, db: Session = Depends(get_db)
):
    supplier = crud.get_supplier(db, supplier_id)
    if not supplier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supplier not found")
    return crud.update_supplier(db, supplier, supplier_in)


@app.delete("/suppliers/{supplier_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier = crud.get_supplier(db, supplier_id)
    if not supplier:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Supplier not found")
    crud.delete_supplier(db, supplier)
    return None


# ---------------- Products ----------------

@app.get("/products", response_model=List[schemas.Product])
def list_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)


@app.get("/products/{product_id}", response_model=schemas.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


@app.post("/products", response_model=schemas.Product, status_code=status.HTTP_201_CREATED)
def create_product(product_in: schemas.ProductCreate, db: Session = Depends(get_db)):
    # opcionalmente validar se supplier existe
    supplier = crud.get_supplier(db, product_in.supplier_id)
    if not supplier:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Supplier")
    return crud.create_product(db, product_in)


@app.put("/products/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: int, product_in: schemas.ProductUpdate, db: Session = Depends(get_db)
):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    if product_in.supplier_id is not None:
        supplier = crud.get_supplier(db, product_in.supplier_id)
        if not supplier:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Supplier")

    return crud.update_product(db, product, product_in)


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    crud.delete_product(db, product)
    return None
