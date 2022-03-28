from django.urls import path
from .views import ArticleList, ArticleDetail, UserList, UserDetail

app_name = 'api'

urlpatterns = [
    path('', ArticleList.as_view(), name='List'),
    path('<int:pk>', ArticleDetail.as_view(), name='Detail'),
    path('users/', UserList.as_view(), name='user_list'),
    path('users/<int:pk>', UserDetail.as_view(), name='user_detail'),
]
