from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserListView(
    generic.ListView
):
    queryset = User.objects.all()
    template_name = 'index.html'
    context_object_name = 'users'

class UserCreateView(
    generic.CreateView
):
    queryset = User.objects.all()
    template_name = 'create-user.html'
    success_url = reverse_lazy('users-list')
    form_class = UserCreationForm