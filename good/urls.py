from django.urls import path

from good.views import good_change

app_name = 'good'

urlpatterns = [
    path('<uuid:post_id>/', good_change, name='good_change'),
]