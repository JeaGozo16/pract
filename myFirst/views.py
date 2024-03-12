from django.shortcuts import render
from django.http import HttpResponse

def index (request):
        return HttpResponse ("Hello world");

def contact (request):
            msg = "<h3> Email: Jeacute@gmail.com <br/> \
                Telephone: 0912345678\
                    </h3>"
            
            return HttpResponse (msg);

def about (request):
        
        context = {
                'pangalan' : "Jea",
                'apelyido' : "Gozo",
                'edad' : "21",
                'palayaw' : 'Aliling',
                'quiz1': 100,
                'quiz2': 20,
        }

        return render (request, "about.html", context);
