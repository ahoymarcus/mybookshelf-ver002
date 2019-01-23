"""myLocalLibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
] 


# 1. nserting a new path to the apps installed in the project
# Note: as a reminder the path object was reimported for this step
#Note: Whenever Django encounters the import function django.urls.include(), it splits the URL string at the designated end character and sends the remaining substring to the included URLconf module for further processing.
from django.urls import include
from django.urls import path

urlpatterns += [
	path('catalog/', include('catalog.urls'))
]


# 2. Adding a URL maps to redirect the base Project URL to the Catalog application
# Note: at 2. the string is empty because '/' is already implied!
from django.views.generic import RedirectView

urlpatterns += [
	path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]


# 3. Using static() to give this ability to the django development server (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Adding Django site authentication urls (for login, logout, password management)
urlpatterns += [
	path('accounts/', include('django.contrib.auth.urls')),
]