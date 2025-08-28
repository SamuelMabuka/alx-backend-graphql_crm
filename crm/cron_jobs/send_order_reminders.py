#!/usr/bin/env python3

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime, timedelta

# GraphQL endpoint
transport = RequestsHTTPTransport(
    url="http://localhost:8000/graphql",
    verify=True,
    retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=False)

# Calculate last week's date
seven_days_ago = (datetime.now() - timedelta(days=7)).isoformat()

# GraphQL query to get orders from the last 7 days
query = gql(
    """
    query getRecentOrders($since: DateTime!) {
    allOrders(filter: {orderDate_Gte: $since}) {
        id
        customer {
        email
        }
        orderDate
    }
    }
    """
)

params = {"since": seven_days_ago}

try:
    result = client.execute(query, variable_values=params)
    orders = result.get("allOrders", [])

    with open("/tmp/order_reminders_log.txt", "a") as log_file:
        for order in orders:
            log_file.write(f"{datetime.now()}: Order {order['id']} - {order['customer']['email']}\n")

    print("Order reminders processed!")

except Exception as e:
    print(f"Error fetching orders: {e}")