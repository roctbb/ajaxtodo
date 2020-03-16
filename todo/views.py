from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from todo.models import Task


def index(request):
    return render(request, "index.html")

def get_tasks(request):
    tasks = Task.objects.all()

    answer = []
    for task in tasks:
        answer.append({
            "text": task.text
        })
    return JsonResponse(answer, safe=False)

def add_task(request):
    text = request.GET.get('text', None)
    if text:
        new_task = Task(text=text)
        new_task.save()
        return JsonResponse({"result": "ok"})

    return JsonResponse({"result": "error"})



