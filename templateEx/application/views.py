from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.  views use for backend logic and in views also write html code but it basicaly use for backend logic
def my_fun(request):
    
    #1 return HttpResponse("<h1>Hello, my name is Rani</h1>")

    # return HttpResponse(request,'application/hello.html')
    
    
   

    #2 html = "<h1>Hello, my name is Rani</h1>"
    # return HttpResponse(html)



#3     html = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Django Project</title>
#     <style>
#     body{
#     backgraound-color: #f0f0f0;
#     font-family:Arial;
#     color:#333;
#     }
#     .container{
#     max-width: 800px;
#     margin: 0 auto;
#     padding: 20px;
#     backgraound-color: #fff;
#     border-radius: 5px;
#     box-shadow: 0 2px 4px rgba(0,0,0,0.1);
#     }
#     </style>
# </head>
# <body>
#      <div class="container">
#      <h1>vaishnavi Bhonde</h1>
#      <p>My name is vaishnavi bhonde, i am from Amravati</p>
#      <p>I have completed master of computer application from SGBA university in 2024 </p>
#      </div>
# </body>
# </html>
# '''
#     return HttpResponse(html)


#4 if you wnat to pass context to the template, you can do this like this :

    # return render(request,'application/hello.html')


    # context = {
    #         'key1':'value1',
    #         'key2':'value2',
    #   }
    # return render (
    #         request,
    #        'hello.html', #this is your tepmlate file name
    #        context = context, #this is dictinary for your context variable
    #        context_type = "text/html",
    #        status=200,
    #        using=None,
    # )
      
     
    # this nm variable use in html file 
    return render(request,'application/hello.html',{'nm':'Joshi'})
    


