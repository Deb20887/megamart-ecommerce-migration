from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import os
import boto3
from botocore.exceptions import ClientError

app = FastAPI(title="MegaMart Order Service")

TABLE_NAME = os.getenv("ORDERS_TABLE", "MegaMartOrders")
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table(TABLE_NAME)


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

    order_data = {
        "order_id": order_id,
        "customer_id": order.customer_id,
        "product_id": order.product_id,
        "quantity": order.quantity,
        "status": "CREATED"
    }

    table.put_item(Item=order_data)

    return order_data


@app.get("/orders/{order_id}")
def get_order(order_id: str):
    try:
        response = table.get_item(
            Key={"order_id": order_id}
        )

        item = response.get("Item")

        if item:
            return item

        return {"error": "Order not found"}

    except ClientError:
        return {"error": "Unable to retrieve order"}
