from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^api/currencies/(?P<curr_from>[A-Z]{3})/(?P<curr_to>[A-Z]{3})$',
        views.get_rate,
        name='get_rate'
    ),
    url(
        r'^api/currencies/$',
        views.get_currencies,
        name='get_currencies'
    )
]
