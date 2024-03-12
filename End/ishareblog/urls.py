"""ishareblog URL Configuration

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
from django.urls import path,include
from django.views.static import serve
from django.urls import path, include, re_path
from ishareblog.settings import STATIC_ROOT, MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

schema_view=get_schema_view(
    openapi.Info(
        title='ishareblog API',
        default_version='V1',
        description="ishareblog API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    # 配置mdeditor路由
    path(r'mdeditor/', include('mdeditor.urls')),
    # django关闭debug模式后，静态文件无法访问，这里要设置下静态文件的访问路由
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT},name='static'),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}, name='media'),
    # swagger配置
 	re_path(r'^doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # 导出
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # <-- 美化UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # <-- 这里
]

#没有这一步 你添加的图片并不会显示出来
# if settings.DEBUG:
    # static files (images, css, javascript, etc.)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

