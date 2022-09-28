
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='index.html'), name="login"),
    path('/', LoginView.as_view(template_name='index.html'), name="login"),
    path('usuarios/', include('Usuarios.urls')),
    path('empresas/', include('Empresas.urls')),
    path('logout/', LogoutView.as_view(template_name='index.html'), name="logout")
    ]
