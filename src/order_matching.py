import heapq

class Order:
    def __init__(self, order_id, price, quantity, timestamp):
        self.order_id = order_id
        self.price = price
        self.quantity = quantity
        self.timestamp = timestamp

    def __lt__(self, other):
        return (self.price, self.timestamp) < (other.price, other.timestamp)

class OrderBook:
    def __init__(self):
        self.buy_orders = []  # Max-heap (highest price gets priority)
        self.sell_orders = []  # Min-heap (lowest price gets priority)

    def add_order(self, order, order_type):
        if order_type == 'buy':
            heapq.heappush(self.buy_orders, (-order.price, order))
        else:
            heapq.heappush(self.sell_orders, (order.price, order))

    def match_orders(self):
        matched_orders = []
        
        while self.buy_orders and self.sell_orders:
            best_buy = self.buy_orders[0][1]
            best_sell = self.sell_orders[0][1]

            if best_buy.price >= best_sell.price:
                matched_qty = min(best_buy.quantity, best_sell.quantity)
                best_buy.quantity -= matched_qty
                best_sell.quantity -= matched_qty
                
                matched_orders.append(f"Matched {matched_qty} units at price {best_sell.price}")
                
                if best_buy.quantity == 0:
                    heapq.heappop(self.buy_orders)
                if best_sell.quantity == 0:
                    heapq.heappop(self.sell_orders)
            else:
                break
        
        return matched_orders
