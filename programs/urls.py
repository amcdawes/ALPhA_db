from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', InstitutionView.as_view(), name='institution_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', InstitutionUpdate.as_view(), name='institution_update'),
    # url(r'instructor/add/$', InstructorCreate.as_view(), name='instructor_add'),
    url(r'instructor/add/(?P<instid>[0-9]+)/$', InstructorCreate.as_view(), name='instructor_add'),
    url(r'instructor/(?P<pk>[0-9]+)/$', InstructorView.as_view(), name='instructor_detail'),
    url(r'instructor/(?P<pk>[0-9]+)/update/$', InstructorUpdate.as_view(), name='instructor_update'),
    url(r'instructor/(?P<pk>[0-9]+)/delete/$', InstructorDelete.as_view(), name='instructor_delete'),
    url(r'course/add/$', CourseCreate.as_view(), name='course_add'),
    url(r'course/(?P<pk>[0-9]+)/$', CourseView.as_view(), name='course_detail'),
    url(r'course/(?P<pk>[0-9]+)/delete/$', CourseDelete.as_view(), name='course_delete'),
    url(r'course/(?P<pk>[0-9]+)/update/$', CourseUpdate.as_view(), name='course_update'),
]
