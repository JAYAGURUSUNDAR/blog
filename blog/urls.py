from django.urls import path
from .views import blog_detail, index, login_view, user_page
app_name = 'blog'
urlpatterns = [
    path('', index),
    path('blog/<int:pk>/', blog_detail, name='blog_detail'),
    path('login/', login_view, name='login'),
    path('user/', user_page, name='user_page')
]
