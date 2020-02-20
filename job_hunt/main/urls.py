from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
        path('', views.main, name='main'),
        path('login/', LoginView.as_view(template_name="main/login.html")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)