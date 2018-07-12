from django.urls import path, include
from . import views



#app_name 设置命名空间
app_name='polls'

urlpatterns = [
     # ex: /polls/
    path('', views.IndexView.as_view(),name='index'),

    # ex: /polls/5/
#DetailView 期望从 URL 中捕获名为 "pk" 的主键值
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),

    #ex: /polls/5/results/
    path('<int:pk>/results/',views.ResultView.as_view(),name='results'),

    #ex: /polls/5/vote/
    path('<int:question_id>/vote/',views.vote,name='vote'),
]
