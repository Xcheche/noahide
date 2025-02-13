from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

from .forms import UserForm
# Create your views here.


class SignUp(generic.CreateView):
    form_class = UserForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, f'Account created successfully for {form.cleaned_data.get("username")}')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    