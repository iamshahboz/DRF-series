from django.http import HttpResponse 

def homepage(request):
    return HttpResponse("<center> <strong> This is the application </strong> </center>")
