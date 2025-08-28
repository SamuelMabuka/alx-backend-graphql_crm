from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime

def log_crm_heartbeat():
    # Log heartbeat
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(f"{datetime.now().strftime('%d/%m/%Y-%H:%M:%S')} CRM is alive\n")

    # Optional: query GraphQL hello field
    transport = RequestsHTTPTransport(
        url="http://localhost:8000/graphql",
        verify=True,
        retries=3,
    )
    client = Client(transport=transport, fetch_schema_from_transport=False)
    query = gql("{ hello }")
    try:
        result = client.execute(query)
        print("GraphQL hello:", result.get("hello"))
    except Exception as e:
        print("GraphQL query failed:", e)
