from django.urls import path
from User import views
app_name='User'


urlpatterns=[
    path('home/',views.home,name='home'),
    path('myprofile/',views.myprofile,name='myprofile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('changepassword/',views.changepassword,name='changepassword'),
    
]