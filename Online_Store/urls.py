from django.contrib import admin
from django.urls import path
from posts.views import (main_view,
                         products_view,
                         product_detail_view,
                         product_create_view)
from django.conf.urls.static import static
from Online_Store import settings
from users.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/', products_view),
    path('products/<int:id>/', product_detail_view),
    path('products/create/', product_create_view),
    path('users/register/', register_view),
    path('users/login/', login_view),
    path('users/logout/', logout_view)

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
