from django import forms
from django.forms import ModelForm, widgets
from core.models import Client
from .models import ProjectType, Project, Ticket, UserStory, Priority, Status

class AddProjectForm(forms.Form):
    name = forms.CharField(label='Nombre', min_length=14, max_length=100, required=True)
    description = forms.CharField(label='Descripción', min_length=20, max_length=600, required=True)
    client = forms.ModelChoiceField(label='Cliente', queryset=Client.objects.all(), required=True)
    project_type = forms.ModelChoiceField(label='Tipo de Proyecto', queryset=ProjectType.objects.all(), required=True)

class AddStoryForm(forms.Form):
    title = forms.CharField(label='Título', min_length=14, max_length=100, required=True)
    description = forms.CharField(label='Descripción', min_length=20, max_length=600, required=True)
    project = forms.ModelChoiceField(label='Proyecto', queryset=Project.objects.all(), required=True)
    uploaded_file = forms.FileField(label='Cargar Archivo')

class AddTicketForm(forms.Form):
    user_story = forms.ModelChoiceField(label='Historia de Usuario', queryset=UserStory.objects.all(), required=True)
    title = forms.CharField(label='Título', min_length=14, max_length=100, required=True)
    description = forms.CharField(label='Descripción', min_length=20, max_length=600, required=True)
    priority = forms.ModelChoiceField(label='Prioridad', queryset=Priority.objects.all(), required=True)
    uploaded_file = forms.FileField(label='Cargar Archivo')

class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'status', 'priority',]
        labels = {
            'title': ('Título'),
            'description': ('Descripción'),
            'status': ('Estado'),
            'priority': ('Prioridad'),
        }
        widgets = {
            'status': forms.Select(attrs={'class':'form-control'}),
            'priority': forms.Select(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk and self.instance.status:
            if self.instance.status == '4':
                self.fields['status'].widget.attrs.update({'disabled': True})

class AddCommentForm(forms.Form):
    description = forms.CharField(label='Comentario', widget=forms.Textarea, min_length=20, max_length=600, required=True)
    ticket = forms.ModelChoiceField(label='Ticket', queryset=Ticket.objects.all(), required=True)