from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from salam.views import Index,inserting,Delete
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',Index,name='index'),
    path('',inserting,name='regform'),
    path('delete/<int:item_id>',Delete,name='Delete'),

]
