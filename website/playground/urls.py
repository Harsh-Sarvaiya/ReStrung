from django.urls import path
from . import views

#URL Conf
urlpatterns = [
    path('hello/', views.say_hello),
    path('main/', views.main),
        path('main/badminton', views.badminton),
        path('main/tennis', views.tennis),
        path('main/squash', views.squash),
        path('main/full_stringer_list',views.full_stringer_list)
]