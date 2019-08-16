from django.shortcuts import render

# Create your views here.
def donate(request):
    return render(request, 'donate/donate.html')
    
def charge(request):
    if request.method == 'GET':
        pass
        #show form
    else:
        pass
        #process form