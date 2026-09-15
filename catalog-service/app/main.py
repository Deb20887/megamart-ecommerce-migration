from fastapi import FastAPI

app = FastAPI(title="MegaMart Catalog Service")

products = [
    {"id": 1, "name": "Laptop", "price": 65000, "inventory": 20},
    {"id": 2, "name": "Smartphone", "price": 30000, "inventory": 50},
    {"id": 3, "name": "Headphones", "price": 5000, "inventory": 100}
]


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/products")
def get_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}


@app.get("/inventory/{product_id}")
def get_inventory(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return {
                "product_id": product_id,
                "inventory": product["inventory"]
            }
    return {"error": "Product not found"}
