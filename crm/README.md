# CRM Weekly Report Task

## Setup

1. Install Redis and dependencies:
   pip install -r requirements.txt
   Ensure Redis is running at redis://localhost:6379/0

2. Run migrations:
   python manage.py migrate

3. Start Celery worker:
   celery -A crm worker -l info

4. Start Celery Beat:
   celery -A crm beat -l info

5. Verify logs:
   Check /tmp/crm_report_log.txt for weekly CRM report entries.
