from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI(title="MegaMart Order Service")

orders = {}


class OrderRequest(BaseModel):
    customer_id: str
    product_id: int
    quantity: int


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/orders")
def create_order(order: OrderRequest):
    order_id = str(uuid.uuid4())

    orders[order_id] = {
        "order_id": order_id,
        "customer_id": order.customer_id,
        "product_id": order.product_id,
        "quantity": order.quantity,
        "status": "CREATED"
    }

    return orders[order_id]


@app.get("/orders/{order_id}")
def get_order(order_id: str):
    return orders.get(order_id, {"error": "Order not found"})
