from django.urls import path
from .views import Index,About,Order,OrderConfirmation,OrderPayConfirmation,Menu,MenuSearch
urlpatterns = [
    path('',Index.as_view(),name="index"),
    path('About/',About.as_view(),name="about"),
    path('Order/',Order.as_view(),name="order"),
    path('Order-Confirmation/<int:pk>',OrderConfirmation.as_view(),name="order-confirmation"),
    path('Payment-Confirmation/<int:pk>',OrderPayConfirmation.as_view(),name="payment-confirmation"),
    path('menu/',Menu.as_view(),name="menu"),
    path('menu/search/',MenuSearch.as_view(),name="menu-search"),
]
