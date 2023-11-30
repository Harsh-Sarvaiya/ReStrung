from django.urls import path
from . import views

#URL Conf
urlpatterns = [
    path('hello/', views.say_hello),
    path('main/', views.main),
        path('main/badminton', views.badminton),
        path('main/tennis', views.tennis),
        path('main/squash', views.squash),
        path('main/tennis_cust',views.stringer_tennis_cust),
        path('main/tennis_rating', views.stringer_tennis_rating),
        path('main/tennis_cost', views.stringer_tennis_cost)
]