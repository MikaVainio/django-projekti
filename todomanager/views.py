from django.shortcuts import render

from .models import Tehtava

def todo_listaus(request):
    context = {
        "tehtavat": Tehtava.objects.all(),
    }
    return render(request, 'todos/listaus.html', context)


def todo_tehtava(request, tehtava_id):
    context = {
        "tehtava": Tehtava.objects.filter(id=tehtava_id).get(),
    }
    return render(request, 'todos/tehtava.html', context)