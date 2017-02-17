from django.conf.urls import url

from . import views
from Tiffin_Mgmt.models import Tiffin_Mgmt

urlpatterns = [
    
    url(r'^home/$', views.home, ),
    url(r'^add_launch/$', views.add_launch),

    ]
