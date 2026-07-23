from django.template.response import TemplateResponse

def index(request):
    header = "Данные пользователя"
    langs = ["Python", "Java", "C#"]
    user = {"name": "Tom", "age": 23}
    is_show_address = True
    address = ("Абрикосовая", 23, 45)

    data = {"header": header, "langs": langs, "user": user, "is_show_address": is_show_address, "address": address}
    return TemplateResponse(request, "blog/index.html", context=data)