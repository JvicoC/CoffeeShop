from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class RegisterView(generic.FormView):
    form_class=UserCreationForm
    template_name="users/register.html"
    success_url=reverse_lazy('list_product')