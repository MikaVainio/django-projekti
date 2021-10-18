from django.shortcuts import render

from .models import Tehtava

def todo_listaus(request):
    context = {
        "tehtavat": Tehtava.objects.all(),
    }
    return render(request, 'todos/listaus.html', context)
