from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='institution_detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', EditView.as_view(), name='institution_edit'),
    url(r'instructor/add/$', InstructorCreate.as_view(), name='instructor_add'),
    url(r'instructor/(?P<pk>[0-9]+)/$', InstructorView.as_view(), name='instructor_detail'),
    url(r'instructor/(?P<pk>[0-9]+)/update/$', InstructorUpdate.as_view(), name='instructor_update'),
    url(r'instructor/(?P<pk>[0-9]+)/delete/$', InstructorDelete.as_view(), name='instructor_delete'),
]
