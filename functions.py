def track_order(order_id: str):
    print("Received Order ID:", repr(order_id))

    order_id = order_id.strip().upper()

    orders = {
        "ORD1001": {
            "status": "Shipped",
            "expected_delivery": "20 July 2026"
        },
        "ORD1002": {
            "status": "Out for Delivery",
            "expected_delivery": "19 July 2026"
        },
        "ORD1003": {
            "status": "Delivered",
            "expected_delivery": "17 July 2026"
        }
    }

    print("Available IDs:", list(orders.keys()))

    order = orders.get(order_id)

    if order:
        return (
            f"✅ Order {order_id} is {order['status']}.\n\n"
            f"Expected Delivery: {order['expected_delivery']}"
        )

    return f"❌ Order '{order_id}' was not found."