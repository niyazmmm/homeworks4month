from django.contrib import admin
from django.urls import path, include

import users
from posts.views import MainPageCBV,ProductCBV , ProductDetailCBV, CreateProductCBV
from Online_Store.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageCBV.as_view()),
    path('products/',ProductCBV.as_view()),
    path('products/<int:id>/', ProductDetailCBV.as_view()),
    path('products/create/',CreateProductCBV.as_view()),

    path("users/", include("users.urls")),

]+ static(MEDIA_URL, document_root=MEDIA_ROOT)
