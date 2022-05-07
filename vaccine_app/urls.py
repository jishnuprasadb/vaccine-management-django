from django.urls import path

from vaccine_app import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login_view/',views.login_view,name='login_view'),
    path('nurse_registration/',views.nurse_registration,name='nurse_registration'),
    path('user_registration/',views.user_registration,name='user_registration'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('nurse_home/',views.nurse_home,name='nurse_home'),
    path('user_home/',views.user_home,name='user_home'),
    path('vaccine_add/',views.vaccine_add,name='vaccine_add'),
    path('vaccine_view/',views.vaccine_view,name='vaccine_view'),
    path('vaccine_update/<int:id>/',views.vaccine_update,name='vaccine_update'),
    path('vaccine_delete/<int:id>/',views.vaccine_delete,name='vaccine_delete'),
    path('user_view/',views.user_view,name='user_view'),
    path('nurse_view/',views.nurse_view,name='nurse_view'),
    path('hospital_add/',views.hospital_add,name='hospital_add'),
    path('hospital_view/',views.hospital_view,name='hospital_view'),
    path('hospital_update<int:id>/',views.hospital_update,name='hospital_update'),
    path('hospital_delete<int:id>/',views.hospital_delete,name='hospital_delete')

]