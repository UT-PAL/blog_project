from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name= 'blog_app'
urlpatterns =[
   path('', views.BlogList.as_view(), name='blog_list'),
   path('write/', views.CreateBlog.as_view(), name='create_blog'),
   path('details/<str:slug>', views.blog_details, name='blog_details'),

path('likes/<str:slug>', views.likes, name='like_details'),
path('dislikes/<str:slug>',views.dislikes,name='dislike_details'),
   path('shared/<str:slug>',views.shared_blog,name='shared_blog'),
path('my_shared_blogs/',views.my_shared_blogs,name='my_shared_blogs'),
   path('liked/<pk>/', views.liked, name='liked_post'),
   path('unliked/<pk>/', views.unliked, name='unliked_post'),
   path('dislike/<pk>/', views.dislike, name='dislike_post'),
   path('disliked/<pk>/', views.disliked, name='disliked_post'),
   path('my-blogs/', views.MyBlogs.as_view(), name='my_blogs'),
   path('edit/<pk>/', views.UpdateBlog.as_view(), name='edit_blog'),
   path('search/',views.search,name='search'),
   path('delete/<str:slug>',views.delete_blogs,name='delete_blogs')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
