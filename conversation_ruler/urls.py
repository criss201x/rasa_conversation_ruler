"""
URL configuration for conversation_ruler project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# ...



admin.site.site_header = 'TSDIT - CHATBOT ADMIN'
admin.site.index_title = 'Administrador de intenciones y respuetas chatbot'
admin.site.site_title = 'Administrador de conversaciones'

urlpatterns = [
    path('administrar/', admin.site.urls),
    path('categorias/', include('rules.urls')),
    path('intensiones/', include('intension.urls')),
    path('mensajes_intension/', include('mensaje_intension.urls')),
    path('respuestas/', include('respuesta.urls')),
    path('mensajes_respuesta/', include('mensaje_respuesta.urls')),
    path('', include('login.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)