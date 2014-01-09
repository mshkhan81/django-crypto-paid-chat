django-crypto-paid-chat
=======================

Example application for [django-cryptocoin]

Quick Start
===========

1. Install requirements `pip install -r requirements.txt`

2. Run a local cryptocoins instance with accepting JSON-RPC commands.

3. Rename `settings_local.py-example` to `settings_local.py` and check settings

4. Run `python manage.py syncdb` and `python manage.py migrate`

5. Run `python manage.py get_exchange_rates` and add this command to cron (every 5 minutes)

6. Run `python manage.py check_incomings` and add this command to cron (every minute)

7. Run `python manage.py runserver` and go to `http://127.0.0.1:8000`



[django-cryptocoin]:https://github.com/quantum13/django-cryptocoin