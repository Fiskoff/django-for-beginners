from django.http import HttpResponse
from django.shortcuts import render

from apps.crud.forms import UserForm


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        return HttpResponse(f'<h2>Привет, {name}, твой возраст: {age}</h2>')
    else:
        user_form = UserForm()
        return render(request, 'crud/index.html', {'form': user_form})