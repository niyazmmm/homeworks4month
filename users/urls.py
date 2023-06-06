from django.urls import path
from .views import LoginCBV, LogoutCBV, RegisterCBV

urlpatterns = [
    path('login/', LoginCBV.as_view()),
    path('register/', RegisterCBV.as_view()),
    path('logout/', LogoutCBV.as_view())
]
