# i have created this file
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse('''<h1>hello shreyas welcome!</h1> <a href="https://www.google.com" </a>Shreyas website ''') #this is example for personal navigators

# def about(request):
#     return HttpResponse("about!")

from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('''<h1>hello shreyas welcome!</h1> <a href="https://www.google.com" </a>Shreyas website ''') #this is example for personal navigators

# def about(request):
#     return HttpResponse("about!")

def index(request):
    # params={'name': 'shreyas'}
    # return HttpResponse("Home")
    return render(request, 'index.html') #return keyword should be placed before render or httpresponse



def anaylize(request):
    #get the text
    djtext=request.GET.get('text','default')
    #check checkbox value
    removef=request.GET.get('removef','off') #replace GET with Post for csrf tokens for understanding
    Captilized=request.GET.get('Captilized','off')#replace GET with Post for csrf tokens for understanding
    Line=request.GET.get('Line','off')#replace GET with Post for csrf tokens for understanding
    spacef=request.GET.get('spacef','off')#replace GET with Post for csrf tokens for understanding
    
    #check with checkbox value is on
    if removef=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        anaylize=""
        for char in djtext:
          if char not in punctuations:
            anaylize=anaylize+char
            params={'purpose':'remove word', 'anaylized_Text':anaylize}    
    
        return render(request,'anaylize.html',params)
    elif(Captilized=='on'):
        anaylize=""
        for char in djtext:
            anaylize=anaylize+char.upper()
        params={'purpose':'change to uppercase', 'anaylized_Text':anaylize}
    
        return render(request,'anaylize.html',params)
        
    elif(Line=='on'):
        anaylize=""
        for char in djtext:
            if char!="\n" and char!="\r": #/r means transport new line
             anaylize=anaylize+char
        params={'purpose':'Line Remove', 'anaylized_Text':anaylize}
    
        return render(request,'anaylize.html',params)
    elif(spacef=='on'):
        anaylize=""
        for index, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
             anaylize=anaylize+char
        params={'purpose':'Line Remove', 'anaylized_Text':anaylize}
    
        return render(request,'anaylize.html',params)
        
    else:
      return HttpResponse('error')





def capfirst(request):
  return HttpResponse("captilize first!")
   
