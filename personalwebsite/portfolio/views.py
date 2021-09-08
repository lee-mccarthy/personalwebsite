from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, TemplateView

from .forms import ContactForm
from .models import Project


class Index(FormView):
    template_name = 'portfolio/index.html'
    form_class = ContactForm
    success_url = reverse_lazy('portfolio:thankyou')

    def form_valid(self, form):
        if form.honeypot_empty():
            form.send_email()
        self.request.session['contact_name'] = form.cleaned_data['name']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.order_by('-pk')
        return context


class ContactMe(FormView):
    template_name = 'portfolio/contact_me.html'
    form_class = ContactForm
    success_url = reverse_lazy('portfolio:thankyou')

    def form_valid(self, form):
        if form.honeypot_empty():
            form.send_email()
        self.request.session['contact_name'] = form.cleaned_data['name']
        return super().form_valid(form)


class ThankYou(TemplateView):
    template_name = 'portfolio/contact_thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.session.pop('contact_name', None)
        return context


class ProjectDetail(DetailView):
    template_name = 'portfolio/project_detail.html'
    model = Project
