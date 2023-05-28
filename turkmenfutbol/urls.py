from django.urls import path
from .views import*

urlpatterns = [
    path('',Home,name='Home'),
    path('about',About,name='About'),
    path('habarlashmak',Habarlashmak,name='Habarlashmak'),
    path('habarlash',habarlash,name='habarlash'),
    path('eachnews/<int:news_id>',eachnews,name='eachnews'),
    path('table/<str:liga_name>',table,name='table'),
    path('each_video/<int:video_id>',eachvideo,name='eachvideo'),
    path('allnews',All_News,name='All_News'),
    path('allvideo',All_video,name='All_Video'),
    path('liganews/<str:gysga>',liga_news,name='Liga_News'),
]