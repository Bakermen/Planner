from django.forms.models import BaseModelForm
from django.http import HttpResponse
from .models import JobApplication
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView




class ApplicataionCreateView(CreateView):
    model = JobApplication
    template_name = "new_application.html"
    fields = ["company_name", "job_title", "job_description", "expected_salary"]
    created_at = timezone.now()

    def form_valid(self, form: JobApplication) -> HttpResponse:
        return super().form_valid(form)

class ApplicationListView(ListView):
    model = JobApplication
    template_name = "applications_list.html"

class ApplicationDetailView(DetailView):
    model = JobApplication
    template_name = "application_detail.html"
