from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import  AddressEntry


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


# Create your views here.
# @login_required(login_url="login/")
# class IndexView(LoginRequiredMixin, generic.ListView):
# class IndexView(ListView):
#     template_name = 'address_book/index.html'
#     context_object_name = 'addressbook_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return AddressEntry.objects.all()


class AddressList(ListView):
    model = AddressEntry

class AddressCreate(CreateView):
    model = AddressEntry
    success_url = reverse_lazy('address_list')
    fields = ['first_name', 'last_name', 'email_address', 'street_address']

class AddressUpdate(UpdateView):
    model = AddressEntry
    success_url = reverse_lazy('address_list')
    fields = ['first_name', 'last_name', 'email_address', 'street_address']

class AddressDelete(DeleteView):
    model = AddressEntry
    success_url = reverse_lazy('address_list')