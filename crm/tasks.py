# crm/tasks.py
from celery import shared_task
from datetime import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

@shared_task
def generate_crm_report():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        transport = RequestsHTTPTransport(
            url="http://localhost:8000/graphql",
            verify=True,
            retries=3
        )
        client = Client(transport=transport, fetch_schema_from_transport=False)

        query = gql("""
        {
        totalCustomers: allCustomers {
            id
        }
        totalOrders: allOrders {
            id
            totalAmount
        }
        }
        """)

        result = client.execute(query)
        num_customers = len(result['totalCustomers'])
        num_orders = len(result['totalOrders'])
        total_revenue = sum(order['totalAmount'] for order in result['totalOrders'])

        log_msg = f"{timestamp} - Report: {num_customers} customers, {num_orders} orders, {total_revenue} revenue"
    except Exception as e:
        log_msg = f"{timestamp} - generate_crm_report failed: {e}"

    with open("/tmp/crm_report_log.txt", "a") as f:
        f.write(log_msg + "\n")
