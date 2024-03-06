from django.http import HttpResponse
from django.shortcuts import render
from taskapp.models import Place

# Create your views here.
def home(request):
    obj=Place.objects.all()
    return render(request,'index.html',{'result':obj})

#def details(request):
 #    return render(request,'details.html')
#def about(request):
 #   return HttpResponse("hello iam about ")
#def contact(request):
 #   return render(request,'contact.html')
#def thanx(request):
 #   return render(request,'thanx.html')
#def demo(request):
 #   return render(request, "demo.html")


#def addition(request):
 #   x = int(request.GET['num1'])
  #  y = int(request.GET['num2'])
   # add=x+y
    #sub=x-y
    #mul=x*y
    #div=x/y

    #return render(request, "result.html", {'add_result':add,'sub_result':sub,'multiply_result':mul,'division_result':div})

