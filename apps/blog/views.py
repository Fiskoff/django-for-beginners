from django.template.response import TemplateResponse

def index(request):
    header = "Данные пользователя"
    langs = ["Python", "Java", "C#"]
    user = {"name": "Tom", "age": 23}
    is_show_address = True
    address = ("Абрикосовая", 23, 45)

    data = {"header": header, "langs": langs, "user": user, "is_show_address": is_show_address, "address": address}
    return TemplateResponse(request, "blog/index.html", context=data)


def about(request):
    header = "Наши контакты"
    contacts = {
        "buyer": (
            "Контакты для покупателей", "+7 (3842) 44-03-13"
        ),
        "provider": (
            "Контакты для поставщиков", "+7 (3842) 44-03-09"
        ),
        "applicant": (
            "Контакты для соискателей", "+7 (800) 600-59-99"
        )}

    data = {"header": header, "contacts": contacts}
    return TemplateResponse(request, "blog/about.html", context=data)