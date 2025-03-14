from src.order_matching import OrderBook, Order

class TransactionProcessor:
    def __init__(self):
        self.order_book = OrderBook()

    def process_transaction(self, order_id, price, quantity, order_type):
        order = Order(order_id, price, quantity, timestamp=0)
        self.order_book.add_order(order, order_type)
        return self.order_book.match_orders()
