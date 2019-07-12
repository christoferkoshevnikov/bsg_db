from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
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

def project_detail(request, slug):
    if request.method == 'GET':
        sample_list = Project.samples.filter(Project = Project)
        template = 'data_db/detail.html'
        context = {'project': Project, 'sample_list': sample_list}
        return render(request, template, context)
    elif request.method == 'POST':
        return HttpResponse("add view")
    elif request.method == 'PUT':
        return HttpResponse("edit view")
    elif request.method == 'DELETE':
        return HttpResponse("delete view")


"""
@login_required
def project_create_view(request):
    form = ProjectModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        #form = ProjectModelForm()
        return redirect("home")
    template_name = 'Projects/add_project.html'
    context = {'form': form}
    return render(request, template_name, context)
"""
"""
    def get(self, request, *args, **kwargs):
        model = Project
        Project = get_object_or_404(Project, slug=kwargs['slug'])
        template = 'data_db/detail.html'
        context = {'Project': Project}
        return render(request, template, context)
"""