from django.urls import path
from accountapp.views import hello_world

app_name = 'accountapp'

urlpatterns = [  # 어디로 갈지? 그 주소로 가도록 연결 시켜주기
    path('hello_world/', hello_world, name='hello_world'),
]