from django.conf.urls import url

from my_app import views


urlpatterns = [ 
    url(r'^api/users$', views.user_list),
]
