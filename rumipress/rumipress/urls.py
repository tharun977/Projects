from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.views.generic.base import RedirectView # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('', RedirectView.as_view(url='books/', permanent=False)),  # Redirect to books app
]
