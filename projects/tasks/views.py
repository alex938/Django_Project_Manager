from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tasks
from project.models import Project
from account.models import User

@login_required
def tasklist(request, p_id, pk):
    project = request.user.projects.all().get(pk=p_id)
    taskl = Tasks.objects.filter(project=project).get(pk=pk)

    return render(request, 'tasks/tasklist.html', {
        'project':project,
        'taskl':taskl
    })

@login_required
def add(request, p_id):
    project = request.user.projects.all().get(pk=p_id)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name:
            Tasks.objects.create(project=project, name=name, description=description, created_by=request.user)
            return redirect('/project/{}'.format(p_id))

    return render(request, 'tasks/add.html')

@login_required
def edittasklist(request, p_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=p_id)
    taskl = Tasks.objects.filter(project=project).get(pk=pk)
    print("Form Data:", request.POST)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name:

            print("New Name:", name)
            print("New Description:", description)

            taskl.name = name
            taskl.description = description
            taskl.save()
            return redirect('/project/{}/{}/'.format(p_id, pk))

    return render(request, 'tasks/edittasklist.html', {
        'project':project,
        'taskl':taskl
    })