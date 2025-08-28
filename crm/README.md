# CRM Celery Setup

This document explains how to set up the CRM weekly report task using Celery and Celery Beat, integrating with the GraphQL schema.

## 1. Install Redis and dependencies
Make sure Redis is installed and running. Then install Python dependencies:

```bash
# Install Redis (Linux example)
sudo apt-get install redis-server

# Install Python dependencies
pip install -r requirements.txt

Dependencies include:

celery

django-celery-beat

redis

graphene-django

gql (for GraphQL queries)

## 2. Run Django migrations

Apply all migrations for Django apps including crm:
python manage.py migrate

## 3. Start Celery worker

Start the Celery worker to process asynchronous tasks:
celery -A crm worker -l info

## 4. Start Celery Beat

Start Celery Beat to schedule periodic tasks:
celery -A crm beat -l info
The generate_crm_report task is scheduled to run weekly (every Monday at 6:00 AM).

## 5. Verify logs

Check the weekly CRM report logs to ensure the task ran successfully:
cat /tmp/crm_report_log.txt
The log entries follow this format: YYYY-MM-DD HH:MM:SS - Report: X customers, Y orders, Z revenue
