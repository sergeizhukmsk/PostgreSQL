from django.shortcuts import render
from .models import Game, Post
#from django.core.paginator import Paginator
#from django.core.paginators import Paginator, EmptyPage, PageNotAnInteger
# from django.contrib.auth.hashers import make_password


# def post_list(request):
#     # получаем все посты
#     posts = Post.objects.all()
#     # создаем пагинатор
#     # paginator = Paginator(posts, 5) # 5 постов на странице
#     per_page = int(request.GET.get('per_page', 5))
#     paginator = Paginator(posts, per_page)  # Пагинация с учетом выбранного значения
#     # получаем номер страницы, на которую переходит пользователь
#     page_number = request.GET.get('page', 1)
#     # получаем посты для текущей страницы
#     page_posts = paginator.get_page(page_number)
#     # передаем контекст в шаблон
#
#     context = {
#         'page_posts':page_posts,
#         'paginator':paginator,
#         'per_page':per_page,  # Передаем выбранное значение per_page в контекст
#     }
#
#     return render(request, 'post_list.html', context)


def platform(request):
    return render(request, 'platform.html')


def games(request):
    # Получаем все записи из таблицы Game
    all_games = Game.objects.all()

    # Формируем контекст для передачи в шаблон
    context = {
        'games':all_games
    }
    return render(request, 'games.html', context)


def cart(request):
    return render(request, 'cart.html')

