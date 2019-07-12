from django.urls import path, include
from django.contrib.auth import views
from .views import(
    home_page,
    register,
    project_detail,
)

app_name = 'data_db'

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('project/<slug:slug>/', project_detail, name='detail')
]
