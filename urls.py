from django.contrib import admin
from django.urls import path
from.views import *

urlpatterns = [
    path('',home),
    path('home/',home),
    path('addstudents/',add_students),
    path('delete_std/<int:srn>',delete_std),
    path('update_std/<int:srn>',update_std),
    path('doupdate_std/<int:srn>',doupdate_std)

]
