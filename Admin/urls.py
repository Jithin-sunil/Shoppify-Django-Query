from django.urls import path
from Admin import views
app_name = 'Admin'


urlpatterns = [
        path('district/',views.district,name='district'),
        path('deldistrict/<int:did>',views.deldistrict,name='deldistrict'),
        path('editdistrict/<int:eid>',views.editdistrict,name='editdistrict'),


        path('place/',views.place,name='place'),
        path('delplace/<int:pid>',views.delplace,name='delplace'),
        path('editplace/<int:eid>',views.editplace,name='editplace'),


        path('category/',views.category,name='category'),
        path('delcategory/<int:cid>',views.delcategory,name='delcategory'),
        path('editcategory/<int:eid>',views.editcategory,name='editcategory'),


        path('subcategory/',views.subcategory,name='subcategory'),
        path('delsubcategory/<int:sid>',views.delsubcategory,name='delsubcategory'),
        path('editsubcategory/<int:eid>',views.editsubcategory,name='editsubcategory'),

        path('admin/',views.admin,name='admin'),

        path('home/',views.home,name='home'),
]