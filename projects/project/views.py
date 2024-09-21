from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.decorators import login_required

@login_required
def project(request):
    projects = Project.objects.filter(created_by=request.user)
    return render(request, 'project/projects.html', {'projects': projects})

@login_required
def project_detail(request, primary_key):
    project = Project.objects.filter(created_by=request.user).get(pk=primary_key)
    return render(request, 'project/project.html', {'project': project, 'user': request.user})

@login_required
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if all([name, description]):
            Project.objects.create(name=name, description=description, created_by=request.user)
            return redirect('/project/')
        else:
            print("Input error!")

    return render(request, 'project/add_project.html')

@login_required
def edit(request, primary_key):
    project = Project.objects.filter(created_by=request.user).get(pk=primary_key)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name:
            project.name = name
            project.description = description
            project.save()
            return redirect('/project/')
        
    return render(request, 'project/edit.html', {'project': project})