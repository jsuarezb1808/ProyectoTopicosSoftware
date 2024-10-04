from django.urls import path,re_path

from . import views

urlpatterns=[
    re_path('^new/$',views.newProduct,name='newProduct'),
    re_path('/',views.viewProducts,name='viewProducts'),
    re_path('^view/<int:id>$',views.detailProduct,name='viewDetailProduct'),
    re_path('^delete/<int:id>$',views.deleteProduct,name='deleteProduct'),
    re_path('^update/<int:id>$',views.updateProduct,name='updateProduct'),
    re_path('^whishlist/<int:id>$',views.wishlistProduct,name='wishlistProduct'),
    re_path('^addToCart/<int:id>$',views.purchaseProduct,name='addToCart'),
    re_path('cart/', views.cart, name='cart'),
    re_path('transaction/', views.transactionPanel, name='transactionPanel'),

]