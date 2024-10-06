from django.shortcuts import render
from .models import News


# Create your views here.
def home(request):
    # news = [
    #     {
    #         'title': 'Наша первая статья',
    #         'text': 'Полный текст  статьи',
    #         'date': '1 Января 2100 года',
    #         'author': 'Джон'
    #     },
    #
    #     {
    #         'title': 'Наша вторая статья',
    #         'text': 'Полный текст  статьи',
    #         'date': '10 Января 2100 года',
    #         # 'author': 'Джон'
    #     }
    # ]
    number = 50
    data = {
        # 'some': number,
        'news': News.objects.all(),
        'title': 'Главная страница!'

    }

    return render(request, 'blog/home.html', data)

    #other variant
def contacti(request):
    return render(request, 'blog/contact.html', {'title': 'Страница контакты!!!'})



