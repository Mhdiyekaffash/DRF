from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import IsSuperUser, IsStaffOrReadOnly, IsAuthorOrReadOnly, IsSuperUserOrStaffOrReadOnly
from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # authentication_classes =


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # lookup_field = 'slug'  # فیلدی که بر اساس اون قراره object ما select بشه . به صورت پیش فرض pk هست.
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffOrReadOnly, )


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffOrReadOnly, )


# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)

    # def get(self, request):
    #     return Response({"method": "get"})
    #
    # def post(self, request):
    #     return Response({"method": "post"})
    #
    # def put(self, request):
    #     return Response({"method": "put"})

    # def delete(self, request):
    #     request.auth.delete()
    #     return Response(status=204)


# 403 عدم دسترسی

# 401 اشتباه بودن یوزر و پسورد و ااینا

# put update
# 204 delete
#201 created
# 200 get