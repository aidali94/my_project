from django.shortcuts import render
from animals.models import Animal


def index(request):
    all_animals = Animal.objects.all()
    print(all_animals)
    context = {
        'all_animals': all_animals
    }
    return render(
        request=request,
        template_name='index.html',
        context=context
    )
