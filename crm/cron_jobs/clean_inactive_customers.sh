#!/bin/bash
# crm/cron_jobs/clean_inactive_customers.sh

# Absolute paths
PROJECT_DIR="/home/re_birth/alx-backend-graphql_crm"
PYTHON_BIN="$PROJECT_DIR/graph_env/bin/python"
MANAGE="$PROJECT_DIR/manage.py"

# Run Django shell command to delete inactive customers
DELETED=$($PYTHON_BIN $MANAGE shell -c "
from datetime import timedelta
from django.utils import timezone
from crm.models import Customer

cutoff = timezone.now() - timedelta(days=365)
qs = Customer.objects.filter(order__isnull=True, created_at__lt=cutoff)
count = qs.count()
qs.delete()
print(count)
")

# Log results with timestamp
echo "$(date): Deleted $DELETED inactive customers" >> /tmp/customer_cleanup_log.txt

