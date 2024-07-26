from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.shortcuts import render  


# admin@123 --> password for user:umesh_222

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user has entered correct credentials or not.
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # A backend authenticated the credentials
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')


    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return render(request,'login.html')


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    # Check Checkbox Value:
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

   

    purpose = ''
    # Check which checkbox is ON:
    if removepunc == 'on':            
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        purpose += "Punctuation Remover"
        params = {'purpose':purpose,'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps == 'on':
        analyzed=''
        for char in djtext:
            analyzed = analyzed + char.upper()
        purpose += "|Changed to Uppercase"
        params = {'purpose':purpose,'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover == 'on':
        analyzed=''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        purpose += "|New Line Remover"
        params = {'purpose':purpose,'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(removepunc != 'on' and fullcaps != 'on'and newlineremover != 'on'):
        return HttpResponse("Please Select any Operation and Try Again!!!!")


    # else:
    #     return HttpResponse("Error")
    return render(request, 'analyze.html', params)

def capfirst(request):
    return HttpResponse("Capitalize first")

def newlineremove(request):
    return HttpResponse("New line remover")

def spaceremove(request):
    return HttpResponse("Spacce remover <a href='/'>Backk</a>")

def charcount(request):
    return HttpResponse("Char count")