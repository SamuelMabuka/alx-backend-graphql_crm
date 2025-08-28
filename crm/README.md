# CRM Weekly Report Task

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Run migrations:
   python manage.py migrate

3. Start Celery worker:
   celery -A crm worker -l info

4. Start Celery Beat:
   celery -A crm beat -l info

5. Verify logs:
   /tmp/crm_report_log.txt