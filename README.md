# Django user notification

[![GitHub license](https://img.shields.io/github/license/anyidea/django-user-notification)](https://github.com/anyidea/django-user-notification/blob/master/LICENSE)
[![pypi-version](https://img.shields.io/pypi/v/django-user-notification.svg)](https://pypi.python.org/pypi/drfexts)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-user-notification)
[![PyPI - Django Version](https://img.shields.io/badge/django-%3E%3D3.0-44B78B)](https://www.djangoproject.com/)
[![Build Status](https://app.travis-ci.com/anyidea/django-user-notification.svg?branch=master)](https://app.travis-ci.com/anyidea/django-user-notification)


Overview
-----
Django user notification is intended to provide a way to send multiple types of notification messages to django users out of box
 and docs are on the way...

Requirements
-----

* Python (3.8, 3.9, 3.10)
* Django (3.0, 3.1, 3.2, 4.0, 4.1)

We **highly recommend** and only officially support the latest patch release of
each Python and Django series.

Installation
-----

Install using `pip`...

    pip install django-user-notification

Add `'notification'` to your `INSTALLED_APPS` setting.
```python
INSTALLED_APPS = [
    ...
    'notification',
]
```

Quick Start
-----

Let's take a look at a quick start of using Django user notification to send notification messages to users.

Run the `notification` migrations using:

    python manage.py migrate notification


Add the following to your `settings.py` module:

```python
INSTALLED_APPS = [
    ...  # Make sure to include the default installed apps here.
    'rest_framework',
]

DJANGO_USER_NOTIFICATION = {
    "aliyunsms": {
        "access_key_id": "ACCESS_KEY_ID",
        "access_key_secret": "ACCESS_KEY_SECRET",
        "sign_name": "SIGN_NAME",
    },
    "dingtalkchatbot": {
        "webhook": "DINGTALK_WEBHOOK",
    },
    "dingtalkworkmessage": {
        "agent_id": "DINGTALK_AGENT_ID",
        "app_key": "DINGTALK_APP_KEY",
        "app_secret": "DINGTALK_APP_SECRET",
    },
    "dingtalktodotask": {
        "app_key": "DINGTALK_APP_KEY",
        "app_secret": "DINGTALK_APP_SECRET",
    },
}
```

Let's send a notification

``` {.python}
from django.contrib.auth import get_user_model
from notification.backends import notify_by_email, notify_by_dingtalk_workmessage

User = get_user_model()

recipient = User.objects.first()

# send a dingtalk work message notification
notify_by_dingtalk_workmessage([recipient], phone_field="phone", title="This is a title", message="A test message")


# send a email notiofication
notify_by_email([recipient], title="This is a title", message="A test message")
```

Send Message With Template
--------------

`django-user-notification` support send notifications with custom template, To
specify a custom message template you can provide the `template_code`
and `context` parameters.

1)  Create a template message with code named `TMP01` on django admin



2) Provide the `template_code` and `context` to `send` method:
``` {.python}
...

notify_by_email([recipient], template_code="TMP01", context={"content": "Hello"})
```



Running the tests
-----------------

To run the tests against the current environment:

``` {.bash}
$ ./manage.py test
```

### Changelog

0.5.0
-----

-   Initial release

## Thanks

[![PyCharm](docs/pycharm.svg)](https://www.jetbrains.com/?from=drfexts)
