from login_registerapp import views
from django.urls import path
app_name = 'login_registerapp'
urlpatterns = [
    path('login/',views.login,name='login'),
    path('login_logic/',views.login_logic,name='login_logic'),
    path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('register_logic/',views.register_logic,name='register_logic'),
    path('forget/',views.forget_password,name='forget'),
    path('changepwd/',views.change_pwd,name='change'),
    path('changepwd_logic/',views.changepwd_logic,name='change_logic'),
    path('reset/',views.reset,name='reset'),
    path('main/',views.main,name='main'),
    path('contact/',views.contact,name='contact'),
    path('contact_logic/',views.contact_logic,name='contact_logic'),
    path('log_out/',views.log_out,name='log_out'),
]