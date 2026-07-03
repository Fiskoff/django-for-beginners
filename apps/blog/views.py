from django.http import HttpResponse


def get_index(request):
    return HttpResponse("<h2>Главная страница</h2>")

def get_about(request):
    return HttpResponse("<h2>О сайте</h2>")

def get_contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def get_user(request, name:str='Undefined', age:int=0):
    return HttpResponse(f'''
        <h2>Пользователь</h2>
        <div>
            <p>{name}</p>
            <p>{age}</p>
        </div>
    ''')

def products(request, id):
    return HttpResponse("<h2>Все товары</h2>")

def new(request):
    return HttpResponse("<h2>Новые товары</h2>")

def top(request):
    return HttpResponse("<h2>Популярные товары</h2>")

def comment(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")

def question(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")