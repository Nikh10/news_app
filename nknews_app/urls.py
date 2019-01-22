
from django.urls import path
from .views import home_view,index_view,details_view,login_view,logout_view,register_view

urlpatterns = [
    path('',home_view ),
    path('index/',index_view),
    path('<int:id>/', details_view, name='details'),
    path('logout', logout_view, name='logout'),
    path('register/', register_view, name='register')

]
