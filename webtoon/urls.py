from django.urls import path

from webtoon import views

app_name = 'webtoon'

urlpatterns = [
    path('', views.main, name="home"),
    path('crawling/main', views.crawling_main, name='crawling_main'),

]
