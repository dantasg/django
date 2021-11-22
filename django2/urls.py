from django.contrib import admin
from django.urls import path, include

from core.views import index, contato

urlpatterns = [
    path('painel/', admin.site.urls),
    path('', include('core.urls'))
]
