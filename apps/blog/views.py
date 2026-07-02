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