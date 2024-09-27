from django.urls import path,re_path

from . import views

app_name='users'

urlpatterns=[
    re_path('^new/$',views.newProduct,name='newProduct'),
    re_path('^view/$',views.viewProduct,name='viewProduct'),
    re_path('^delete/$',views.deleteProduct,name='deleteProduct'),
    re_path('^update/$',views.updateProduct,name='updateProduct'),
]