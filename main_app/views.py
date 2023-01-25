from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Watch
from .forms import ServiceForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def watches_index(request):
    watches = Watch.objects.all()
    return render(request, 'watches/index.html', { 'watches': watches })

def watches_detail(request, watch_id):
    watch = Watch.objects.get(id=watch_id)
    service_form = ServiceForm()
    return render(request, 'watches/detail.html', {
        'watch': watch,
        'service_form': service_form
    })

def add_service(request, watch_id):
    form = ServiceForm(request.POST)
    if form.is_valid():
        new_service = form.save(commit=False)
        new_service.watch_id = watch_id
        new_service.save()
    return redirect('detail', watch_id=watch_id)

class WatchCreate(CreateView):
    model = Watch
    fields = '__all__'

class WatchUpdate(UpdateView):
    model = Watch
    fields = '__all__'

class WatchDelete(DeleteView):
    model = Watch
    success_url = '/watches/'