from fastapi import FastAPI, Query, Body
from pydantic import BaseModel
from typing import List, Optional
import os
from datetime import date
import pandas as pd

app = FastAPI(title="API Data of Sales")


sales_df = pd.DataFrame({
    'id' : range(1, 11),
    'product':['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphone',
    'WebCam', 'SSD', 'RAM', 'GPU', 'CPU'],
    'category': ['Computers', 'Acessories', 'Acessories', 'Periferics', 
                 'Audio','Periferics', 'Components', 'Components', 
                 'Components', 'Components'],
    'price': [3500, 150, 200, 1200, 350, 180, 450, 300, 20000, 1500],
    'sales_volume': [12, 85, 63, 35, 42, 30, 55, 70, 22, 15]  
})


class Product(BaseModel):
    id: int
    product: str
    category: str
    price: float
    sales_volume: int


class ProductCreate(BaseModel):
    product: str
    category: str
    price: float
    sales_volume: int

@app.get("/")
def read_root():
    return {"mensagem": "API Data of Sales"}

@app.get("/products", response_model=List[Product])
def get_products(
    category: Optional[str] = Query(None, description="Category Filter"),
    min_price: Optional[float] = Query(None, description="minor Price"),
    max_price: Optional[float] = Query(None, description="max Price")
):
    df = sales_df.copy()

    if category:
        df = df[df['category'] == category]

    if min_price is not None:
        df = df[df['price'] >= min_price]

    if max_price is not None:
        df = df[df['price'] <= max_price]

    return df.to_dict(orient='records')


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = sales_df[sales_df['id'] == product_id]
    if not product.empty:
        return product.iloc[0].to_dict()
    return {"error": "Product Not Found"}

# Endpoint for insert new data - available only Docker Compose
@app.post("/products", response_model=Product)
def create_sale(sale: ProductCreate):
    # In Docker Compose Example, this method saved in PostgreSQL
    global sales_df

    new_id = sales_df['id'].max() + 1 if not sales_df.empty else 1
    new_product = {
        'id': new_id,
        **sale.dict()
    }
    sales_df = pd.concat([sales_df, pd.DataFrame([new_product])])
    return new_product
