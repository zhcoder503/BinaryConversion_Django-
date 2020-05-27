from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def base(request):
    num=int(request.POST["num"])
    binary=bin(num)
    return render(request,'result.html',{'binary':binary})
