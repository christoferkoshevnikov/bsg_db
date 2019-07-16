from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.text import slugify
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .forms import (
    UserRegisterForm,
)
from .models import (
    Project,
    Experiment,
    Sample,
)

@login_required
def home_page(request):
    project_list = Project.objects.filter(user=request.user)
    template_name = 'data_db/home.html'
    context = {
        'project_list': project_list.order_by('-published_on'), 
        }
    return render(request, template_name, context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'data_db/register.html', {'form':form})

@login_required
def project_detail(request, slug):
    if request.method == 'GET':
        project = Project.objects.get(slug=slug)
        template = 'data_db/detail.html'
        context = {'project': project, 'sample_list': project.samples.all()}
        return render(request, template, context)

    elif request.method == 'POST':
        """form = ProjectCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            samples = form.cleaned_data['samples']
            
            Project.objects.create(
                slug = slugify(name),
                name = name,
                samples = samples,
                user = request.user
            ).save()
        """
        return HttpResponse("add view")
    elif request.method == 'PUT':
        return HttpResponse("edit view")
    elif request.method == 'DELETE':
        return HttpResponse("delete view")

class ProjectCreateView(LoginRequiredMixin, CreateView):

    model=Project
    template_name = 'data_db/add-project.html'
    fields = ('name', 'samples')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return HttpResponseRedirect(self.model.get_absolute_url(form.instance))
