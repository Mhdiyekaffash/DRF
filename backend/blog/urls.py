from django.urls import path
from .views import ArticleList, ArticleDetail

app_name = 'blog'

urlpatterns = [
    path('', ArticleList.as_view(), name='List'),
    path('<int:pk>', ArticleDetail.as_view(), name='detail'),
]
