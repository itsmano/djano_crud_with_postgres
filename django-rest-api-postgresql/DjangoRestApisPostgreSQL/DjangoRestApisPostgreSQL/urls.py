from django.conf.urls import url, include
# from django.contrib.auth import admin
from django.contrib import admin

urlpatterns = [ 
    url(r'^', include('my_app.urls')),
    url(r'^admin/', admin.site.urls),

    # url(r'^', include('myapp.urls')),
]
