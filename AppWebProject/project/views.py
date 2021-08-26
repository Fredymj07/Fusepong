from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, UserStory, Ticket, Status, Comment
from .forms import AddProjectForm, AddStoryForm, AddTicketForm, AddCommentForm

# Create your views here.
def ProjectList(request):
    project_list = Project.objects.order_by('id')
    return render(request, 'project/project_list.html', {'project_list':project_list})

def AddProject(request):
    if request.method=='POST':
        projectForm = AddProjectForm(request.POST)
        if projectForm.is_valid():
            data = Project()
            data.name = projectForm.cleaned_data['name']
            data.description = projectForm.cleaned_data['description']
            data.client = projectForm.cleaned_data['client']
            data.project_type = projectForm.cleaned_data['project_type']
            data.save()
            return redirect('project:Projects')
    else:
        projectForm = AddProjectForm()
    return render(request, 'project/add_project.html', {'projectForm': projectForm})

def UserStoryList(request):
    story_list = UserStory.objects.order_by('id')
    return render(request, 'userstory/story_list.html', {'story_list':story_list})

def AddUserStory(request):
    if request.method=='POST':
        storyForm = AddStoryForm(request.POST, request.FILES)
        if storyForm.is_valid():
            data = UserStory()
            data.title = storyForm.cleaned_data['title']
            data.description = storyForm.cleaned_data['description']
            data.project = storyForm.cleaned_data['project']
            data.uploaded_file = storyForm.cleaned_data['uploaded_file']
            data.save()
            return redirect('project:Stories')
    else:
        storyForm = AddStoryForm()
    return render(request, 'userstory/add_story.html', {'storyForm': storyForm})

def TicketList(request):
    ticket_list = Ticket.objects.order_by('id')
    return render(request, 'ticket/ticket_list.html', {'ticket_list':ticket_list})

def AddTicket(request):
    if request.method=='POST':
        ticketForm = AddTicketForm(request.POST, request.FILES)
        if ticketForm.is_valid():
            data = Ticket()
            data.user_story = ticketForm.cleaned_data['user_story']
            data.title = ticketForm.cleaned_data['title']
            data.description = ticketForm.cleaned_data['description']
            data.status = Status.objects.get(id=1)
            data.priority = ticketForm.cleaned_data['priority']
            data.uploaded_file = ticketForm.cleaned_data['uploaded_file']
            data.save()
            return redirect('project:Tickets')
    else:
        ticketForm = AddTicketForm()
    return render(request, 'ticket/add_ticket.html', {'ticketForm':ticketForm})

def CancelTicket(request, id):
    cancelTicket = get_object_or_404(Ticket, pk=id)
    if cancelTicket:
        cancelTicket.status = Status.objects.get(id=4)
        cancelTicket.save()
        messages.success(request, 'Ticket cancelado correctamente')
    return redirect('project:Tickets')

def DetailTicket(request, id):
    detailTicket = get_object_or_404(Ticket, pk=id)
    try:
        comment_list = Comment.objects.filter(ticket=detailTicket.id)
    except ObjectDoesNotExist:
        messages.info(request, 'No existen comentarios para el ticket seleccionado.')
    return render(request, 'ticket/detail_ticket.html', {'detailTicket':detailTicket, 'comment_list':comment_list})

def AddComment(request):
    if request.method=='POST':
        commentForm = AddCommentForm(request.POST)
        if commentForm.is_valid():
            data = Comment()
            data.description = commentForm.cleaned_data['description']
            data.ticket = commentForm.cleaned_data['ticket']
            data.save()
            return redirect('project:Tickets')
    else:
        commentForm = AddCommentForm()
    return render(request, 'comment/add_comment.html', {'commentForm':commentForm})