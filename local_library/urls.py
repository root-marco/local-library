# urls.py define os mapeamentos de URL para visualização do site. Mesmo que esse arquivo possa conter todo o código para mapeamento de URL, é mais comum delegar apenas o mapeamento para aplicativos específicos, como será visto mais adiante.

from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/')),
]
