"""musicology URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from blog.views import UpdatePostView, DeletePostView, frontpage, post_detail, about
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', frontpage, name='frontpage'),
    path('about/', about, name='about'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    
    
]
