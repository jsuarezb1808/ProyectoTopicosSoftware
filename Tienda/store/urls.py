from django.urls import path,re_path

from . import views

app_name='users'

urlpatterns=[
    re_path('^new/$',views.newProduct,name='newProduct'),
    re_path('^view/$',views.viewProduct,name='viewProduct'),
    re_path('^view/<int:id>$',views.detailProduct,name='viewDetailProduct'),
    re_path('^delete/<int:id>$',views.deleteProduct,name='deleteProduct'),
    re_path('^update/<int:id>$',views.updateProduct,name='updateProduct'),
    re_path('^whishlist/<int:id>$',views.wishlistProduct,name='wishlistProduct'),
    re_path('^addToCart/<int:id>$',views.purchaseProduct,name='addToCart'),

]