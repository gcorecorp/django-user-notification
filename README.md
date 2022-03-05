# django-user-notification

[![GitHub license](https://img.shields.io/github/license/anyidea/django-user-notification)](https://github.com/anyidea/django-user-notification/blob/master/LICENSE)
[![pypi-version](https://img.shields.io/pypi/v/django-user-notification.svg)](https://pypi.python.org/pypi/drfexts)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-user-notification)
[![PyPI - Django Version](https://img.shields.io/badge/django-%3E%3D3.0-44B78B)](https://www.djangoproject.com/)
[![Build Status](https://app.travis-ci.com/anyidea/django-user-notification.svg?branch=master)](https://app.travis-ci.com/anyidea/django-user-notification)

**A Notification Backend For Django**

Installation
------------

``` {.bash}
$ pip install django-user-notification
```

Quick Start
-----

1) Add default notification backend and set dingding webhook url.

``` {.python}
NOTIFICATION_BACKENDS = [
    'notification.backends.DingDingBotNotificationBackend'
]
DINGDING_WEBHOOK = (
    'https://oapi.dingtalk.com/robot/send?access_token=xxxx'
)
```
2) Send notification to django users.
``` {.python}
from django.contrib.auth import get_user_model
from notification.backends import notify_by_dingding

User = get_user_model()

receiver = User.objects.first()

notify_by_dingding([receiver,], message="This is a test notification")
```

Custom Message Template
--------------

By default, a `CSVRenderer` will output fields in sorted order. To
specify a custom message template you can provide the `template_code`
and `context` parameters. There are two ways to do this:

1)  Create a new renderer class and override the `header` attribute
    directly:

    > ``` {.python}
    > class MyUserRenderer (CSVRenderer):
    >     header = ['first', 'last', 'email']
    >
    > @api_view(['GET'])
    > @renderer_classes((MyUserRenderer,))
    > def my_view(request):
    >     users = User.objects.filter(active=True)
    >     content = [{'first': user.first_name,
    >                 'last': user.last_name,
    >                 'email': user.email}
    >                for user in users]
    >     return Response(content)
    > ```

2)  Use the `renderer_context` to override the field ordering on the
    fly:

    > ``` {.python}
    > class MyView (APIView):
    >     renderer_classes = [CSVRenderer]
    >
    >     def get_renderer_context(self):
    >         context = super().get_renderer_context()
    >         context['header'] = (
    >             self.request.GET['fields'].split(',')
    >             if 'fields' in self.request.GET else None)
    >         return context
    >
    >     ...
    > ```


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
