from langchain_core.tools import tool


@tool
def track_order(order_id: str) -> str:
    """
    Returns the current status of an order using its order ID.
    """

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

    order_id = order_id.strip().upper()

    if order_id in orders:
        order = orders[order_id]

        return (
            f"Order {order_id} is {order['status']}.\n"
            f"Expected Delivery: {order['expected_delivery']}."
        )

    return "Sorry, I couldn't find that order ID."