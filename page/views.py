from django.shortcuts import render
from page.models import Slider, Service, Project, Category, Worker, Client


def home(request):
    sliders = Slider.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()
    categories = Category.objects.all()
    workers = Worker.objects.all()
    clients = Client.objects.all()
    context = {
        'sliders':sliders,
        'services':services,
        'projects':projects,
        'categories':categories,
        'workers':workers,
        'clients':clients,
    }
    return render(request, 'page/home.html', context, request.FILES)
