from django.urls import path
from Guest import views
app_name = 'Guest'

urlpatterns =[
        path('user/',views.user,name='user'),
        path('login/',views.login,name='login'),
        path('shop/',views.shop,name='shop'),
        path('ajaxplace/',views.ajaxplace,name='ajaxplace'),
]