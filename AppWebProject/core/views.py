from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AddClientForm
from .models import Client
from project.models import Project

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

# def ProjectTypeList(request):
#     # project_type_list = Project.objects.order_by('id')
#     # print(project_type_list)
#     # return render(request, 'core/index.html', {'project_type_list':project_type_list})
#     client_list = Client.objects.order_by('id')
#     print(client_list)
#     return render(request, 'core/index.html', {'client_list':client_list})

@login_required
def ClientList(request):
    client_list = Client.objects.order_by('id')
    return render(request, 'client/client_list.html', {'client_list':client_list})

@login_required
def AddClient(request):
    if request.method=='POST':
        clientForm = AddClientForm(request.POST)

        if clientForm.is_valid():
            data = Client()
            data.name = clientForm.cleaned_data['name']
            data.last_name = clientForm.cleaned_data['last_name']
            data.address = clientForm.cleaned_data['address']
            data.document_type = clientForm.cleaned_data['document_type']
            data.document_number = clientForm.cleaned_data['document_number']
            data.phone = clientForm.cleaned_data['phone']
            data.email = clientForm.cleaned_data['email']
            data.save()
            return redirect('core:Clients')
    else:
        clientForm = AddClientForm()
    return render(request, 'client/add_client.html', {'clientForm': clientForm})