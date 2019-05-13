from django.shortcuts import redirect, render
from django.utils import timezone
from django.http import HttpResponse

# Create your views here.


def nothing(request):
    return HttpResponse("你484想壞壞")
def index(request):
    return render(request, 'blog/index.html', {})