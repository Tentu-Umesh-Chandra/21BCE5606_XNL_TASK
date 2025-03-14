from fastapi import FastAPI
from src.transaction_processor import TransactionProcessor
from app import routes  # Import routes correctly

app = FastAPI()
processor = TransactionProcessor()

@app.post("/add_order/")
def add_order(order_id: int, price: float, quantity: int, order_type: str):
    matches = processor.process_transaction(order_id, price, quantity, order_type)
    return {"message": "Order added successfully", "matches": matches}

@app.get("/health")
def health_check():
    return {"status": "Server running successfully!"}

# Correctly include your router
app.include_router(routes.router)
