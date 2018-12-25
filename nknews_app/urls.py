
from django.urls import path
from .views import home_view,index_view,details_view

urlpatterns = [
    path('',home_view ),
    path('index/',index_view),
    path('<int:id>/', details_view, name='details'),

]
