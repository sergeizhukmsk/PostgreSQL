from django.urls import path
from .views import platform, games, cart  #, post_list

#path('', post_list, name='home'),  # Здесь мы добавляем маршрут с именем 'home'
#path('post_list/', post_list, name='post_list'),

urlpatterns = [
    path('platform/', platform, name='platform'),
    path('games/', games, name='games'),
    path('cart/', cart, name='cart'),
]

