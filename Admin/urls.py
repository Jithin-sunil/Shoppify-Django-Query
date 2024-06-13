from django.urls import path
from Admin import views
app_name = 'Admin'


urlpatterns = [
        path('district/',views.district,name='district'),
        path('deldistrict/<int:did>',views.deldistrict,name='deldistrict'),
        path('editdistrict/<int:eid>',views.editdistrict,name='editdistrict'),


        path('place/',views.place,name='place'),
]