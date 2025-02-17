from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from main import views as main_views
from about import views as about_views
from news import views as news_views

urlpatterns = [
    path('', main_views.index),
    path('admin/', admin.site.urls),
    path('post/<int:post_id>', news_views.show_post),
    path('page/<int:number_page>', news_views.main),
    path('about/<str:name_part>', about_views.history)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)