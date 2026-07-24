from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from apps.crud.models import Person


def index(request):
    people = Person.objects.all()
    return render(request, 'crud/index.html', {'people': people})

def create(request):
    if request.method == 'POST':
        person = Person()
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save()
    return redirect('index')

def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == 'POST':
            person.name = request.POST.get('name')
            person.age = request.POST.get('age')
            person.save()
            return redirect('index')
        else:
            return render(request, 'crud/edit_form.html', {'person': person})
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')

def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return redirect('index')
    except Person.DoesNotExist:
        return HttpResponseNotFound('<h2>Person not found</h2>')