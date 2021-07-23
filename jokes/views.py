from django.shortcuts import render
import pyjokes
# Create your views here.
def index(request):
    jokes=pyjokes.get_joke()
    return render(request,'index.html',{'jokes':jokes})