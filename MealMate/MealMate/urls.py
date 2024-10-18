"""
URL configuration for MealMate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from management.views import home_view
from forum.views import forum_home_view,forum_post_view,post_detail
from django.conf import settings
from django.conf.urls.static import static
from api.views import PostListView,SearchPostView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home_view, name='home'),
    path('forum/',forum_home_view,name='forum_home'),
    path('forum/<int:forum_id>/',forum_post_view,name='forum_post'),
    path('forum/post/<uuid:uuid>/', post_detail, name='post_detail'),
    path('api/posts/', PostListView.as_view(), name='post-list'),
    path('search/post/', SearchPostView.as_view(), name='search-post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
