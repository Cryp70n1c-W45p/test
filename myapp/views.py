from django import forms
from myapp.models import Image
from django.shortcuts import render
from .forms import ImageForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    imgs = Image.objects.all()
    return render(request, 'index.html',{'form':form,'imgs':imgs})
