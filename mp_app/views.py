from django.shortcuts import render
from django.views.generic import View, ListView

from mp_app.models import Client


# Create your views here.

class LlistarClientsView(ListView):
    model = Client
    template_name = 'list_clients.html'
    context_object_name = 'clients'

    def get_queryset(self):
        return Client.objects.filter(actiu=True)

class DetallClientView(View):
    model = Client
    def get(self, request, *args, **kwargs):
        client = Client.objects.get(pk=kwargs['id_client'])
        return render(request, "client/detall_client.html", {'client': client})
