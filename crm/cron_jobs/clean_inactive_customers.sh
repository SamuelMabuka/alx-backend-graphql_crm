#!/bin/bash

# Navigate to project root
cd /home/re_birth/alx-backend-graphql_crm/

# Activate virtual environment
source graph_env/bin/activate

# Run Django shell to delete inactive customers
DELETED=$(python manage.py shell -c '
from crm.models import Customer
from django.utils import timezone
from datetime import timedelta

one_year_ago = timezone.now() - timedelta(days=365)

# Customers with no orders in the last year
inactive = Customer.objects.filter(orders__order_date__lt=one_year_ago) | Customer.objects.filter(orders__isnull=True)
count = inactive.count()
inactive.delete()
print(count)
')

# Log the number of deleted customers with timestamp
echo "$(date): Deleted $DELETED inactive customers" >> /tmp/customer_cleanup_log.txt

