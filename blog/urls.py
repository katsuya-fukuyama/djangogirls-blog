from django.urls import path #本体からインポート
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # post_listへのルーティング
]