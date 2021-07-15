from django.urls import path
from .import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('',views.signin,name='signin'),
    path('update/<int:pk>/',views.edit_user_details,name='update'),
    path('detelete/<int:pk>/',views.deleteuserdetails,name='delete'),
    path('passchange/',views.change_pass,name='changepass'),
]