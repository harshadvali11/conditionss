from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':19,'b':190,'c':98713}
    return render(request,'conditions.html',context=d)