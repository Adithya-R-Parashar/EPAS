from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home , name='home'),
    path('form', views.form, name='form'),
    path('datas', views.datas, name='data'),
    path('output', views.output, name='output'),
    path('emp_details/<int:empno>/', views.emp_details, name='empno'),
    path('rating/<int:empno>/', views.rating, name='rating'),
    path('reg', views.reg, name='reg'),
    path('login', views.login_pg, name='login'),
    path('landing',views.landing, name='landing'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)