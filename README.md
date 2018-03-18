This is a very simple web-based REST application for currency conversion. You will need an account on http://openexchangerates.org in order to be able to get the latest exchange rates. After you obtain the APP ID from openexchangerates.org, put it in OPENEXCHANGERATES_APP_ID in the settings.py file.

### Installation and running

This application requires Django 1.11 and Django REST Framework.
Before running the app, be sure to run **python manage.py update_rates** in order to populate the database with latest exchange rates.

```sh
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py update_rates
$ python manage.py runserver 127.0.0.1:8000
```

You can use crontab to run the **manage.py update_rates** periodically. For instance, in order to update the rates every day at 9.00AM, open crontab -e, and enter:
```sh
0 9 * * * python manage.py update_rates >/dev/null 2>&1
```

### Tests
```sh
$ python manage.py test
```