from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('refresh-token/', refresh_jwt_token),
    path('demanda/', views.DemandaList.as_view(), name='demanda-list'),
    path('^anunciante/', views.AnuncianteList.as_view(),
         name='anunciante-list'),
]
