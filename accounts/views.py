from django.views import generic
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    model = CustomUser
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
