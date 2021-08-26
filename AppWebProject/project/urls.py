from django.urls import path
from . import views

app_name='project'
urlpatterns = [
    path('Projects/', views.ProjectList, name = 'Projects'),
    path('AddProject/', views.AddProject, name = 'AddProject'),
    path('Stories/', views.UserStoryList, name = 'Stories'),
    path('AddStory/', views.AddUserStory, name = 'AddStory'),
    path('Tickets/', views.TicketList, name = 'Tickets'),
    path('AddTicket/', views.AddTicket, name = 'AddTicket'),
    path('CancelTicket/<int:id>', views.CancelTicket, name='CancelTicket'),
    path('DetailTicket/<int:id>', views.DetailTicket, name='DetailTicket'),
    path('AddComment/', views.AddComment, name='AddComment'),
]
