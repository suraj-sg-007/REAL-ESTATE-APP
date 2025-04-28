from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from listings.views import (
    home,
    listing_list,
    listing_retrieve,
    listing_create,
    listing_update,
    listing_delete,
    contact,
    register,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('listings/', listing_list, name='listing_list'),
    path('listings/<int:pk>/', listing_retrieve, name='listing_retrieve'),
    path('add-listing/', listing_create, name='listing_create'),
    path('listings/<int:pk>/edit/', listing_update, name='listing_update'),
    path('listings/<int:pk>/delete/', listing_delete, name='listing_delete'),
    path('contact/', contact, name='contact'),  # Contact page
    path('register/', register, name='register'),  # Register page
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout
    # Authentication URLs (Login/Logout/Password Change)
    path('accounts/', include('django.contrib.auth.urls')),  # Includes login, logout, and password URLs
    #path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Custom login view
    
    path('admin/', admin.site.urls),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
