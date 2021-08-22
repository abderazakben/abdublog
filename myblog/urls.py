from django.urls import path 
from . import views
from .views import HomeView , ArticleDetalView , CategorylistView, AddPostView , UpdatePostView ,DeletePostView , AddCategorView , CategoryView ,likeView ,AddCommentView , AdminLoginView ,AdminHome , courMView , AboutView

app_name = "myblog"
urlpatterns = [
 
  #path('', views.home, name="home"),
  path('', HomeView.as_view(), name="home"),
  path('articl/<int:pk>',ArticleDetalView.as_view(),name='article_detaile'),
  path('add_post/' , AddPostView.as_view() , name='add_post'),
  path('add_category/' , AddCategorView.as_view() , name='add_category'),
  path('article/edit/<int:pk>' , UpdatePostView.as_view() , name='updet_post'),
  path('article/<int:pk>/remove' , DeletePostView.as_view() , name='delete_post'),
  path('category/<str:cats>/', CategoryView, name='category'),
  path('category-list/',CategorylistView, name='category-list'),
  path('like/<int:pk>', likeView, name='like_post'),
  path('article/<int:pk>/comment/', AddCommentView.as_view(),name='add_comment'),
   path('about/', AboutView.as_view() , name= 'about'),
############ admin path ##########

path("admin-login/" , AdminLoginView.as_view() , name="admin"),
path("admin-home/" , AdminHome.as_view(), name="adminhome"),
path('motaki_dris/' , views.courMView , name='motaki_dris'),


]
