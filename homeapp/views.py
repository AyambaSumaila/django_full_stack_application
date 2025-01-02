from django.shortcuts import render

# Create your views here.


def index(request):
    template_data= {} 
    template_data['title'] = 'Movies Hub'
    return render(request, 'homeapp/index.html', {'template_data': template_data})



def about(request):
    template_data= {} 
    template_data['title'] = 'About'
    return render(request, 'homeapp/about.html', {'template_data': template_data})

