from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='home'),
    url(r'^blog/(?P<slug>[\w-]+)/', views.PostDetail.as_view(), name='post_detail'),
]
