from django.shortcuts import render, get_object_or_404
from .models import Classes

# Create your views here.
def home(request):
    return render(request, 'phishproofapi/home.html', {'home': home})
def class_list(request):
    class_list = Classes.objects.all()
    return render(request, 'phishproofapi/class_list.html', {'class_list': class_list})

def class_description(request, pk):
    classes = get_object_or_404(Classes, pk=pk)
    return render(request, 'phishproofapi/class_description.html', {'classes': classes})