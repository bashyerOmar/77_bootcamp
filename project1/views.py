from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    context = {
        "msg": "hello",
        "title":"bootcamp 7/7",
    }
    return render(request, 'hello.html', context)


