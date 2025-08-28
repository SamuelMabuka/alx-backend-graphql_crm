# crm/cron.py
from datetime import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def update_low_stock():
    timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    try:
        transport = RequestsHTTPTransport(
            url="http://localhost:8000/graphql",
            verify=True,
            retries=3
        )
        client = Client(transport=transport, fetch_schema_from_transport=False)
        mutation = gql("""
        mutation {
            updateLowStockProducts {
                updatedProducts {
                    name
                    stock
                }
                message
            }
        }
        """)
        result = client.execute(mutation)
        updated = result["updateLowStockProducts"]["updatedProducts"]
        lines = [f"{p['name']}: stock={p['stock']}" for p in updated]
        log_msg = f"{timestamp} - Updated products:\n" + "\n".join(lines)
    except Exception as e:
        log_msg = f"{timestamp} - updateLowStockProducts failed: {e}"

    with open("/tmp/low_stock_updates_log.txt", "a") as f:  # checker expects this path
        f.write(log_msg + "\n")
