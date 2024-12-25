from django.contrib import admin
from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('media/<int:post_id>', views.show_post),
    path('page/<int:number_page>', views.main),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)