from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import toditem

def index(request):
    all_todo_items = toditem.objects.all()
    context = {"all_todo_items":all_todo_items}
    return render(request,'todolist/index.html',context)

def addtodo(request):
    new_item = toditem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todolist/')

def deletetodo(request,todo_id):
    item_to_delete=toditem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todolist/')
