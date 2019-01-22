
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from nknews_app.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nknews_app/', include('nknews_app.urls')),
    path('login/', login_view, name='login')

]
