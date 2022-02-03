from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django_intro.task.models import Task


# def home(request):
#     items = Task.objects.all()
#     items_string = ''.join(f'<li>{i.title}</li>' for i in items)
#     html = f'''
#     <h1>It works!</h1>
#     <ul>
#     {items_string}
#     </ul>
#     '''
#     return HttpResponse(html)

def home(request):
    context = {
        'title': 'It works from view!',
        'tasks': Task.objects.all(),
    }
    return render(request, 'home.html', context)

