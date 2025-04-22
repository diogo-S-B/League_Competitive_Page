from django.contrib import admin
from django.urls import path
from app_league import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', views.home, name='home'),
    path ('ltasul/', views.teamname, name='ltasul'),
    path ('lpl/', views.lpl, name='lpl'),
    path ('south/', views.ltasouth, name='ltasouth'),
    path ('north/', views.ltanorth, name='ltanorth'),
    path ('lck/', views.lck, name='lck'),

]
