from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post_list'),
    url(r'^blog/(?P<slug>[\w-]+)', views.PostDetail.as_view(), name='post_detail'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact_view')
]
